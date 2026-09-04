# WeeklyClaw Thumbnail Host-Likeness Rules (2026-08-26)

Authoritative likeness contract for WeeklyClaw YouTube thumbnails (host art generated on Enterprise under `~ent/Documents/WeeklyClawVideo/`, driven by Geordi/Codex). Written after Henry rejected regenerated ep23–26 thumbnails for wrong faces despite a "canonical host identity lock" already existing.

## Identity mapping (verified against live approved thumbnails + public profile photos)

- **Andy = bald, light-skinned, short dense beard.** Always LEFT position.
- **Henry = dark-skinned, curly hair, full black beard, glasses, dark cap with white emblem (current look), headphones, mustard-gold shirt (ep26-era).** Always RIGHT position.
- The identity card (Henry-supplied reference) labels are CORRECT, not swapped — early suspicion of swapped labels was disproven. Bad outputs were likeness failures, not placement failures.

## Ground-truth reference assets (Enterprise)

- Highest-authority likeness refs: cropped card headshots at
  `~ent/Documents/WeeklyClawVideo/work/host-identity-pack/henry-ground-truth-20260826/card-andy.jpg` and `card-henry.jpg` (plus `card-refs-clean.jpg`).
- Rule: **card wins on any conflict** with other references. This is patched into `work/host-identity-pack/generation-prompt.md`.
- Good generated exemplars: approved thumbnails for episodes 21 and 22 (Henry named them as correct).
- QA ingest crops: `work/episode-26/andyml-900.jpg`, `him-2100.jpg`.

## The failure mode: "broad-but-generic"

The old QA gate only checked geometry (Andy broad/near-square vs oval). Wrong outputs still passed because they were broad but looked like a **generic handsome chiselled bald podcast man**. Reject on ANY of:

- angular/chiselled jaw; hollow or sunken cheeks; pointed/narrow chin
- sparse/patchy/wispy beard
- smaller, slimmer, more refined nose
- older/leaner overall look

## Andy positive likeness markers (require these)

- large round head relative to shoulders
- full fleshy cheek apples; soft wide rounded chin; wide but softly padded jaw
- dense, dark, FULLY-connected beard
- medium-to-large substantial nose
- mid-30s regular-guy appearance, not model-lean

## Henry positive markers

- exact current cap (Episode 26 dark cap, white emblem), glasses, headphones, dense beard, mustard-gold shirt — cap/wardrobe drift is a QA failure, not a style choice.

## QA gate contract

A thumbnail passes likeness QA only if BOTH geometry AND soft-tissue likeness match the card refs. Files carrying the rules (Enterprise, keep in sync when touching any):

1. `work/host-identity-pack/generation-prompt.md` (generation-time rules + rejection criteria)
2. `work/host-identity-pack/README.md`
3. `~/.codex/skills/thumbnail-skill/SKILL.md` (QA requirements)

## Pipeline facts

- Deterministic branding: base art generated WITHOUT text/logo/badge (reserved: upper-left logo, upper-right badge, lower-center headline); typography added afterward by the build script.
- Archive layout: `work/thumbnail-archive/<date>/episode-N/` with prompts + QA record; finals copied to `assets/thumbnails/`, mobile derivative `-160x90.png`.
- QA must be checked at full size AND 160×90 (mobile readability).
- Generation provider: Gemini Nano Banana Pro (`gemini-3-pro-image-preview`) via `ce-gemini-imagegen` skill + `GEMINI_API_KEY` env; the OpenAI direct route is billing-blocked (`429 credit_balance_exhausted`) and must not be retried without new credits.
