# S4 — Writer cuts agent cost in the harness, not the model alone

**Candidate:** C26 — Writer harness + Palmyra X6 agent cost cuts (Aug 13)
**Score:** 9.6
**Owner:** Andy (lead)

## Story

Writer's updated harness made six tested models 33–61% cheaper, raised quality per dollar 82%, and averaged 44% faster completion at parity. Paired with Palmyra X6 (GLM-5.2 base, 1M context, $2/$8 per M tok), the company reports 52% lower cost, 48% faster work, 10% higher quality at ~$0.12 per finished task.

## Numbers

- **33–61%** cost reduction across six tested models
- **82%** quality per dollar improvement
- **44%** faster completion at parity
- **52% / 48% / 10%** with Palmyra X6 (cost / speed / quality)
- **~$0.12** per finished task
- **7,876 / 7,886** cache read rate (byte-stable prefix)
- **n=22 prompts, 6 models, r=0.99**
- **8 hours** write-ahead recovery objective

## Harness levers (six)

1. Stable prompt prefix (byte-stable) — cache read 7,876 / 7,886
2. Typed compaction at 80% budget — auto-summary and offload
3. Context offload to durable store — resumable from disk
4. Zero-token suspension (wait) — no idle billing
5. Bounded retries + failure routing — avoid repeated error loops
6. Write-ahead recovery — up to 8 hours on a single task

## Vendor-reported vs independent

- ALL cost/quality figures are Writer-run on n=22 prompts across 6 models.
- The r=0.99 result spans only six models; figures are directional, not a general benchmark.
- Independent workload test was not performed in this build.
- VentureBeat corroborated the 52% headline number but not the underlying harness research.

## Caveats

- Do not extrapolate Writer's 33–61% reduction across all harnesses — n=6, directional.
- Do not claim r=0.99 implies a universal harness-leverage effect.
- Palmyra X6 is GLM-5.2-base — quality deltas vs GLM-5.3 are unknown.

## Sources

- https://writer.com/blog/aug-roundup-new-at-writer/
- https://writer.com/engineering/harness-research-tokens-efficiency-cost-spend-ai/
- https://dev.writer.com/home/models
- https://venturebeat.com/orchestration/writer-says-its-new-palmyra-x6-model-cuts-ai-agent-costs-by-52-as-token-spending-surges