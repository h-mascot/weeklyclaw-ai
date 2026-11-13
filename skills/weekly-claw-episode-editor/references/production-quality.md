# Production quality contract — 2026-10-04.1

Apply to Weekly Claw production together with [editorial-direction.md](editorial-direction.md). The current full-frame camera direction supersedes older automatic no-enlargement/padding defaults; the legacy validator retains its historical profile and scope.

## Carry forward the treatment, reassess the recording

- Compare the most recently approved episode's treatment and established footer design with the current editorial direction. Record its exact master hash as a visual baseline, never as approval for the new episode or authority to restore superseded camera defaults. Compare source-sized neutral/moving frames before choosing the new layout.
- Default to full-frame group panels with matched portrait crops. Use full-width solos only for sustained actual-speaker contributions supported by direct evidence. Choose face/eye-aware crops from the highest-resolution verified sources, preserve aspect and meaningful movement, and review early/middle/late posture. When frame fill needs source-limited enlargement, document the exact transform, quality tradeoff and hashed preview review under the current native profile. Never infer a universal scale allowance, hide detail loss, or substitute decorative padding/blurred filler.
- Assess exposure, white balance, contrast and source blur separately for every camera. Compare native source, proposed correction and the previous treatment at matched display sizes. Record a reasoned colour decision even when it is “no change.” Do not blindly reuse last week's gamma/brightness, or use heavy sharpening, denoise or generated facial detail to conceal source limitations.
- Information/fact-check notes remain the established section footer with live hosts above it. They are not new full-screen pages. Use `scripts/section_footer.py`; preserve source wording, literal percentages and citations. Native full-screen primary evidence and genuinely readable charts are a different editorial unit and remain permitted when useful. Larger claims must be split in time or carefully reflowed without shrinking text into illegibility.
- Keep authentic primary visuals, mapped demo motion and neutral source notes. The programme mark is a single alpha-transparent stacked `WEEKLY / [official green claw mark] CLAW` overlay fixed to the global bottom-left across all layouts, archive and outro; no plate or rail-relative movement. Keep participant names/verified handles tile-local without moving the mark. Inspect actual alpha and duplicate baked programme marks while preserving authentic source logos. Preserve the established ending and approved previous masters.

## Executable preflight

The builder/schema below applies only to the strict legacy FFmpeg two-up profile `2026-09-12.1`. It does not certify current full-frame native compositions or reviewed enlargement exceptions. For native Kdenlive use [native-quality-profile.md](native-quality-profile.md), the `native-evidence-2026-10-04.1` contract, explicitly reviewed native-effect mapping and actual moving proof. Hold the long render until native semantics and every represented composition are reviewed. Never fabricate a legacy plan to obtain PASS while encoding another graph.

Only when intentionally using that legacy graph, use `scripts/quality_gate.py` as its shared camera transform builder and call `preflight` from the render entry point **before encoding**. A standalone PASS followed by a different graph is not enforcement. On a scratch render host, transfer the exact helper and record its hash; do not substitute an old host-local copy.

The current layout-plan schema adds `quality_contract`:

```json
{
  "version": "2026-09-12.1",
  "baseline_master_sha256": "<64-character hash of the actual approved visual baseline>",
  "camera_sources": {"AndyML": "<verified aligned filename>", "HiM": "<verified aligned filename>"},
  "color": {"AndyML": {"gamma": 1.08}, "HiM": {}},
  "review_evidence": [{"path": "<episode-relative assessment or comparison file>", "sha256": "<actual file hash>"}]
}
```

The colour values above illustrate the schema, not a preset. Camera transforms use explicit `crop: [width,height,x,y]`, `scale: [width,height]`, and optional solid-colour `pad: [width,height,x,y]`. Probe and hash actual independent camera sources. Run:

```bash
python3 scripts/quality_gate.py /absolute/episode/layout-plan.json --report /absolute/episode/quality-preflight.json
```

The legacy gate rejects enlargement, stretching, invalid crop bounds, missing camera/colour review, changed evidence/assets, and full-page information notes. Record its profile/validator/plan/source hashes in receipts. Do not silently waive or weaken it to reuse a shot. Current full-frame source-quality exceptions belong to the revised native profile with actual hashed review evidence, not a fabricated legacy PASS.

After encoding, run the existing media audit and inspect actual first/middle/last changed-shot samples, every affected boundary, mobile-size source text and a short moving before/after comparison. Check the final MP4, not just the source or storyboard. A numeric geometry pass cannot establish tasteful colour, perceptual sharpness, privacy clearance, sync or listening.

For future scheduled runs, read this current reference and run the applicable legacy or native preflight branch afresh. Do not inherit a previous PASS or hard-code episode-specific camera filenames/coordinates into the shared skill. Preserve earlier masters and all human approval boundaries.
