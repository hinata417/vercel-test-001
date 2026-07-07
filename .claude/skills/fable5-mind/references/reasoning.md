# Deep-Reasoning Tactics

How to convert extra thinking into extra correctness. These tactics are what
"more intelligence" mostly cashes out to in practice — and every one of them
can be executed deliberately by a smaller model.

## 1. Hypothesis trees (debugging, diagnosis, research)

When facing a "why does X happen?" question:

1. Enumerate ALL plausible causes first — aim for 3–6 — before investigating
   any of them. Write them down (scratchpad, comment, or thinking).
2. For each, note the cheapest observation that would confirm or kill it.
3. Investigate in order of (probability × cheapness). Kill hypotheses with
   evidence, never with vibes.
4. When evidence kills your favorite hypothesis, that is progress. Do not
   bend the evidence to save the hypothesis.
5. If all hypotheses die, the enumeration was too narrow — widen one level
   (wrong file? wrong process? wrong machine? wrong assumption about the
   spec itself?) and restart.

Anti-pattern to avoid: latching onto the first plausible cause and building
an increasingly elaborate story around it ("motivated reasoning"). Frontier
models are better at abandoning bad branches — replicate that by making
branch-abandonment an explicit, evidence-triggered step.

## 2. Self-consistency (high-stakes single answers)

For any answer where being wrong is costly (a number, a root cause, a legal/
API/date fact, a design decision):

1. Derive the answer once.
2. Derive it AGAIN via a genuinely different route (different formula,
   different starting point, different source, inverse direction).
3. Match → confidence justified. Mismatch → you found a bug in your own
   reasoning before the user did. Reconcile before answering.

For arithmetic and unit conversions: always compute twice, once forwards and
once by checking the inverse. Never trust a single mental calculation.

## 3. Constraint ledger (long or multi-part tasks)

Non-frontier models lose constraints stated early ("must stay backwards
compatible", "don't touch the config", "answer in French") as context grows.
Countermeasure:

1. At Phase 1, write an explicit numbered list of every constraint in the
   request — including implicit ones (existing tests must keep passing;
   public API stays stable).
2. Before delivering, re-read the ledger item by item and check each one
   against the actual work. A violated constraint is a Phase 3 failure, not
   a footnote.
3. **After any context compaction/summarization** (long agentic sessions):
   assume constraint loss. Re-read the user's original message and rebuild
   the ledger before continuing — the summary kept the task; it may have
   dropped the "don't"s.

## 4. Think longer — but only where it pays

Extra deliberation helps at decision points and hurts (via drift) during
mechanical execution. Spend thinking on:
- choosing between approaches (Phase 2),
- interpreting ambiguous requirements,
- post-mortem when verification fails,
- the adversarial self-review.

Do NOT spend it re-justifying decisions already made or narrating routine
steps. When a step is mechanical, execute it mechanically.

## 5. Know the edge of your knowledge

- Anything time-sensitive (versions, prices, APIs, news) that postdates your
  training: verify with a tool or mark as unverified. Never present recalled
  time-sensitive facts as current.
- Distinguish three confidence levels explicitly in your own reasoning:
  I observed it this session / I recall it and it is stable knowledge /
  I am inferring it. Only the first two may be stated without hedging, and
  only the first for anything project-specific.

## 6. Inversion

Before finalizing a design or a conclusion, invert: "Assume this is wrong —
what is the most likely way?" One minute of inversion catches the majority
of confident-but-wrong deliveries. If the inversion produces a concrete,
plausible failure mode, test it (Phase 4) instead of shipping the risk.
