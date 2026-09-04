# Host-feedback parallel execution

Use when a host sends several review items, especially through reply-to text plus screenshot, and asks for a specific worker count.

## Routing template

### Read-only scout

- Episode/date and authoritative revision
- Exact question to answer
- Allowed source paths and external sources
- No writes
- Return: evidence, exact locations, proposed change, caveats

### Implementation owner

- Episode/date and authoritative revision
- Consolidated approved findings from scouts
- Sole write authority for the next revision
- Required outputs: all seven package artifacts, state/evidence/runlog updates, validation receipt, render-QA receipt, website-draft verification when applicable

### Coordinator

- Dispatches workers in background
- Keeps conversation thread responsive
- Does not duplicate delegated implementation when user requested subagent-only execution
- Reconciles conflicts and verifies artifacts after workers finish

## Reply and screenshot recovery

Treat reply-to text, caption, screenshot, and attachment as one packet. Extract:

1. Superseded material
2. Replacement material
3. Editorial edits
4. Research questions
5. Requested links or delivery surfaces

If the packet says “use this instead” but the replacement itself is missing or unreadable, mark only that item `BLOCKED: replacement payload absent`. Do not preserve the rejected talk track by inertia. Continue independent items.

## Receipt contract

Each worker returns:

- Status: DONE / BLOCKED
- Inputs inspected
- Evidence or source URLs
- Files changed, or `none` for scouts
- Validation performed
- Remaining uncertainty

Coordinator final receipt names requested worker count, actual dispatched count, implementation owner, final revision, validation status, and mobile-openable links. Never imply the thread is occupied by background work.
