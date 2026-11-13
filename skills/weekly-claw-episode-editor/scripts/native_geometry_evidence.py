#!/usr/bin/env python3
"""Check declared geometry + actual XML bindings + hashed rendered evidence.
NOT an MLT semantic adapter, face detector, privacy review or release validator.
"""
import argparse, hashlib, json, math, subprocess, xml.etree.ElementTree as ET
from pathlib import Path
from PIL import Image

OLD_PROFILE = 'native-evidence-2026-10-03.1'
NEW_PROFILE = 'native-evidence-2026-10-04.1'

def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for c in iter(lambda:f.read(1048576),b''):h.update(c)
 return h.hexdigest()
def vec(v,n):
 if not isinstance(v,list) or len(v)!=n or any(type(x) not in (int,float) or not math.isfinite(x) for x in v):raise ValueError('invalid finite geometry')
 return v

def integer_vec(v,n,name):
 if not isinstance(v,list) or len(v)!=n or any(type(x) is not int for x in v):
  raise ValueError(name+' requires explicit integer geometry')
 return v

def _review_evidence(transform):
 """Return the explicit per-transform enlargement review record, if any.

 The new profile intentionally does not interpret an ``approved`` flag as
 evidence.  A source-limited enlargement needs a real hashed review artifact
 and a plain-language limitation/reason.
 """
 for key in ('source_limited_enlargement', 'enlargement_review', 'scale_exception'):
  value=transform.get(key)
  if value is not None:
   return value
 return None

def _require_review_evidence(item, root):
 if not isinstance(item,dict):
  raise ValueError('source-limited enlargement review must be an object')
 reason=item.get('limitation_reason') or item.get('reason')
 evidence=item.get('review_evidence') or item.get('evidence')
 if not isinstance(reason,str) or not reason.strip():
  raise ValueError('source-limited enlargement limitation/reason required')
 if not isinstance(evidence,dict) or not evidence.get('path') or not evidence.get('sha256'):
  raise ValueError('source-limited enlargement hashed review evidence required')
 p=Path(evidence['path']);p=p if p.is_absolute() else root/p
 if not p.is_file() or sha(p)!=evidence['sha256']:
  raise ValueError('source-limited enlargement review evidence missing/changed: '+str(p))

def _group_viewports(state):
 """Normalize the small accepted group-state shape without guessing layout."""
 if not isinstance(state,dict):
  raise ValueError('group state must be an object')
 members=state.get('members')
 viewports=state.get('viewports')
 if isinstance(viewports,dict):
  rows=[]
  for member, viewport in viewports.items():
   rows.append({'member':member,'viewport':viewport})
  viewports=rows
 if not isinstance(members,list) or any(type(m) is not str or not m for m in members):
  raise ValueError('group state members must be a nonempty string list')
 if not isinstance(viewports,list):
  raise ValueError('group state viewports must be a list or member map')
 normalized=[]
 for row in viewports:
  if not isinstance(row,dict):
   raise ValueError('group state viewport must be an object')
  member=row.get('member',row.get('id',row.get('transform')))
  transform=row.get('transform',member)
  viewport=row.get('viewport',row.get('rect'))
  if not isinstance(member,str) or not member or not isinstance(transform,str) or not transform or viewport is None:
   raise ValueError('group state viewport requires member, transform and viewport')
  normalized.append((member,transform,integer_vec(viewport,4,'group viewport')))
 return members,normalized

def _check_group_states(data, transforms, canvas, fail):
 states=data.get('group_states')
 if not isinstance(states,list) or not states:
  fail('new profile requires declared group states')
  return
 cw,ch=integer_vec(canvas,2,'canvas')
 transform_by_id={t.get('id'):t for t in transforms if isinstance(t,dict)}
 for state in states:
  try:
   members,rows=_group_viewports(state)
   if len(members)<2:
    raise ValueError('group state requires at least two members')
   if len(set(members))!=len(members):
    raise ValueError('group state has duplicate members')
   row_members=[member for member,_,_ in rows]
   if len(set(row_members))!=len(row_members) or set(row_members)!=set(members):
    raise ValueError('group state members and viewports must match exactly')
   row_transforms=[transform for _,transform,_ in rows]
   if len(set(row_transforms))!=len(row_transforms) or not set(row_transforms).issubset(transform_by_id):
    raise ValueError('group state references an undeclared transform')
   ordered=sorted((viewport[0],viewport[2],member,transform,viewport) for member,transform,viewport in rows)
   cursor=0
   for x,w,member,transform,viewport in ordered:
    y=viewport[1];h=viewport[3]
    if y!=0 or h!=ch or x!=cursor or w<=0 or x+w>cw:
     raise ValueError('group state viewports must be full-height contiguous horizontal tiles')
    declared=transform_by_id[transform].get('viewport')
    if declared is not None and declared!=viewport:
     raise ValueError('group state viewport does not match transform viewport: '+transform)
    cursor=x+w
   if cursor!=cw:
    raise ValueError('group state viewports must tile the full canvas with no gap')
  except (KeyError,TypeError,ValueError) as exc:
   fail('invalid group state: '+str(exc))

def check(data, root):
 root=Path(root); errors=[]; measurements=[]
 def fail(s):errors.append(s)
 def hashed(item):
  p=Path(item['path']);p=p if p.is_absolute() else root/p
  if not p.is_file() or sha(p)!=item['sha256']:raise ValueError('missing/changed evidence: '+str(p))
  return p
 try:
  project=hashed(data['project']); xml=ET.parse(project).getroot()
  profile=xml.find('profile')
  if profile is None or [int(profile.get('width',0)),int(profile.get('height',0))]!=data['canvas']:fail('actual project canvas mismatch')
  profile_name=data.get('profile')
  if profile_name not in (OLD_PROFILE,NEW_PROFILE):fail('unsupported profile')
  new_profile=profile_name==NEW_PROFILE
  cw,ch=vec(data['canvas'],2)
  if cw<=0 or ch<=0:fail('invalid canvas')
  if data.get('deliverable_kind')=='full_episode' and [cw,ch]!=[1920,1080]:fail('full episode must remain landscape 1920x1080')
  if not data.get('transforms'):fail('no transforms')
  for t in data.get('transforms',[]):
   name=t['id'];src=hashed(t['source']);sw,sh=vec(t['source_size'],2)
   actual=json.loads(subprocess.check_output(['ffprobe','-v','error','-select_streams','v:0','-show_entries','stream=width,height','-of','json',str(src)]))['streams'][0]
   if [actual['width'],actual['height']] != [sw,sh]:fail(name+': source dimensions mismatch actual probe')
   w,h,x,y=vec(t['crop'],4);ow,oh=vec(t['scale'],2);vx,vy,vw,vh=vec(t['viewport'],4)
   if min(sw,sh,w,h,ow,oh,vw,vh)<=0 or min(x,y,vx,vy)<0 or x+w>sw or y+h>sh:fail(name+': invalid crop/source geometry')
   if ow>w+1e-8 or oh>h+1e-8:
    if not new_profile:
     fail(name+': enlargement')
    else:
     _require_review_evidence(_review_evidence(t),root)
   if w<=0 or h<=0 or abs(ow/w-oh/h)>0.001:fail(name+': aspect distortion')
   if ow>vw or oh>vh or vx+vw>cw or vy+vh>ch:fail(name+': output does not fit viewport/canvas')
   if new_profile and [ow,oh]!=[vw,vh]:fail(name+': full-frame group picture must fill its declared viewport')
   if not t.get('native_bindings') or not t.get('conversion_explanation'):fail(name+': actual native bindings/conversion explanation missing')
   for b in t.get('native_bindings',[]):
    matches=xml.findall(b['xpath'])
    if len(matches)!=1 or matches[0].text!=b['text']:fail(name+': native XML binding mismatch: '+b['xpath'])
  if new_profile:
   _check_group_states(data,data.get('transforms',[]),data['canvas'],fail)
  tol=data['tolerances']; eye=tol['eye_spread_px'];face=tol['max_face_ratio'];head=tol['headroom_spread_px']
  if not all(type(v) in (int,float) and math.isfinite(v) for v in [eye,face,head]) or not 0<eye<=50 or not 1<=face<=1.15 or head<0:fail('invalid or silently weakened review tolerance')
  if not tol.get('headroom_rationale'):fail('episode-specific headroom tolerance rationale missing')
  if not data.get('samples'):fail('no actual rendered samples')
  for s in data.get('samples',[]):
   ip=hashed(s['image'])
   with Image.open(ip) as im:
    if list(im.size)!=data['canvas']:fail(s['id']+': rendered sample dimensions mismatch canvas')
    im.verify()
   with Image.open(ip) as im:
    im.load()
   people=s['people'];eyes=[];faces=[];heads=[]
   if len(people)<2:fail('group measurement requires at least two visible people')
   for p in people:
    top,bottom,crown,ey,chin,left,right=vec([p[k] for k in ('viewport_top','viewport_bottom','crown','eyes','chin','face_left','face_right')],7)
    vl,vr=vec(p['viewport_horizontal'],2)
    if not 0<=top<crown<ey<chin<bottom<=ch or not 0<=vl<left<right<vr<=cw:fail(s['id']+': clipped/invalid face envelope')
    eyes.append(ey);faces.append(chin-crown);heads.append(crown-top)
   if eyes:
    m={'id':s['id'],'eye_spread_px':max(eyes)-min(eyes),'face_ratio':max(faces)/min(faces) if min(faces)>0 else None,'headroom_spread_px':max(heads)-min(heads)};measurements.append(m)
    if m['eye_spread_px']>eye or (m['face_ratio'] is None or m['face_ratio']>face) or m['headroom_spread_px']>head:fail(s['id']+': group matching tolerance exceeded')
  if not data.get('native_semantics_review',{}).get('evidence'):fail('native effect semantic mapping review evidence absent')
  else:hashed(data['native_semantics_review']['evidence'])
 except (KeyError,ValueError,TypeError,OSError,ET.ParseError,ZeroDivisionError,subprocess.CalledProcessError,IndexError) as e:fail(str(e))
 return {'status':'FAILED' if errors else 'CHECKED_SUBSET_PENDING_REVIEW','errors':errors,'measurements':measurements,'limits':'Numeric declarations and exact XML/hash bindings only. Verify MLT effect semantics, measured face coordinates, complete motion/privacy and exact-master listening separately. Never a release PASS.'}
def write_report(path, report):
 with Path(path).open('x') as f:
  f.write(json.dumps(report,indent=2,allow_nan=False)+'\n')

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('plan');ap.add_argument('--report',required=True);a=ap.parse_args();p=Path(a.plan);r=check(json.loads(p.read_text()),p.parent);r['plan_sha256']=sha(p);r['validator_sha256']=sha(__file__);write_report(a.report,r);print(r['status']);raise SystemExit(bool(r['errors']))
