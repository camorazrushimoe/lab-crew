# Skill: hypothesis-crafting

## Purpose

Turn a fuzzy idea or research brief into one or more explicit, testable hypotheses.

## When to use

- A new research request arrives
- An existing idea is too vague to experiment on
- Results come back and new hypotheses need to be generated

## What a good hypothesis looks like

A hypothesis should be:

1. **Specific** — names the variables or signals involved
2. **Testable** — it is possible to collect evidence for/against it
3. **Falsifiable** — there is a clear way it can fail
4. **Scoped** — not trying to prove an entire product vision at once

### Template

```markdown
### H1 — <short name>
**Statement:** ...
**Success criteria:** ...
**Failure criteria:** ...
**Why it matters:** ...
**Cheapest first test:** ...
**Status:** proposed | in-progress | supported | rejected | inconclusive
```

## Process

1. Restate the original idea in one plain sentence.
2. Extract the core claim(s).
3. Split into the smallest useful hypotheses.
4. For each hypothesis write success/failure criteria.
5. Propose the cheapest possible first experiment.
6. Add them to `hypotheses.md`.

## Anti-patterns

- "Users will love this" (not testable)
- "We need a full data platform" (solution, not hypothesis)
- Hypotheses that require production infrastructure before any signal is observed
