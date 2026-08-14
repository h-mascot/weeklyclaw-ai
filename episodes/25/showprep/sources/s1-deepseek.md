# S1 — DeepSeek ships the model, the harness, and the API dialect

**Candidate:** C20 — DeepSeek ships the model + harness + Codex-compatible API (Aug 13)
**Score:** 9.9
**Owner:** Andy (lead) · Henry (co-lead cold open)

## Story

DeepSeek-V4-Pro-0813 reached GA on August 13, 2026. The release shipped three things in one news cycle: a 1.65T-param MIT-licensed model checkpoint, an OpenAI Responses + Anthropic Messages compatible API dialect, and the MIT-licensed DeepSeek Harness (TypeScript, everything-is-a-plugin). The npm family `@deepseek-ai/dsh` ships an executable CLI; the repo had 805 GitHub stars at retrieval.

## Numbers

- **1.65T params**, **66 safetensor shards** on Hugging Face
- **1,048,576 / 384,000** tokens (context / completion)
- **OpenRouter AA index 53** (independent)
- **805** GitHub stars on DeepSeek Harness at retrieval

## Vendor-reported vs independent

- DeepSeek-reported (NOT independently reproduced): Terminal Bench 2.1 = 87.9, NL2Repo = 61.5, DeepSWE = 62.7, Toolathlon-Verified = 74.1.
- Independent: OpenRouter Artificial Analysis index 53 — but this is not a harness-matched run, so it does not validate DeepSeek's harness-leveraged claims.
- No independent benchmark of DeepSeek Harness's `everything-is-a-plugin` framework versus OpenClaw or Hermes at retrieval.

## Caveats

- Developer preview — compatibility may break.
- The "MIT-like" framing is correct for both weights and harness; the API dialect is API-level, not a license.
- 805 stars is a snapshot; do not extrapolate to "verified adoption."

## Sources

- https://api-docs.deepseek.com/updates/
- https://github.com/deepseek-ai/deepseek-harness
- https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813
- https://openrouter.ai/deepseek/v4-pro-0813
- https://www.npmjs.com/package/@deepseek-ai/dsh