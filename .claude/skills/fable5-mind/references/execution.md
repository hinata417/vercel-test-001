# Agentic Execution Discipline (coding tasks)

Tool-use habits that separate frontier agents from average ones. Apply on
top of SKILL.md Phase 3.

## Reading before writing

- NEVER edit a file you have not read in this session. No exceptions.
- Read enough context: the function you're changing, its callers, its tests.
  Editing a function without reading one caller is a guess, not an edit.
- Before adding anything (helper, dependency, config key), search for an
  existing one. Duplicating an existing utility is a correctness bug waiting
  to happen and a review-time embarrassment.
- Learn the project's conventions from the project itself: how do existing
  modules handle errors, logging, naming, tests? Conform. If the project
  has CLAUDE.md / AGENTS.md / CONTRIBUTING.md, those override your defaults.

## Search strategy

- Prefer structural search (grep for the symbol, glob for the filename) over
  reading files one by one.
- When a search returns nothing, distrust the pattern before distrusting the
  premise: try case-insensitive, try a substring, try a synonym. Three empty
  searches with varied patterns = real evidence of absence; one is not.
- Locate ALL usage sites before renaming/changing a shared symbol. The
  compiler will not catch string references, configs, docs, or reflection.

## Edit hygiene

- One logical change at a time; verify between changes. When a batch of
  edits fails, a batch is also what you must bisect.
- Preserve behavior you were not asked to change — including whitespace,
  comment style, and public signatures.
- Never delete or overwrite something you don't understand. If a file's
  content contradicts what you expected, stop and surface the contradiction.
- Leave no debugging residue: no stray prints, no commented-out code, no
  TODO you added for yourself.

## Running things

- Reproduce the bug BEFORE fixing it. A fix for an unreproduced bug is a
  hypothesis, and must be labeled as one.
- After the fix, re-run the same reproduction and show the difference.
- Run the project's own test suite the project's own way (check package.json
  / Makefile / CI config for the real command), not a generic guess.
- Long/destructive commands: check what they will do first (`--dry-run`,
  `git status`, `ls` the target) before executing.

## Failure protocol

1. Read the WHOLE error message, including the middle of the stack trace.
   The answer is usually literally printed.
2. Form a hypothesis; state (to yourself) what output would confirm it.
3. Make the single cheapest observation that tests the hypothesis.
4. Two dead hypotheses → widen scope (env? version? wrong file? stale
   build cache?). Five minutes of loop → step back and re-plan; grinding
   the same wall is a model-quality giveaway.
5. Never suppress an error to make it go away (bare except, `|| true`,
   ts-ignore) unless the user asked for exactly that.

## Over-engineering: the warning signs

Simplicity is intelligence. Stop and reconsider when you notice yourself:

- Adding a config option, parameter, or abstraction layer "for flexibility"
  that no current caller needs.
- Building a general solution when the request was one concrete case.
- Introducing a new dependency for something 15 lines of code would do.
- Creating interfaces/base classes with exactly one implementation.
- Writing more test scaffolding than test.
- Handling error cases that cannot occur given the actual call sites.

The fix is always the same: delete down to the smallest change that fully
solves the stated problem, and mention the considered-and-rejected
generalization in your report if it matters.

## Version control

- Work on the designated branch; never commit to main uninvited.
- Commit messages describe WHY at the first line, not a file list.
- Before committing: `git diff` and actually read it. You are the first
  reviewer. Anything in the diff you can't justify, remove.
- Never `push --force`, never rewrite shared history, never delete branches
  you didn't create, unless explicitly instructed.
