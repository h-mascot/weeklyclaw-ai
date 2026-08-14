# S5 — OpenAI turns Mac activity and Drive files into ambient work context

**Candidate:** C27 — OpenAI Computer History + Google Drive in Library (Aug 13)
**Score:** 9.8
**Owner:** Andy (lead) · Henry (handoff)

## Story

On August 13, OpenAI shipped Computer History for macOS — interaction events from selected apps and sites, NOT screenshots, screen recordings, microphone, or system audio — and made connected Google Drive files and folders browsable in Library. The personal agent stops needing a daily briefing; it reconstructs what happened.

## What Computer History captures / does not capture

- **Captures:** selected app and website interaction events
- **Does NOT capture:** private browsing, screenshots, screen recordings, microphone, system audio
- **Controls:** off by default, inclusion lists for apps/sites, pause, timeline inspection, deletion
- **Admin:** Business / Enterprise admin enablement + individual opt-in
- **Rollout:** Pro / Business / Enterprise outside EEA, UK, Switzerland first

## Google Drive in Library

- Connected Drive files and folders browsable in Library
- Keep Docs / Sheets / Slides beside a conversation
- Work across a selected folder; update source file where authorized
- Shared Drives and some collaboration features not yet included
- Builds on Chronicle with reduced token use and more privacy controls

## Vendor-reported vs independent

- ALL of OpenAI's framing is interaction events vs screen recording; this build did NOT inspect local event files, server-side retention behavior, deletion completeness, cross-workspace leakage, or real recall quality.
- The rollout geography (excluding EEA / UK / Switzerland first) is OpenAI's own disclosure; regulatory review status is not in scope.
- Shared Drives exclusion is OpenAI's product status disclosure, not an external feature comparison.

## Caveats

- Do not characterise Computer History as "always on" — it is opt-in, off by default, with explicit admin/user gating.
- Do not imply ambient memory is end-to-end encrypted at rest — OpenAI's framing distinguishes "off by default + opt-in" from "fully encrypted" without equating them.
- The "update source file where authorized" framing must include "where authorized" — it is gated per resource.

## Sources

- https://help.openai.com/en/articles/6825453-chatgpt-release-notes
- https://x.com/OpenAI/status/2087996496088297746 (OpenAI official X — Computer History)