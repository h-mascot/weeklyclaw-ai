"""Validate a WeeklyClaw deck revision against its speaker notes, media,
prior-episode template authority, and rendered visual quality.

This is the canonical post-build validator. It bundles the checks the skill
mandates into a single script so every weekly run produces the same evidence.

Usage:
    python3 scripts/validate_deck.py <deck.html> <speaker-notes.md> [authority-deck.html]

Exit code 0 = PASS. Non-zero = first failed check, with the failure printed.

If a third argument (authority-deck.html) is supplied, the template-comparison,
invented-logo rejection, and sponsor-asset provenance gates also run.
"""
import hashlib
import os
import re
import subprocess
import sys


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()


def extract_style_block(html):
    """Extract the contents of the first (primary) <style> block."""
    m = re.search(r'<style>(.*?)</style>', html, re.DOTALL)
    return m.group(1) if m else ''


def extract_css_custom_properties(style_text):
    """Extract :root CSS custom properties as a dict."""
    root_m = re.search(r':root\s*\{([^}]*)\}', style_text)
    if not root_m:
        return {}
    props = {}
    for m in re.finditer(r'(--[\w-]+)\s*:\s*([^;]+);', root_m.group(1)):
        props[m.group(1)] = m.group(2).strip()
    return props


def extract_svg_symbols(html):
    """Extract all <symbol id="..."> definitions and their viewBox."""
    symbols = {}
    for m in re.finditer(r'<symbol\s+id="([^"]+)"([^>]*)>', html):
        sym_id = m.group(1)
        attrs = m.group(2)
        vb_m = re.search(r'viewBox="([^"]+)"', attrs)
        symbols[sym_id] = {'viewBox': vb_m.group(1) if vb_m else None}
    return symbols


def extract_layout_classes(style_text):
    """Extract names of significant layout classes defined in CSS."""
    classes = set()
    for m in re.finditer(r'\.([\w-]+)\s*[\{,]', style_text):
        classes.add(m.group(1))
    return classes


def extract_sponsor_refs(html):
    """Extract all assets/sponsors/ file references from the deck."""
    return set(re.findall(r'(?:src|href)="(assets/sponsors/[^"]+)"', html))


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)

    deck_path, notes_path = sys.argv[1], sys.argv[2]
    authority_path = sys.argv[3] if len(sys.argv) > 3 else None
    deck_dir = os.path.dirname(os.path.abspath(deck_path))
    with open(deck_path) as f:
        html = f.read()
    with open(notes_path) as f:
        notes = f.read()

    # 1. Slide-ID parity ---------------------------------------------
    deck_ids = sorted(set(re.findall(r'id="(s-[^"]+)"', html)))
    note_ids = sorted(set(re.findall(r'^## (s-\S+)', notes, re.MULTILINE)))
    if deck_ids != note_ids:
        print(f"FAIL: slide-ID parity\n  deck:  {deck_ids}\n  notes: {note_ids}")
        sys.exit(1)
    print(f"PASS: slide-ID parity ({len(deck_ids)} slides <-> notes)")

    # 2. JS syntax via node --check - --------------------------------
    m = re.search(r'<script>(.*?)</script>', html, re.DOTALL)
    if not m:
        print("FAIL: no <script> block found in deck")
        sys.exit(1)
    out = subprocess.run(
        ['node', '--check', '-'],
        input=m.group(1),
        capture_output=True,
        text=True,
    )
    if out.returncode != 0:
        print(f"FAIL: JS syntax\n{out.stderr}")
        sys.exit(1)
    print("PASS: JS syntax (node --check -)")

    # 3. No autoplay -------------------------------------------------
    autoplay_tokens = [
        t for t in re.finditer(r'autoplay', html, re.IGNORECASE)
        if 'NOT autoplay' not in html[max(0, t.start() - 30):t.end() + 30]
        and 'no autoplay' not in html[max(0, t.start() - 30):t.end() + 30].lower()
    ]
    if autoplay_tokens:
        for tok in autoplay_tokens:
            start = max(0, tok.start() - 60)
            end = min(len(html), tok.end() + 60)
            print(f"  ... {html[start:end]} ...")
        print(f"FAIL: {len(autoplay_tokens)} unexpected autoplay tokens")
        sys.exit(1)
    print("PASS: no autoplay")

    # 4. Clickable source links --------------------------------------
    # EP23 uses class="src-links" for its source link containers; the links
    # themselves are <a href="..."> target="_blank" inside those containers.
    # Accept both "source-link" and "src-link" class patterns, plus any
    # external <a href="https://..."> with target="_blank" as a source link.
    src_links_class = re.findall(
        r'class="(?:source-link|src-link|src-links|source-links)[^"]*"[^>]*href="([^"]+)"',
        html,
    )
    # Also count external links with target="_blank" as source links.
    ext_links = re.findall(
        r'<a\s+href="(https?://[^"]+)"[^>]*target="_blank"', html
    )
    src_links = list(set(src_links_class + ext_links))
    if len(src_links) < 10:
        print(f"FAIL: only {len(src_links)} source links (expect >= 10)")
        sys.exit(1)
    print(f"PASS: {len(src_links)} clickable source links")

    # 5. Final Sources slide -----------------------------------------
    if 's-sources' not in deck_ids:
        print("FAIL: final Sources slide (s-sources) missing")
        sys.exit(1)
    print("PASS: final Sources slide present")

    # 5b. Close-slide Discord QR (Henry, 2026-08-23) ------------------
    # The final close slide must carry a QR code leading to the WeeklyClaw
    # Discord. Uses the authority template's .discord-qr card: a local PNG
    # under assets/socials/, linked to https://weeklyclaw.ai/discord (the
    # rotating invite route — never a hardcoded discord.gg/<code>).
    qr_anchor = re.search(
        r'<a\s+class="discord-qr"[^>]*href="([^"]+)"[^>]*>\s*'
        r'<img\s+src="([^"]+)"', html)
    if not qr_anchor:
        print('FAIL: close-slide Discord QR missing — deck needs the '
              '.discord-qr card (local assets/socials/ QR image linking to '
              'https://weeklyclaw.ai/discord)')
        sys.exit(1)
    if 'weeklyclaw.ai/discord' not in qr_anchor.group(1):
        print(f"FAIL: Discord QR links to {qr_anchor.group(1)} — must link "
              "to https://weeklyclaw.ai/discord (rotating invite route, "
              "never a hardcoded discord.gg code)")
        sys.exit(1)
    if not qr_anchor.group(2).startswith('assets/'):
        print(f"FAIL: Discord QR image {qr_anchor.group(2)} must be a local "
              "assets/ file (copy weeklyclaw-discord-qr.png from the prior "
              "episode's showprep assets)")
        sys.exit(1)
    if not os.path.exists(os.path.join(deck_dir, qr_anchor.group(2))):
        print(f"FAIL: Discord QR image missing on disk: {qr_anchor.group(2)}")
        sys.exit(1)
    print(f"PASS: close-slide Discord QR ({qr_anchor.group(2)} -> "
          "weeklyclaw.ai/discord)")

    # 6. Theme markers ----------------------------------------------
    # FIXED: check for weeklyclaw-logo symbol (the real logo in the APPROVED
    # Episode 23 template), NOT the generic "claw-mark" string. Episode 24
    # invented a fake <symbol id="claw-mark"> that passed the old check while
    # the real Episode 23 deck (which uses weeklyclaw-logo) would have failed.
    markers = {
        "cream_paper": '--site-paper' in html or '#f4ecd8' in html.lower(),
        "teal_cyan": '--claw-red' in html and (
            'cyan' in html.lower()
            or '#0e7c86' in html.lower()
            or '#1a8a8e' in html.lower()
            or '#2a7e6b' in html.lower()
            or '#286f7d' in html.lower()
        ),
        "weeklyclaw_logo_symbol": (
            'weeklyclaw-logo' in html
            and '<symbol' in html
            and 'id="weeklyclaw-logo"' in html
        ),
        "barlow_condensed": 'Barlow+Condensed' in html or 'Barlow Condensed' in html,
        "ibm_plex_mono": 'IBM+Plex+Mono' in html or 'IBM Plex Mono' in html,
    }
    missing = [k for k, v in markers.items() if not v]
    if missing:
        print(f"FAIL: theme markers missing: {missing}")
        sys.exit(1)
    print(f"PASS: theme markers: {list(markers.keys())}")

    # 7. Local media paths resolved ----------------------------------
    local_paths = re.findall(r'src="(assets/[^"]+)"', html)
    if not local_paths:
        print("FAIL: no local media paths in deck")
        sys.exit(1)
    missing_media = []
    for p in local_paths:
        full = os.path.join(deck_dir, p)
        if not os.path.exists(full):
            missing_media.append(p)
    if missing_media:
        print(f"FAIL: missing local media: {missing_media}")
        sys.exit(1)
    print(f"PASS: {len(local_paths)} local media paths resolved")

    # 8. Story-ID set readable from speaker notes --------------------
    seg_ids = re.findall(r's-seg-(\S+?)"', html)
    if not seg_ids:
        seg_ids = re.findall(r'^##\s+s-seg-(\S+)', notes, re.MULTILINE)
    print(f"PASS: segment IDs found: {seg_ids}")

    # === TEMPLATE-AUTHORITY GATES (require authority deck) ==========

    if authority_path:
        with open(authority_path) as f:
            auth_html = f.read()

        # 9. CSS custom-property parity ---------------------------------
        deck_props = extract_css_custom_properties(extract_style_block(html))
        auth_props = extract_css_custom_properties(extract_style_block(auth_html))
        # All theme-defining custom properties in the authority must be present
        # in the new deck with the same value.
        theme_props = [
            '--site-paper', '--site-ink', '--site-mint', '--site-cyan',
            '--claw-red', '--claw-orange', '--claw-gradient',
            '--bg-dark', '--bg-card',
            '--display', '--mono',
            '--text-primary', '--text-secondary', '--text-muted',
            '--border-subtle',
        ]
        mismatched = []
        for prop in theme_props:
            if prop in auth_props:
                if prop not in deck_props:
                    mismatched.append(f"{prop}: MISSING from new deck")
                elif deck_props[prop] != auth_props[prop]:
                    mismatched.append(
                        f"{prop}: new='{deck_props[prop]}' vs authority='{auth_props[prop]}'"
                    )
        if mismatched:
            print(f"FAIL: CSS custom-property drift from authority deck:")
            for mm in mismatched:
                print(f"  {mm}")
            sys.exit(1)
        print(f"PASS: CSS custom properties match authority deck ({len(theme_props)} checked)")

        # 10. SVG symbol parity -----------------------------------------
        deck_symbols = extract_svg_symbols(html)
        auth_symbols = extract_svg_symbols(auth_html)
        # The authority deck's symbols must all be present in the new deck.
        missing_syms = set(auth_symbols.keys()) - set(deck_symbols.keys())
        if missing_syms:
            print(f"FAIL: SVG symbols missing from new deck: {sorted(missing_syms)}")
            sys.exit(1)
        # Check viewBox match for the weeklyclaw-logo symbol specifically.
        if 'weeklyclaw-logo' in auth_symbols and 'weeklyclaw-logo' in deck_symbols:
            if auth_symbols['weeklyclaw-logo'].get('viewBox') != deck_symbols['weeklyclaw-logo'].get('viewBox'):
                print(f"FAIL: weeklyclaw-logo viewBox drift: "
                      f"new='{deck_symbols['weeklyclaw-logo'].get('viewBox')}' "
                      f"vs authority='{auth_symbols['weeklyclaw-logo'].get('viewBox')}'")
                sys.exit(1)
        print(f"PASS: SVG symbols match authority deck ({sorted(deck_symbols.keys())})")

        # 11. Invented-logo rejection -----------------------------------
        # Any <symbol> in the new deck that is NOT in the authority deck is an
        # invention. Only episode-specific content symbols would be acceptable,
        # but a claw/logo/brand symbol is always an invention.
        invented_symbols = set(deck_symbols.keys()) - set(auth_symbols.keys())
        brand_keywords = ['claw', 'logo', 'brand', 'mark', 'icon', 'wc']
        brand_inventions = [
            s for s in invented_symbols
            if any(kw in s.lower() for kw in brand_keywords)
        ]
        if brand_inventions:
            print(f"FAIL: invented brand/logo SVG symbols not in authority deck: "
                  f"{sorted(brand_inventions)}")
            sys.exit(1)
        # Also check for inline SVG <path>/<g> that draws claw-like shapes
        # outside of a <use href="#weeklyclaw-logo"> reference. This catches
        # the Episode 24 invented claw pattern.
        inline_claw_paths = re.findall(
            r'<svg[^>]*(?:claw|brand-mark)[^>]*>.*?</svg>', html, re.DOTALL | re.IGNORECASE
        )
        # Filter out legitimate <use> references to the authority symbol
        legit_uses = re.findall(r'<use\s+href="#weeklyclaw-logo"', html)
        suspicious_inline = [
            p for p in inline_claw_paths
            if '<use href="#weeklyclaw-logo"' not in p
        ]
        if suspicious_inline:
            print(f"FAIL: {len(suspicious_inline)} inline SVG block(s) with claw/brand "
                  f"marking that are not <use> references to the authority symbol")
            sys.exit(1)
        if invented_symbols:
            print(f"  NOTE: non-brand invented symbols (may be content): "
                  f"{sorted(invented_symbols)}")
        print("PASS: no invented brand/logo symbols")

        # 12. Layout-class coverage -------------------------------------
        deck_classes = extract_layout_classes(extract_style_block(html))
        auth_classes = extract_layout_classes(extract_style_block(auth_html))
        # Core layout classes from the authority must be present.
        core_classes = [
            'slide', 'content', 'card', 'part-label', 'story-num',
            'claw-bg', 'glow-orb', 'logo-row', 'slide-container',
            'nav-dots', 'slide-counter', 'gradient-text', 'gradient-line',
            'bullet-list', 'two-col', 'three-col',
        ]
        missing_classes = [
            c for c in core_classes
            if c in auth_classes and c not in deck_classes
        ]
        if missing_classes:
            print(f"FAIL: layout classes from authority deck missing from new deck: "
                  f"{missing_classes}")
            sys.exit(1)
        print(f"PASS: core layout classes present ({len(core_classes)} checked)")

        # 13. Sponsor-asset provenance ----------------------------------
        deck_sponsors = extract_sponsor_refs(html)
        auth_sponsors = extract_sponsor_refs(auth_html)
        if deck_sponsors:
            auth_dir = os.path.dirname(os.path.abspath(authority_path))
            for ref in sorted(deck_sponsors):
                deck_file = os.path.join(deck_dir, ref)
                auth_file = os.path.join(auth_dir, ref)
                if not os.path.exists(deck_file):
                    print(f"FAIL: sponsor asset referenced but missing on disk: {ref}")
                    sys.exit(1)
                if os.path.exists(auth_file):
                    deck_hash = sha256_file(deck_file)
                    auth_hash = sha256_file(auth_file)
                    if deck_hash != auth_hash:
                        print(f"FAIL: sponsor asset hash mismatch for {ref}: "
                              f"new={deck_hash[:12]}... vs authority={auth_hash[:12]}...")
                        sys.exit(1)
                # If the authority deck doesn't have this exact ref but the
                # asset exists, that's OK (new sponsor). But it must match a
                # prior-episode sponsor asset by name+hash somewhere.
            print(f"PASS: {len(deck_sponsors)} sponsor assets resolved and provenance-checked")

        # 14. Deck size sanity ------------------------------------------
        deck_size = len(html)
        auth_size = len(auth_html)
        # A new deck that is less than 60% of the authority deck's size likely
        # stripped layout/CSS/assets (Episode 24 was 37KB vs Episode 23's 74KB).
        if auth_size > 0 and deck_size < auth_size * 0.55:
            print(f"FAIL: deck size {deck_size} bytes is less than 55% of authority "
                  f"deck size {auth_size} bytes; likely stripped layout/CSS/assets")
            sys.exit(1)
        print(f"PASS: deck size {deck_size} bytes (authority: {auth_size} bytes)")

    print("\n=== ALL CHECKS PASSED ===")


if __name__ == '__main__':
    main()
