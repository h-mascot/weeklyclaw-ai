#!/usr/bin/env python3
"""Ep27 rev3 render-QA at 1600x900 with Playwright (mirrors render_qa_rev2.py)."""
import asyncio, json, sys, pathlib
from playwright.async_api import async_playwright

DECK = pathlib.Path('/home/henrymascot/weeklyclaw/episodes/27/showprep/revs/deck.rev3.html').resolve()
OUT = pathlib.Path('/home/henrymascot/weeklyclaw/episodes/27/showprep/qa/render-1600x900-rev3')
OUT.mkdir(parents=True, exist_ok=True)

CANARIES = [
    ('s-title', 'Weekly Claw'),
    ('s-title', 'Episode 27'),
    ('s-cold-open', 'consolidation'),
    ('s-seg-nvidia-hf', 'Hugging Face'),
    ('s-seg-glm-flash', 'GLM-5.3-Flash'),
    ('s-seg-openai-stack', 'Jalape'),
    ('s-seg-instinct-raise', '$2.5 billion'),
    ('s-seg-openai-agi', 'AGI by December'),
    ('s-seg-qwen-flash-next', 'Qwen3.8-Flash-Next'),
    ('s-seg-headlong', 'Headlong'),
    ('s-seg-portable-computer', 'Portable Computer'),
    ('s-seg-robot-data', 'Figure'),
    ('s-signal-outside', 'Codex'),
    ('s-hot-take', 'deployment layer'),
    ('s-watch', 'September 4'),
    ('s-sources', 'cnbc.com'),
]

async def main():
    bad = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=['--no-sandbox'], executable_path='/usr/bin/google-chrome')
        page = await browser.new_page(viewport={'width': 1600, 'height': 900})
        await page.goto(DECK.as_uri(), wait_until='networkidle')
        slide_ids = await page.eval_on_selector_all('.slide', 'els=>els.map(e=>e.id)')
        print(f'SLIDES={len(slide_ids)} {slide_ids}')
        results = []
        for i, sid in enumerate(slide_ids):
            await page.evaluate(
                '(i)=>{document.querySelectorAll(".slide").forEach(e=>e.style.transition="none");'
                'document.querySelectorAll(".slide").forEach((e,j)=>e.classList.toggle("active",i===j))}', i)
            await page.wait_for_timeout(80)
            r = await page.evaluate('''(sid)=>{
                const s=document.getElementById(sid);
                if(!s) return {id:sid, missing:true};
                const c=s.querySelector('.content');
                if(!c) return {id:sid, missingContent:true};
                const cr=c.getBoundingClientRect();
                const els=[...c.querySelectorAll('h1,h2,h3,p,li,a,img,table,.card,.quote-block')];
                let overlaps=0;
                for(let i=0;i<els.length;i++){
                    let a=els[i].getBoundingClientRect();
                    if(!a.width||!a.height) continue;
                    for(let j=i+1;j<els.length;j++){
                        let b=els[j].getBoundingClientRect();
                        if(!b.width||!b.height) continue;
                        if(a.left<b.right-2&&a.right>b.left+2&&
                           a.top<b.bottom-2&&a.bottom>b.top+2&&
                           !els[i].contains(els[j])&&!els[j].contains(els[i])) overlaps++;
                    }
                }
                return {id:sid,
                        overflow: cr.top<42||cr.bottom>840||cr.left<30||cr.right>1570,
                        scrollOverflow: c.scrollHeight>c.clientHeight+2||c.scrollWidth>c.clientWidth+2,
                        overlaps: overlaps, contentH: c.clientHeight, contentScrollH: c.scrollHeight};
            }''', sid)
            # h2 overflow check
            h2r = await page.evaluate('''(sid)=>{
                const s=document.getElementById(sid); const h=s&&s.querySelector('h2');
                if(!h) return null; return {sh:h.scrollHeight, ch:h.clientHeight};
            }''', sid)
            if h2r and h2r['sh'] - h2r['ch'] > 4:
                r['h2overflow'] = h2r['sh'] - h2r['ch']
            await page.screenshot(path=str(OUT / f'{i+1:02d}-{sid}.png'))
            results.append(r)
        for r in results:
            flag = []
            if r.get('overflow'): flag.append('OVERFLOW')
            if r.get('scrollOverflow'): flag.append(f"SCROLL({r['contentScrollH']-r['contentH']})")
            if r.get('overlaps', 0) > 0: flag.append(f"OVL={r['overlaps']}")
            if r.get('h2overflow'): flag.append(f"H2OVL={r['h2overflow']}")
            if r.get('missing'): flag.append('MISSING')
            if r.get('missingContent'): flag.append('NO_CONTENT')
            print(f"  [{r['id']:28s}] {'FAIL ' + ','.join(flag) if flag else 'ok'}")
            if flag: bad.append(r)
        for sid, canary in CANARIES:
            present = await page.evaluate(f'''()=>{{
                const s=document.getElementById({sid!r});
                if(!s) return false;
                return s.innerHTML.includes({canary!r});
            }}''')
            if not present:
                print(f'CANARY_FAIL: {sid} missing "{canary}"')
                bad.append({'id': sid, 'canary_missing': canary})
        await browser.close()
    if bad:
        print('=== RENDER-QA FAIL (rev3) ===')
        print(json.dumps(bad, indent=2))
        sys.exit(1)
    print('=== RENDER-QA PASS (rev3) ===')

asyncio.run(main())
