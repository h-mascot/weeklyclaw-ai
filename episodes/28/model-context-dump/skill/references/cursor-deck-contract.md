# Cursor deck contract: fallback and validation receipt

## Required output contract

A successful Cursor run must produce all six files in `output/`:

- `deck.html`
- `speaker-notes.md`
- `talking-points.md`
- `henry-section.md`
- `andy-section.md`
- `host-cheat-sheet.md`

Do not accept a partial run even when Cursor exits 0. In one verified run, Kimi produced only deck, speaker notes, talking points, and Henry view before hanging; Opus produced only deck, speaker notes, and talking points before hanging. Both were failures because the host views/cheat sheet were incomplete. Sol completed all six files.

## Fallback receipt fields

For each attempted model, record:

```json
{
  "model": "kimi-k3-high",
  "exit": "timeout/incomplete",
  "artifacts": ["deck.html"],
  "fallback_reason": "required files absent after bounded wait",
  "artifact_hashes": {}
}
```

Then clear partial output before the next model, or place it in a clearly labelled failed-attempt directory. Never merge partial model outputs into a supposedly successful revision.

## Local validation recipe

1. Confirm all six files exist and are non-empty.
2. Parse `state.json`, `candidates.json`, and `media-manifest.json` with `python3 -m json.tool`.
3. Extract slide IDs from both possible HTML attribute orders:

```python
slides = re.findall(
    r'<(?:section|div)\\b[^>]*class=["\\\'][^"\\\']*\\bslide\\b[^"\\\']*["\\\'][^>]*id=["\\\']([^"\\\']+)',
    html, re.I
)
slides += re.findall(
    r'<(?:section|div)\\b[^>]*id=["\\\']([^"\\\']+)["\\\'][^>]*class=["\\\'][^"\\\']*\\bslide\\b',
    html, re.I
)
```

4. Extract notes with `^##\\s+(s\\S+)$` in multiline mode. Assert slide IDs and note IDs are equal in order, with no duplicates.
5. Assert the deck has navigation hooks, a final Sources/Links slide, visible external source links, and no `<video ... autoplay` attribute.
6. Validate embedded JavaScript by extracting `<script>` bodies to `/tmp/` and running `node --check`; process substitution can fail under Node because `/proc` pipe paths disappear.
7. Hash revision files and the normalized candidate set. Keep the hashes in `rev<N>-hashes.txt`, `state.json`, and `evidence.md`.

## Evidence language

Use precise labels:

- `primary`: official report, docs, release, model card, or paper.
- `secondary`: a source describing another source or comparison without its own receipt.
- `vendor-reported`: publisher benchmark or performance claim.
- `author-reported/unreplicated`: fresh preprint metrics without independent rerun.
- `fallback still`: a verified static cue, not a fabricated screenshot.

A deck may pass structural validation while still being `UNVALIDATED` for host approval. Keep those states separate.
