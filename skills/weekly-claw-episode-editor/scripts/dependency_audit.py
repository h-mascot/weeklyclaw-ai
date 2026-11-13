#!/usr/bin/env python3
"""Read-only package link and explicit runtime-prerequisite inventory; not QA approval."""
import argparse, hashlib, json, re
from pathlib import Path
from urllib.parse import unquote, urlsplit

RUNTIME = {
 'editing': ['verified episode source inventory and offsets', 'approved baseline master/hash and comparison', 'native editor/renderer and effect support', 'ffmpeg and ffprobe', 'Pillow and licensed footer fonts', 'official mark and approved original outro/music'],
 'publishing': ['authenticated permitted browser', 'verified target channel tuple and upload permission', 'exact thumbnail and release approval', 'work/publishing/platform-rollout.md for requested non-YouTube surfaces'],
 'community': ['authorized destination ledger, current rules and receipts', 'verified media-capable WhatsApp route if requested'],
 'thumbnail': ['current episode real participant frames', 'likeness-generation authorization', 'approved prior thumbnail style reference', 'available authorized image-generation capability', 'independent reviewer'],
 'scheduler': ['verified canonical owner and existing manager state; never create from package presence alone']
}
def audit(root):
 root=Path(root).resolve(); links=[]; files=[]
 for p in sorted(root.rglob('*')):
  if not p.is_file() or '__pycache__' in p.parts: continue
  files.append({'path':str(p.relative_to(root)), 'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
  if p.suffix!='.md': continue
  for ref in re.findall(r'\]\(([^)]+)\)', p.read_text()):
   ref=ref.strip().split(' "',1)[0]; u=urlsplit(ref)
   if u.scheme or ref.startswith('#'): continue
   q=(p.parent/unquote(u.path)).resolve()
   if not u.path: continue
   links.append({'source':str(p.relative_to(root)),'target':ref,'exists':q.exists(),'in_package':q.is_relative_to(root)})
 missing=[r for r in links if not r['exists']]; outside=[r for r in links if not r['in_package']]
 return {'status':'BUNDLED_LINKS_PRESENT_RUNTIME_UNVERIFIED' if not missing and not outside else 'INCOMPLETE_BUNDLE','files':files,'missing_links':missing,'outside_links':outside,'runtime_prerequisites_unverified':RUNTIME,'limitations':'Markdown link audit only. Backtick paths, runtime tools/assets/permissions and semantic correctness require stage-specific verification.'}
def write_report(path, report):
 with Path(path).open('x') as f:
  f.write(json.dumps(report,indent=2)+'\n')

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('root');ap.add_argument('--report',required=True);a=ap.parse_args();r=audit(a.root);write_report(a.report,r);print(r['status']);raise SystemExit(bool(r['missing_links'] or r['outside_links']))
