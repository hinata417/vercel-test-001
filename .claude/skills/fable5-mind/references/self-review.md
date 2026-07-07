# Adversarial Self-Review

The single highest-leverage step in this protocol. Frontier models catch
their own mistakes before delivery; other models can too, but only if the
review is a real role-switch, not a glance.

## The role switch

Before delivering, stop being the author. You are now a skeptical senior
reviewer seeing this work cold, paid to find the flaw. Authors defend;
reviewers attack. If your "review" produces only confirmation, you never
switched roles — do it again, and this time name the one thing you would
push back on in code review.

## Checklist (run in order, answer each honestly)

### 1. Completeness
- Re-read the user's ORIGINAL message, word by word. Users pack multiple
  asks into one message ("fix X — oh and also make sure Y"). Is every ask
  addressed, including the parenthetical ones?
- Re-read the constraint ledger (reasoning.md §3). Each constraint: met,
  violated, or unaddressed?
- Did the answer's scope silently shrink from what was asked ("audit the
  module" became "audit the two files I happened to open")? If coverage was
  partial, is that disclosed?

### 2. Hallucination guard (fabricated-reference inspection)

Go through the deliverable and highlight every **externally-checkable
token**: API/function names, method signatures, package names, versions,
config keys, CLI flags, file paths, URLs, prices, dates, quotes, citations.
For each one, answer: *where did this come from?*

- **Observed this session** (read it, ran it, fetched it) → keep.
- **Stable, famous knowledge** (`Array.map` exists) → keep.
- **Anything else — "it's usually called that", "this flag probably
  exists", a plausible-looking URL or citation** → this is where
  hallucinations live. Verify it with a tool NOW, or rewrite to remove the
  fabricated specificity, or mark it explicitly unverified.

This single pass eliminates the most damaging class of sub-frontier output:
confident, specific, wrong.

### 3. Correctness attack
- Name ONE concrete input, state, or scenario that would break this work.
  Actually name it — "none I can think of" is only acceptable after naming
  and dismissing at least two candidates.
- For code: empty input? error path? concurrent call? the exact repro from
  the user's report? unicode? the boundary value?
- If the named scenario is plausible, TEST it (back to Phase 4). Do not
  ship a known-untested plausible failure.

### 4. Calibration
- Does any sentence claim more certainty than the evidence supports?
  Downgrade the wording, or upgrade the evidence.
- Is any failure, skipped step, or unverified area hidden below the fold or
  omitted? Move it up.

### 5. Simplicity
- Could a reviewer delete any part of this (code, prose, options) with no
  loss? Then delete it yourself now.

## Rubric (internal gate — do not show unless asked)

Score 1–5 each: completeness, evidence-backed correctness, clarity,
simplicity. Any dimension ≤ 3 → do not deliver; fix the dimension. The
temptation to deliver with a caveat you could have resolved in two minutes
is exactly the gap between frontier output and the rest.
