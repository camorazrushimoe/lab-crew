# Skill: research-briefing

## Purpose

Write a clear, actionable brief for Research Engineer so an experiment can start without ambiguity.

## When to use

- After hypotheses are formulated and prioritized
- When handing a specific experiment to Research Engineer

## What a good brief contains

1. **Hypothesis reference** — which hypothesis (H1, H2…) this experiment serves
2. **Goal** — what question this experiment must answer
3. **Success / failure signals** — what result would support or reject the hypothesis
4. **Constraints** — time, data limits, “cheap first” requirements
5. **Out of scope** — what the engineer should *not* build
6. **Handoff point** — when to stop and report back

## Template

```markdown
## Experiment Brief: <short name>

**Hypothesis:** H1 — ...
**Goal:** ...
**Success signal:** ...
**Failure signal:** ...
**Constraints:**
- Prefer temporary data
- No production infrastructure
- Max effort: ...
**Out of scope:** ...
**Report back when:** ...
```

## Anti-patterns

- Briefs that say “explore the data” without a hypothesis
- Asking for a full pipeline before any signal is observed
- Missing success/failure criteria
