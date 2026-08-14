# S2 — GLM-5.3 cyber via post-training; weights delayed two weeks

**Candidate:** C24 — Z.ai delays GLM-5.3 weights 2 weeks after cyber gain (Aug 14)
**Score:** 9.8
**Owner:** Henry (lead) · Andy (handoff)

## Story

Z.ai launched GLM-5.3 on August 14, 2026 using the same 743B-class base as GLM-5.2. Every reported gain came from post-training (more executable environments, more verifiers, more RL) — the base model is unchanged. The capability delta on exploit-chain tasks (+30.0pp on ExploitBench) was large enough that the company delayed the downloadable weights by two weeks for safety evaluation and hardening.

## Numbers

- Terminal-Bench 3.0: **4.6 → 28.3** (+23.7)
- DeepSWE v1.1: **46.2 → 66.9** (+20.7)
- CyberGym: **77.2% → 84.5%** (+7.3pp)
- ExploitBench: **24.4% → 54.4%** (+30.0pp)
- Findings audited: **2,436** across **269** projects, **1,097** critical/high severity
- cvd.z.ai ledger: **53 disclosed**, **2,383 under embargo** at retrieval
- Weight delay: **two weeks**

## Vendor-reported vs independent

- ALL benchmark deltas are Z.ai evaluation runs, single-run, not independently reproduced.
- The cvd.z.ai ledger counts were Z.ai's own audit queue at retrieval.
- No GLM-5.3 repository present on the official `zai-org` Hugging Face org at cutoff.

## Caveats

- This build did not validate any 5.3 number, severity label, or finding attribution.
- A "two-week weight delay" is a Z.ai announcement, not an external regulator or auditor's decision.
- The disclosure ladder mixes internal audits with externally-submitted vulnerabilities; framing must be precise on air.

## Sources

- https://z.ai/blog/glm-5.3
- https://cvd.z.ai/
- https://docs.z.ai/devpack/overview
- https://huggingface.co/zai-org (5.3 not yet present at cutoff)