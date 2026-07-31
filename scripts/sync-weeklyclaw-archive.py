#!/usr/bin/env python3
"""Sync local WeeklyClaw archive folders into the static website repo.

Default source: /home/henrymascot/weeklyclaw
Default destination: current repo root

This intentionally does not delete repo files. It only copies/updates episode files,
refreshes the homepage/episode archive, and connects published YouTube videos.
"""
from __future__ import annotations

import argparse
import html
import json
import os
import re
import shutil
import subprocess
from pathlib import Path

MONTH_RE = r"(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:t(?:ember)?)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)"
YOUTUBE_THUMBNAIL_OVERRIDES = {
    20: "w20-v2-ai-got-cheap-approved-20260727.jpg",
    21: "w21-v2-approved-20260727.jpg",
    22: "w22-v2-the-sandbox-failed-approved-20260727.jpg",
}


def repo_root_from_script() -> Path:
    return Path(__file__).resolve().parents[1]


def fetch_youtube_episodes() -> dict[int, dict[str, str]]:
    """Return public Weekly Claw videos keyed by episode number.

    Sync remains usable offline: a missing yt-dlp binary or network failure simply
    leaves existing card media unchanged.
    """
    try:
        result = subprocess.run(
            [
                "yt-dlp",
                "--flat-playlist",
                "--playlist-end",
                "50",
                "--dump-single-json",
                "https://www.youtube.com/@weeklyclaw/videos",
            ],
            check=True,
            capture_output=True,
            text=True,
            timeout=90,
        )
        playlist = json.loads(result.stdout)
    except (FileNotFoundError, json.JSONDecodeError, subprocess.SubprocessError):
        return {}

    episodes: dict[int, dict[str, str]] = {}
    for entry in playlist.get("entries") or []:
        video_id = entry.get("id")
        title = entry.get("title") or ""
        match = re.search(r"Weekly Claw\s*#(\d+)\b", title, re.I)
        if not video_id or not match:
            continue
        episode = int(match.group(1))
        episodes[episode] = {
            "id": video_id,
            "url": f"https://www.youtube.com/watch?v={video_id}",
            "thumbnail": f"https://i.ytimg.com/vi/{video_id}/maxresdefault.jpg",
        }
    return episodes


def download_youtube_thumbnails(repo: Path, videos: dict[int, dict[str, str]]) -> None:
    asset_dir = repo / "assets" / "youtube-thumbnails"
    asset_dir.mkdir(parents=True, exist_ok=True)
    for episode, video in videos.items():
        if episode in YOUTUBE_THUMBNAIL_OVERRIDES:
            continue
        destination = asset_dir / f"w{episode}.jpg"
        try:
            subprocess.run(
                ["curl", "-L", "--fail", "--silent", "--show-error", video["thumbnail"], "-o", str(destination)],
                check=True,
                timeout=45,
            )
        except (FileNotFoundError, subprocess.SubprocessError):
            destination.unlink(missing_ok=True)


def refresh_youtube_cards(text: str, videos: dict[int, dict[str, str]], *, archive: bool) -> str:
    """Convert cards for published videos to Video + Slides without touching other cards."""
    card_class = "week-card" if archive else "episode-card"
    week_class = "week-number" if archive else "episode-week"

    for episode, video in videos.items():
        thumbnail_filename = YOUTUBE_THUMBNAIL_OVERRIDES.get(episode, f"w{episode}.jpg")
        pattern = re.compile(
            rf'(<article class="{card_class}"[^>]*>(?:(?!</article>)[\s\S])*?'
            rf'<span class="{week_class}">W{episode}</span>(?:(?!</article>)[\s\S])*?</article>)'
        )
        match = pattern.search(text)
        if not match:
            continue
        block = match.group(1)
        local_thumbnail = f"/assets/youtube-thumbnails/{thumbnail_filename}"
        if archive:
            def add_player_data(article_match: re.Match[str]) -> str:
                opening = re.sub(r'\sdata-(?:week|video-id)="[^"]*"', "", article_match.group(0))
                return f'{opening[:-1]} data-week="{episode}" data-video-id="{video["id"]}">'

            block = re.sub(r'<article class="week-card"[^>]*>', add_player_data, block, count=1)
            media = (
                f'<a class="thumb youtube-thumb" href="{video["url"]}" data-play-video="{episode}" '
                f'aria-label="Play Weekly Claw episode {episode} on this page">'
                f'<img src="{local_thumbnail}" alt="YouTube thumbnail for Weekly Claw episode {episode}">'
                f'<span class="week-number">W{episode}</span><span class="availability">Video + slides</span></a>'
            )
            block = re.sub(r'<(?:div|a) class="thumb(?: youtube-thumb)?"[^>]*>[\s\S]*?</(?:div|a)>', media, block, count=1)
            block = re.sub(r'<p class="card-kicker">.*?</p>', '<p class="card-kicker">Video · main slides</p>', block, count=1)
            actions = (
                f'<div class="card-actions"><a class="source-link" href="{video["url"]}" data-play-video="{episode}" '
                f'aria-label="Play Weekly Claw episode {episode} video on this page">Video</a>'
                f'<button class="deck-button secondary" type="button" data-week="{episode}" data-deck="main" '
                f'data-title="W{episode} · Main show slides" data-url="/episodes/{episode}/deck">Slides</button></div>'
            )
            block = re.sub(r'<div class="card-actions">[\s\S]*?</div>', actions, block, count=1)
        else:
            media = (
                f'<a class="episode-thumb youtube-thumb" href="{video["url"]}" target="_blank" rel="noopener" '
                f'aria-label="Watch Weekly Claw episode {episode} on YouTube">'
                f'<img src="assets/youtube-thumbnails/{thumbnail_filename}" alt="YouTube thumbnail for Weekly Claw episode {episode}">'
                f'<span class="episode-week">W{episode}</span></a>'
            )
            block = re.sub(r'<div class="episode-thumb">[\s\S]*?</div>', media, block, count=1)
            block = re.sub(r'<p class="packet-label">.*?</p>', '<p class="packet-label">Video + slides</p>', block, count=1)
            actions = (
                f'<div class="episode-actions">\n'
                f'              <a class="button small" href="{video["url"]}" target="_blank" rel="noopener">Video</a>\n'
                f'              <a class="button small secondary" href="/episodes?week={episode}&amp;deck=main">Slides</a>\n'
                f'            </div>'
            )
            block = re.sub(r'<div class="episode-actions">[\s\S]*?</div>', actions, block, count=1)
        text = text[:match.start()] + block + text[match.end():]
    return text


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
    return html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s))).strip()


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
    if re.sub(r"[^a-z0-9]+", " ", headline.lower()).strip() in {"weekly claw", f"weekly claw {ep}"}:
        story_frame = re.search(r"<h2[^>]*>(.*?)</h2>", text, re.I | re.S)
        if story_frame:
            headline = strip_tags(story_frame.group(1))
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
    if not desc:
        cold_open = re.search(r"##\s*Cold Open[^\n]*\n+([^\n]+)", md, re.I)
        if cold_open:
            desc = strip_tags(re.sub(r"[#*_`>]+", " ", cold_open.group(1)))
    if not desc and md:
        for para in re.split(r"\n\s*\n", md):
            clean = re.sub(r"[#*_`>\-]+", " ", para).strip()
            if len(clean) > 80 and "Date:" not in clean:
                desc = strip_tags(clean)
                break
    if not desc:
        desc = "Latest Weekly Claw video and main show slides."
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

def update_homepage(repo: Path, latest: int, meta: dict[str, str], videos: dict[int, dict[str, str]]) -> None:
    path = repo / "index.html"
    text = path.read_text()
    existing_week_match = re.search(r'<div class="latest-number" aria-hidden="true">(\d+)</div>', text)
    existing_week = int(existing_week_match.group(1)) if existing_week_match else None
    # Only update explicit latest CTAs. Historical episode-card links must keep their own week.
    text = re.sub(r'href="/episodes\?week=\d+&amp;deck=main">Watch the latest', f'href="/episodes?week={latest}&amp;deck=main">Watch the latest', text)
    text = re.sub(r'\s*<div class="latest-action">.*?</div>', "", text, count=1)
    text = re.sub(r'<div class="latest-number" aria-hidden="true">\d+</div>', f'<div class="latest-number" aria-hidden="true">{latest}</div>', text)
    text = re.sub(r'<p class="latest-label">Featured latest episode · .*?</p>', f'<p class="latest-label">Featured latest episode · {html.escape(meta["date"])}</p>', text)
    text = re.sub(r'<h2 id="latest-title">.*?</h2>', f'<h2 id="latest-title">{html.escape(meta["headline"])}</h2>', text)
    text = re.sub(r'<p class="latest-meta">.*?</p>', f'<p class="latest-meta">{html.escape(meta["desc"])}</p>', text)

    def update_featured_media(card_match: re.Match[str]) -> str:
        opening = card_match.group(0)
        existing_video = re.search(r'\sdata-video-id="[^"]+"', opening)
        existing_audio = re.search(r'\sdata-audio-src="[^"]+"', opening)
        opening = re.sub(r'\sdata-(?:video-id|audio-src)="[^"]*"', "", opening)
        video_attribute = (
            f' data-video-id="{videos[latest]["id"]}"'
            if latest in videos
            else existing_video.group(0) if existing_week == latest and existing_video else ""
        )
        audio_attribute = existing_audio.group(0) if existing_week == latest and existing_audio else ""
        return f"{opening[:-1]}{video_attribute}{audio_attribute}>"

    text = re.sub(r'<div class="latest-card"[^>]*>', update_featured_media, text, count=1)

    card = f'''          <article class="episode-card">
            <div class="episode-thumb"><img src="assets/episode-art-v2/signal-studio.jpg" alt="Editorial illustration of a cobalt broadcast studio connecting unusual software objects"><span class="episode-week">W{latest}</span></div>
            <div class="episode-copy">
              <p class="packet-label">Main slides</p>
              <h3>{html.escape(meta['headline'])}</h3>
              <p>{html.escape(meta['desc'])}</p>
            </div>
            <div class="episode-actions">
              <a class="button small" href="/episodes?week={latest}&amp;deck=main">Slides</a>
            </div>
          </article>'''
    existing_card = re.compile(rf'          <article class="episode-card">(?:(?!          </article>).)*?<span class="episode-week">W{latest}</span>(?:(?!          </article>).)*?          </article>', re.S)
    if existing_card.search(text):
        text = existing_card.sub(card, text, count=1)
    else:
        text = text.replace('        <div class="archive-grid">\n', '        <div class="archive-grid">\n' + card + '\n')
    text = refresh_youtube_cards(text, videos, archive=False)
    path.write_text(text)


def update_episodes_index(repo: Path, latest: int, meta: dict[str, str], videos: dict[int, dict[str, str]]) -> None:
    path = repo / "episodes" / "index.html"
    text = path.read_text()
    count = len([p for p in (repo / "episodes").iterdir() if p.is_dir() and p.name.isdigit() and (p / "deck.html").exists() or (p.is_dir() and p.name.isdigit() and (repo / f"w{p.name}" / "changelog" / "index.html").exists())])
    text = re.sub(r'<div class="fact"><strong>\d+</strong><span>archived episodes</span></div>', f'<div class="fact"><strong>{count:02d}</strong><span>archived episodes</span></div>', text)

    card = f'''          <article class="week-card" data-kind="main">
            <div class="thumb"><img src="/assets/episode-art-v2/signal-studio.jpg" alt="Cobalt broadcast studio connecting unusual software objects"><span class="week-number">W{latest}</span><span class="availability">Main slides</span></div>
            <div class="card-copy"><p class="card-kicker">Main slides</p><h3>{html.escape(meta['headline'])}</h3><p>{html.escape(meta['desc'])}</p></div>
            <div class="card-actions"><button class="deck-button" type="button" data-week="{latest}" data-deck="main" data-title="W{latest} · Main show slides" data-url="/episodes/{latest}/deck">Slides</button></div>
          </article>'''
    existing_card = re.compile(rf'          <article class="week-card"[^>]*>(?:(?!          </article>).)*?<span class="week-number">W{latest}</span>(?:(?!          </article>).)*?          </article>', re.S)
    existing_match = existing_card.search(text)
    if existing_match:
        existing_block = existing_match.group(0)
        existing_audio = re.search(r'\sdata-audio-src="[^"]+"', existing_block)
        if existing_audio:
            card = card.replace('data-kind="main"', f'data-kind="main"{existing_audio.group(0)}', 1)
        if latest not in videos and 'data-video-id=' in existing_block:
            card = re.sub(
                r'(<div class="card-copy"><p class="card-kicker">.*?</p>)<h3>.*?</h3><p>.*?</p>(</div>)',
                lambda match: (
                    f'{match.group(1)}<h3>{html.escape(meta["headline"])}</h3>'
                    f'<p>{html.escape(meta["desc"])}</p>{match.group(2)}'
                ),
                existing_block,
                count=1,
            )
        text = existing_card.sub(lambda _: card, text, count=1)
    else:
        text = text.replace('        <div class="gallery" id="gallery">\n', '        <div class="gallery" id="gallery">\n' + card + '\n')
    text = re.sub(r'W\d+ includes its original host slides and agenda;', f'W{latest} includes its original host slides;', text)
    text = refresh_youtube_cards(text, videos, archive=True)
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
    count = len([p for p in (repo / "episodes").iterdir() if p.is_dir() and p.name.isdigit() and ((p / "deck.html").exists() or (repo / f"w{p.name}" / "changelog" / "index.html").exists())])
    text = re.sub(r"(for \(const needle of \['Weekly Claw Episodes', )'W\d+'", rf"\1'W{latest}'", text)
    text = re.sub(rf"('W{latest}', )'/episodes/\d+/deck'", rf"\1'/episodes/{latest}/deck'", text)
    text = re.sub(r"'<strong>\d+</strong>', 'archived episodes'", f"'<strong>{count:02d}</strong>', 'archived episodes'", text)
    text = text.replace("'/episodes?week=20&amp;deck=main'", f"'/episodes?week={latest}&amp;deck=main'")
    text = text.replace("const week19HostDeck = readFileSync(new URL('../episodes/19/host.html', import.meta.url), 'utf8');\nif (!week19HostDeck.includes('Host cue') || !week19HostDeck.includes('Weekly Claw #19')) {\n  console.error('Week 19 host deck is missing expected host cue/content markers');\n  process.exit(1);\n}\n", "")
    # Include latest deck in basic deck sanity loop.
    def include_latest(match: re.Match[str]) -> str:
        weeks = [int(value) for value in re.findall(r"\d+", match.group(1))]
        if latest not in weeks:
            weeks.append(latest)
        return "for (const week of [" + ", ".join(map(str, weeks)) + "])"
    text = re.sub(r"for \(const week of \[([0-9, ]+)\]\)", include_latest, text, count=1)
    path.write_text(text)


def public_episode_paths(repo: Path, latest: int) -> list[Path]:
    episode = repo / "episodes" / str(latest)
    candidates = [
        episode / "deck.html",
        episode / "agenda.md",
        episode / "agenda" / "index.html",
        episode / "source-assets",
        episode / "assets",
        episode / "media-manifest.json",
        episode / "host-cheat-sheet",
    ]
    return [path for path in candidates if path.exists()]


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
    videos = fetch_youtube_episodes()
    download_youtube_thumbnails(repo, videos)
    write_agenda_html(repo, latest, meta)
    write_markdown_page(repo, latest, "host-cheat-sheet.md", "host-cheat-sheet", "Host Cheat Sheet", meta)
    update_homepage(repo, latest, meta, videos)
    update_episodes_index(repo, latest, meta, videos)
    update_validate(repo, latest)

    print(f"SYNC_OK latest={latest} headline={meta['headline']!r}")
    if args.commit or args.push:
        subprocess.run(["npm", "run", "build"], cwd=repo, check=True)
        public_paths = [str(path.relative_to(repo)) for path in public_episode_paths(repo, latest)]
        subprocess.run(["git", "add", "index.html", "episodes/index.html", "assets/youtube-thumbnails", *public_paths, "scripts/validate.mjs", "scripts/sync-weeklyclaw-archive.py", "README.md"], cwd=repo, check=True)
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
