#!/usr/bin/env python3
"""Sync local WeeklyClaw archive folders into the static website repo.

Default source: /home/henrymascot/weeklyclaw
Default destination: current repo root

This intentionally does not delete repo files. It only copies/updates episode files,
regenerates simple agenda HTML pages, and refreshes the homepage/episode archive
latest-card metadata.
"""
from __future__ import annotations

import argparse
import html
import os
import re
import shutil
import subprocess
from pathlib import Path

MONTH_RE = r"(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:t(?:ember)?)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)"


def repo_root_from_script() -> Path:
    return Path(__file__).resolve().parents[1]


def copy_tree_merge(src: Path, dst: Path) -> None:
    for root, dirs, files in os.walk(src):
        dirs[:] = [d for d in dirs if d not in {"legacy-week-page", "recordings"}]
        rel = Path(root).relative_to(src)
        out = dst / rel
        out.mkdir(parents=True, exist_ok=True)
        for name in files:
            s = Path(root) / name
            d = out / name
            d.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(s, d)


def strip_tags(s: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s)).strip()


def deck_meta(repo: Path, ep: int) -> dict[str, str]:
    deck = repo / "episodes" / str(ep) / "deck.html"
    agenda = repo / "episodes" / str(ep) / "agenda.md"
    text = deck.read_text(errors="ignore") if deck.exists() else ""
    title = ""
    m = re.search(r"<title>(.*?)</title>", text, re.I | re.S)
    if m:
        title = strip_tags(m.group(1))
    h = re.search(r"<h1[^>]*>(.*?)</h1>", text, re.I | re.S) or re.search(r"<h2[^>]*>(.*?)</h2>", text, re.I | re.S)
    headline = strip_tags(h.group(1)) if h else title
    if not headline:
        headline = f"Weekly Claw #{ep}"

    md = agenda.read_text(errors="ignore") if agenda.exists() else ""
    date = ""
    dm = re.search(r"\*\*Date:\*\*\s*([^\n]+)", md)
    if dm:
        date = re.sub(r"<[^>]+>", " ", dm.group(1)).replace("·", "·").strip()
        date = re.sub(r"\s+", " ", date)
    else:
        tm = re.search(rf"({MONTH_RE}\s+\d{{1,2}},\s+20\d{{2}})", title + "\n" + text, re.I)
        date = tm.group(1) if tm else "Latest episode"

    # Prefer episode thesis paragraph if present; otherwise first useful agenda paragraph.
    desc = ""
    thesis = re.search(r"##\s*Episode Thesis\s+(.+?)(?:\n##|\Z)", md, re.I | re.S)
    if thesis:
        desc = strip_tags(thesis.group(1).replace("**", ""))
    if not desc and md:
        for para in re.split(r"\n\s*\n", md):
            clean = re.sub(r"[#*_`>\-]+", " ", para).strip()
            if len(clean) > 80 and "Date:" not in clean:
                desc = strip_tags(clean)
                break
    if not desc:
        desc = "Latest Weekly Claw host deck, agenda, and show packet."
    if len(desc) > 170:
        desc = desc[:167].rsplit(" ", 1)[0] + "…"

    return {"headline": headline, "title": title, "date": date, "desc": desc}


def markdown_to_html(md: str) -> str:
    lines = md.splitlines()
    out: list[str] = []
    in_ul = False
    in_ol = False

    def close_lists() -> None:
        nonlocal in_ul, in_ol
        if in_ul:
            out.append("</ul>")
            in_ul = False
        if in_ol:
            out.append("</ol>")
            in_ol = False

    def inline(s: str) -> str:
        s = html.escape(s)
        s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
        s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
        return s

    for raw in lines:
        line = raw.rstrip()
        if not line.strip():
            close_lists()
            continue
        hm = re.match(r"^(#{1,3})\s+(.+)", line)
        if hm:
            close_lists()
            level = len(hm.group(1)) + 1
            out.append(f"<h{level}>{inline(hm.group(2))}</h{level}>")
            continue
        bm = re.match(r"^[-*]\s+(.+)", line)
        if bm:
            if not in_ul:
                close_lists(); out.append("<ul>"); in_ul = True
            out.append(f"<li>{inline(bm.group(1))}</li>")
            continue
        om = re.match(r"^\d+\.\s+(.+)", line)
        if om:
            if not in_ol:
                close_lists(); out.append("<ol>"); in_ol = True
            out.append(f"<li>{inline(om.group(1))}</li>")
            continue
        close_lists()
        out.append(f"<p>{inline(line)}</p>")
    close_lists()
    return "\n".join(out)


def write_agenda_html(repo: Path, ep: int, meta: dict[str, str]) -> None:
    md_path = repo / "episodes" / str(ep) / "agenda.md"
    if not md_path.exists():
        return
    body = markdown_to_html(md_path.read_text(errors="ignore"))
    out = repo / "episodes" / str(ep) / "agenda" / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Weekly Claw #{ep} Agenda — {html.escape(meta['headline'])}</title>
<style>
:root {{ color-scheme: light; --ink:#24201c; --paper:#fff9ee; --muted:#6e645a; --line:#b5a996; --accent:#2a7e6b; }}
body {{ margin:0; font:18px/1.55 system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif; color:var(--ink); background:#ece4d5; }}
a {{ color:var(--accent); }}
.shell {{ width:min(920px, calc(100% - 36px)); margin-inline:auto; }}
header, footer {{ padding:22px 0; }}
nav {{ display:flex; justify-content:space-between; gap:16px; align-items:center; }}
.wordmark {{ font-weight:800; text-transform:uppercase; text-decoration:none; color:var(--ink); }}
.button {{ display:inline-flex; align-items:center; min-height:40px; padding:0 14px; border:1px solid var(--accent); border-radius:6px; background:var(--accent); color:var(--paper); text-decoration:none; font-weight:700; }}
.button.secondary {{ color:var(--ink); background:transparent; border-color:var(--line); }}
.intro {{ padding:56px 0 32px; border-block:1px solid var(--line); }}
.eyebrow {{ margin:0 0 10px; color:var(--accent); font:700 12px/1 ui-monospace,Menlo,monospace; letter-spacing:.12em; text-transform:uppercase; }}
h1 {{ margin:0; font-size:clamp(42px,8vw,78px); line-height:.9; letter-spacing:-.05em; text-transform:uppercase; }}
article {{ padding:36px 0 70px; }}
h2,h3,h4 {{ line-height:1.05; margin-top:2em; }}
p,li {{ max-width:78ch; }}
code {{ background:rgba(36,32,28,.08); padding:.1em .3em; border-radius:4px; }}
</style>
</head>
<body>
<header><nav class="shell" aria-label="Episode navigation"><a class="wordmark" href="/">Weekly Claw</a><div><a class="button secondary" href="/episodes">Episodes</a> <a class="button" href="/episodes/{ep}/deck">Open slides</a></div></nav></header>
<main class="shell">
<section class="intro"><p class="eyebrow">Episode {ep} · {html.escape(meta['date'])}</p><h1>{html.escape(meta['headline'])}</h1><p>{html.escape(meta['desc'])}</p></section>
<article>{body}</article>
</main>
<footer class="shell">Weekly Claw #{ep} · Agenda and source notes · <a href="/episodes/{ep}/deck">View host deck</a></footer>
</body>
</html>
""")



def write_markdown_page(repo: Path, ep: int, source_name: str, route_name: str, title_suffix: str, meta: dict[str, str]) -> None:
    md_path = repo / "episodes" / str(ep) / source_name
    if not md_path.exists():
        return
    body = markdown_to_html(md_path.read_text(errors="ignore"))
    out = repo / "episodes" / str(ep) / route_name / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(f"""<!doctype html>
<html lang="en">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Weekly Claw #{ep} {html.escape(title_suffix)}</title><style>body{{margin:0;font:18px/1.55 system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;color:#24201c;background:#ece4d5}}a{{color:#2a7e6b}}.shell{{width:min(920px,calc(100% - 36px));margin-inline:auto}}header,footer{{padding:22px 0}}nav{{display:flex;justify-content:space-between;gap:16px;align-items:center}}.wordmark{{font-weight:800;text-transform:uppercase;text-decoration:none;color:#24201c}}.button{{display:inline-flex;align-items:center;min-height:40px;padding:0 14px;border:1px solid #2a7e6b;border-radius:6px;background:#2a7e6b;color:#fff9ee;text-decoration:none;font-weight:700}}.button.secondary{{color:#24201c;background:transparent;border-color:#b5a996}}.intro{{padding:56px 0 32px;border-block:1px solid #b5a996}}.eyebrow{{margin:0 0 10px;color:#2a7e6b;font:700 12px/1 ui-monospace,Menlo,monospace;letter-spacing:.12em;text-transform:uppercase}}h1{{margin:0;font-size:clamp(42px,8vw,78px);line-height:.9;letter-spacing:-.05em;text-transform:uppercase}}article{{padding:36px 0 70px}}h2,h3,h4{{line-height:1.05;margin-top:2em}}p,li{{max-width:78ch}}code{{background:rgba(36,32,28,.08);padding:.1em .3em;border-radius:4px}}</style></head>
<body><header><nav class="shell"><a class="wordmark" href="/">Weekly Claw</a><div><a class="button secondary" href="/episodes">Episodes</a> <a class="button" href="/episodes/{ep}/deck">Open slides</a></div></nav></header><main class="shell"><section class="intro"><p class="eyebrow">Episode {ep} · {html.escape(title_suffix)}</p><h1>{html.escape(meta['headline'])}</h1></section><article>{body}</article></main><footer class="shell">Weekly Claw #{ep} · {html.escape(title_suffix)}</footer></body></html>
""")

def update_homepage(repo: Path, latest: int, meta: dict[str, str]) -> None:
    path = repo / "index.html"
    text = path.read_text()
    # Only update explicit latest CTAs. Historical episode-card links must keep their own week.
    text = text.replace('href="/episodes?week=20&amp;deck=main">Watch the latest', f'href="/episodes?week={latest}&amp;deck=main">Watch the latest')
    text = text.replace('href="/episodes?week=20&amp;deck=main">Open episode', f'href="/episodes?week={latest}&amp;deck=main">Open episode')
    text = re.sub(r'<div class="latest-number" aria-hidden="true">\d+</div>', f'<div class="latest-number" aria-hidden="true">{latest}</div>', text)
    text = re.sub(r'<p class="latest-label">Featured latest episode · .*?</p>', f'<p class="latest-label">Featured latest episode · {html.escape(meta["date"])}</p>', text)
    text = re.sub(r'<h2 id="latest-title">.*?</h2>', f'<h2 id="latest-title">{html.escape(meta["headline"])}</h2>', text)
    text = re.sub(r'<p class="latest-meta">.*?</p>', f'<p class="latest-meta">{html.escape(meta["desc"])}</p>', text)

    card = f'''          <article class="episode-card">
            <div class="episode-thumb"><img src="assets/episode-art-v2/signal-studio.jpg" alt="Editorial illustration of a cobalt broadcast studio connecting unusual software objects"><span class="episode-week">W{latest}</span></div>
            <div class="episode-copy">
              <p class="packet-label">Main slides + agenda</p>
              <h3>{html.escape(meta['headline'])}</h3>
              <p>{html.escape(meta['desc'])}</p>
            </div>
            <div class="episode-actions">
              <a class="button small" href="/episodes?week={latest}&amp;deck=main">Main slides</a>
              <a class="button small secondary" href="/episodes/{latest}/agenda">Agenda</a>
            </div>
          </article>'''
    if f'<span class="episode-week">W{latest}</span>' not in text:
        text = text.replace('        <div class="archive-grid">\n', '        <div class="archive-grid">\n' + card + '\n')
    path.write_text(text)


def update_episodes_index(repo: Path, latest: int, meta: dict[str, str]) -> None:
    path = repo / "episodes" / "index.html"
    text = path.read_text()
    count = len([p for p in (repo / "episodes").iterdir() if p.is_dir() and p.name.isdigit() and (p / "deck.html").exists() or (p.is_dir() and p.name.isdigit() and (repo / f"w{p.name}" / "changelog" / "index.html").exists())])
    text = re.sub(r'<div class="fact"><strong>\d+</strong><span>archived episodes</span></div>', f'<div class="fact"><strong>{count:02d}</strong><span>archived episodes</span></div>', text)

    card = f'''          <article class="week-card" data-kind="main">
            <div class="thumb"><img src="/assets/episode-art-v2/signal-studio.jpg" alt="Cobalt broadcast studio connecting unusual software objects"><span class="week-number">W{latest}</span><span class="availability">Slides + agenda</span></div>
            <div class="card-copy"><p class="card-kicker">Main slides · full agenda</p><h3>{html.escape(meta['headline'])}</h3><p>{html.escape(meta['desc'])}</p></div>
            <div class="card-actions"><button class="deck-button" type="button" data-week="{latest}" data-deck="main" data-title="W{latest} · Main show slides" data-url="/episodes/{latest}/deck">Main slides</button><a class="source-link secondary" href="/episodes/{latest}/agenda">Agenda</a><a class="source-link secondary" href="/episodes/{latest}/host-cheat-sheet">Host sheet</a></div>
          </article>'''
    if f'<span class="week-number">W{latest}</span>' not in text:
        text = text.replace('        <div class="gallery" id="gallery">\n', '        <div class="gallery" id="gallery">\n' + card + '\n')
    text = text.replace('W20 includes its original host slides and agenda;', f'W{latest} includes its original host slides and agenda;')
    path.write_text(text)


def update_validate(repo: Path, latest: int) -> None:
    path = repo / "scripts" / "validate.mjs"
    text = path.read_text()
    insert = f"  'episodes/{latest}/agenda.md',\n  'episodes/{latest}/agenda/index.html',\n  'episodes/{latest}/deck.html',"
    if f"episodes/{latest}/deck.html" not in text:
        text = text.replace("  'episodes/20/deck.html',", "  'episodes/20/deck.html',\n" + insert)
    text = text.replace("'/episodes/20/deck'", f"'/episodes/{latest}/deck'")
    text = text.replace("'/episodes/20/agenda'", f"'/episodes/{latest}/agenda'")
    text = text.replace("'W20'", f"'W{latest}'")
    text = text.replace("'<strong>11</strong>'", "'<strong>12</strong>'")
    text = text.replace("'/episodes?week=20&amp;deck=main'", f"'/episodes?week={latest}&amp;deck=main'")
    text = text.replace("const week19HostDeck = readFileSync(new URL('../episodes/19/host.html', import.meta.url), 'utf8');\nif (!week19HostDeck.includes('Host cue') || !week19HostDeck.includes('Weekly Claw #19')) {\n  console.error('Week 19 host deck is missing expected host cue/content markers');\n  process.exit(1);\n}\n", "")
    # Include latest deck in basic deck sanity loop.
    text = text.replace("for (const week of [10, 12, 13, 14, 15, 19, 20])", f"for (const week of [10, 12, 13, 14, 15, 19, 20, {latest}])")
    path.write_text(text)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--archive", default="/home/henrymascot/weeklyclaw")
    ap.add_argument("--repo", default=str(repo_root_from_script()))
    ap.add_argument("--commit", action="store_true")
    ap.add_argument("--push", action="store_true")
    args = ap.parse_args()

    archive = Path(args.archive)
    repo = Path(args.repo)
    if not (archive / "episodes").exists():
        raise SystemExit(f"Archive missing episodes directory: {archive / 'episodes'}")

    # Copy archive episodes into repo.
    for src_ep in sorted((archive / "episodes").iterdir(), key=lambda p: int(p.name) if p.name.isdigit() else 9999):
        if src_ep.is_dir() and src_ep.name.isdigit():
            copy_tree_merge(src_ep, repo / "episodes" / src_ep.name)

    episode_nums = sorted([int(p.name) for p in (repo / "episodes").iterdir() if p.is_dir() and p.name.isdigit() and (p / "deck.html").exists()])
    if not episode_nums:
        raise SystemExit("No episode decks found")
    latest = max(episode_nums)
    meta = deck_meta(repo, latest)
    write_agenda_html(repo, latest, meta)
    write_markdown_page(repo, latest, "host-cheat-sheet.md", "host-cheat-sheet", "Host Cheat Sheet", meta)
    update_homepage(repo, latest, meta)
    update_episodes_index(repo, latest, meta)
    update_validate(repo, latest)

    print(f"SYNC_OK latest={latest} headline={meta['headline']!r}")
    if args.commit or args.push:
        subprocess.run(["npm", "run", "build"], cwd=repo, check=True)
        subprocess.run(["git", "add", "index.html", "episodes/index.html", f"episodes/{latest}", "scripts/validate.mjs", "scripts/sync-weeklyclaw-archive.py", "README.md"], cwd=repo, check=True)
        diff = subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=repo)
        if diff.returncode == 0:
            print("GIT_NO_CHANGES")
        else:
            subprocess.run(["git", "commit", "-m", f"chore: sync Weekly Claw episode {latest}"], cwd=repo, check=True)
            print("GIT_COMMITTED")
            if args.push:
                subprocess.run(["git", "push", "origin", "HEAD:main"], cwd=repo, check=True)
                print("GIT_PUSHED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
