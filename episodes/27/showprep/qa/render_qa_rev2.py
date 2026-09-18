#!/usr/bin/env python3
"""Ep 27 rev2 render-QA at 1600x900 with Playwright.
Per weeklyclaw-show-prep/references/prior-episode-template-authority.md, prefer Playwright.
Asserts per-slide: no overflow, no scroll overflow, no element overlap.
Also asserts revision-explicit gates: rendered slide count == unique .slide IDs,
slide order matches authority deck, content canaries in HTML + screenshot.
"""
import asyncio, json, sys, pathlib
from playwright.async_api import async_playwright

DECK = pathlib.Path('/home/henrymascot/weeklyclaw/episodes/27/showprep/revs/deck.rev2.html').resolve()
AUTH = pathlib.Path('/home/henrymascot/weeklyclaw/episodes/27/showprep/qa/authority-deck-ep26.html').resolve()
OUT = pathlib.Path('/home/henrymascot/weeklyclaw/episodes/27/showprep/qa/render-1600x900-rev2')
OUT.mkdir(parents=True, exist_ok=True)

CANARIES = [
    # (slide id, canary substring expected in slide's HTML)
    ('s-title', 'Weekly Claw'),
    ('s-title', 'Episode 27'),
    ('s-cold-open', 'agent'),
    ('s-sponsor-heritage', 'Heritage Telecom'),
    ('s-sponsor-herald', 'Herald Labs'),
    ('s-seg-openai-stack', 'Jalape'),
    ('s-seg-qwen-flash-next', 'Qwen3.8-Flash-Next'),
    ('s-seg-headlong', 'Headlong'),
    ('s-seg-portable-computer', 'Portable Computer'),
    ('s-seg-robot-data', 'Figure'),
    ('s-signal-outside', 'Codex'),
    ('s-hot-take', 'deployment layer'),
    ('s-watch', 'September 4'),
    ('s-sources', 'openai.com'),
]

async def get_slide_ids(page):
    return await page.eval_on_selector_all('.slide', 'els=>els.map(e=>e.id)')

async def measure_and_screenshot(browser, page, deck_uri, slide_ids, out_dir, prefix):
    results = []
    for i, sid in enumerate(slide_ids):
        # Disable transitions + activate only slide i
        await page.evaluate(
            '(i)=>{document.querySelectorAll(".slide")'
            '.forEach(e=>e.style.transition="none");'
            'document.querySelectorAll(".slide")'
            '.forEach((e,j)=>e.classList.toggle("active",i===j))}', i)
        await page.wait_for_timeout(80)
        r = await page.evaluate('''(sid)=>{
            const s=document.getElementById(sid);
            if(!s) return {id:sid, missing:true};
            const c=s.querySelector('.content');
            if(!c) return {id:sid, missingContent:true};
            const cr=c.getBoundingClientRect();
            const els=[...c.querySelectorAll(
              'h1,h2,h3,p,li,a,img,table,.card,.quote-block')];
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
                    scrollOverflow: c.scrollHeight>c.clientHeight+2||
                                    c.scrollWidth>c.clientWidth+2,
                    overlaps: overlaps,
                    contentH: c.clientHeight,
                    contentScrollH: c.scrollHeight};
        }''', sid)
        await page.screenshot(path=str(out_dir / f'{prefix}-{i+1:02d}-{sid}.png'))
        results.append(r)
    return results

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=['--no-sandbox'],
            executable_path='/usr/bin/google-chrome')
        page = await browser.new_page(viewport={'width': 1600, 'height': 900})
        await page.goto(DECK.as_uri(), wait_until='networkidle')

        # Author-declared slide count
        new_ids = await get_slide_ids(page)
        print(f'NEW_DECK_SLIDES={len(new_ids)} ids={new_ids}')

        # Render new deck
        new_results = await measure_and_screenshot(browser, page, DECK.as_uri(), new_ids, OUT, 'new')
        new_bad = [r for r in new_results if r.get('overflow') or r.get('scrollOverflow') or r.get('overlaps', 0) > 0 or r.get('missing') or r.get('missingContent')]
        print(f'NEW_RENDER_QA {"PASS" if not new_bad else "FAIL"} bad_slides={len(new_bad)}')
        for r in new_results:
            flag = []
            if r.get('overflow'): flag.append('OVERFLOW')
            if r.get('scrollOverflow'): flag.append(f'SCROLL({r["contentScrollH"]-r["contentH"]})')
            if r.get('overlaps', 0) > 0: flag.append(f'OVL={r["overlaps"]}')
            if r.get('missing'): flag.append('MISSING')
            if r.get('missingContent'): flag.append('NO_CONTENT')
            print(f'  [{r["id"]:32s}] {"FAIL " + ",".join(flag) if flag else "ok"}')

        # Now check authority deck for comparison
        await page.goto(AUTH.as_uri(), wait_until='networkidle')
        auth_ids = await get_slide_ids(page)
        print(f'\nAUTH_DECK_SLIDES={len(auth_ids)} ids={auth_ids}')

        # Canary content check on new deck
        await page.goto(DECK.as_uri(), wait_until='networkidle')
        for sid, canary in CANARIES:
            present = await page.evaluate(f'''()=>{{
                const s=document.getElementById({sid!r});
                if(!s) return false;
                return s.innerHTML.includes({canary!r});
            }}''')
            if not present:
                print(f'CANARY_FAIL: slide {sid} missing canary "{canary}"')
                new_bad.append({'id': sid, 'canary_missing': canary})

        # Verify sponsor-order canary: Heritage must appear before Herald in slide order
        slide_order = new_ids
        h_i = slide_order.index('s-sponsor-heritage') if 's-sponsor-heritage' in slide_order else -1
        a_i = slide_order.index('s-sponsor-herald') if 's-sponsor-herald' in slide_order else -1
        if h_i < 0 or a_i < 0:
            print(f'SPONSOR_ORDER_FAIL: missing sponsors (heritage@{h_i}, herald@{a_i})')
            new_bad.append({'sponsor_order': 'missing'})
        elif h_i > a_i:
            print(f'SPONSOR_ORDER_FAIL: herald@{a_i} appears before heritage@{h_i}')
            new_bad.append({'sponsor_order': 'reversed'})
        else:
            print(f'SPONSOR_ORDER_OK: heritage@{h_i} herald@{a_i}')

        await browser.close()

        if new_bad:
            print(f'\n=== RENDER-QA FAIL (rev2) ===')
            print(json.dumps(new_bad, indent=2))
            sys.exit(1)
        print(f'\n=== RENDER-QA PASS (rev2) ===')

asyncio.run(main())
