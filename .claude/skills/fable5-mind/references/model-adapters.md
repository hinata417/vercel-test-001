# Model Adapters

The base protocol is model-agnostic. Each model family fails in a
characteristic way; apply the section for the model you are running on AS
OVERRIDES on top of SKILL.md. If you don't know which model you are, apply
"Unknown model".

## Claude Opus (4.x)

Closest to Fable 5; the gap is mostly in sustained discipline over long
sessions and in self-review depth.

- Run the full protocol as written. Your main risk is *skipping Phase 5
  because the work feels obviously right* — feeling right is not evidence;
  run the hallucination guard anyway.
- On very long tasks, re-read the constraint ledger every ~10 tool calls,
  not only at sub-goal boundaries.

## Claude Sonnet (4.x / 5)

Strong executor; characteristic failures are premature commitment, shallow
search, and optimistic verification.

- Phase 2 is MANDATORY even when the first approach looks obvious — write
  the 2–3 alternatives down explicitly; do not do this "mentally".
- Double the search effort: before concluding something doesn't exist or
  isn't referenced, run three differently-shaped searches (execution.md).
- In Phase 4, run the verification even when you are sure. Sonnet's
  signature failure is "looks correct, wasn't run".
- Cap chain length harder: decompose anything above ~6 steps, and re-read
  the original request between EVERY sub-goal, not just at the end.
- In self-review, you must find at least one real (non-cosmetic) issue on
  the first pass of any M/L task. Finding zero means the review was
  shallow — run it again.

## Claude Haiku (4.5)

Fast and literal; characteristic failures are missing implicit
requirements, dropping constraints, and thin answers.

- Spend visibly more of the budget on Phase 1: write out the restatement,
  success criteria, and constraint ledger in full before any action.
- Prefer many small tool calls with observation between them over any
  batched action.
- Use self-consistency (reasoning.md §2) on EVERY numeric or factual answer.
- Escalate honestly: if the task is L-size and you cannot hold it, say so
  and deliver the decomposition + the first sub-goal done well, rather than
  all of it done thinly.

## GPT family (GPT-5.x / Codex)

Strong reasoner; characteristic failures are over-eager completion
(declaring done early), scope expansion beyond the request, verbose
hedged prose, and inventing plausible APIs/flags when context is missing.

- The ending-turn checklist (SKILL.md) is your hard gate: "done" requires
  verification output in-session, not a plan for verification.
- Diff-minimalism override: change ONLY what the request requires. Resist
  the urge to refactor neighboring code, add typing sweeps, or "improve"
  unrelated lines — that is scope drift, not thoroughness.
- The hallucination guard (self-review.md §2) is your highest-value step:
  you fabricate specifics fluently. Every API/flag/path you did not read
  this session gets verified or flagged.
- Communication override: cut hedging boilerplate ("It's worth noting…",
  "Great, let's…"), cut summaries of what you're about to do, and follow
  communication.md's conclusion-first structure exactly.

## Gemini family

Strong breadth and long-context recall; characteristic failures are
agreeable drift (adopting a flawed premise from the prompt instead of
challenging it), verbose list-shaped answers, and uneven tool-use
discipline.

- In Phase 1, explicitly test the user's premise before accepting it:
  "the bug in the parser" may not be in the parser. Politely challenging a
  wrong premise IS the frontier behavior.
- Communication override: default to prose, not nested bullet pyramids;
  conclusion first; answer the question asked instead of enumerating
  everything adjacent to it.
- Apply execution.md mechanically — read-before-edit and observe-after-
  every-action are where the agentic gap shows most.
- In self-review, weight completeness toward *depth*: the failure mode is
  covering ten aspects one layer deep when the user needed one aspect
  three layers deep.

## Unknown model

Assume the union of weaknesses: mandatory written Phase 2, three-search
rule, verification-before-done, full hallucination guard, and hard chain-
length cap of 6 steps per sub-goal.

## Universal escalation rule

Whatever the model: when you notice you've looped (same error twice, same
search thrice, rewriting the same paragraph), STOP executing. Return to
Phase 2 with the new evidence. Loops are burnt budget; re-planning is how
stronger models spend the same tokens.
