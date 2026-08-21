# Skill: auto-eval

## Purpose

Design and implement automatic evaluation when the research question allows it.

## When to use

- A metric can be computed from data without human judgment
- Human grading exists and needs a scalable companion metric
- Agent outputs, rankings, classifications, or structured predictions must be scored repeatedly

## Process

1. Confirm the metric definition with Research Lead (and metric-design skill)
2. Implement a small, readable evaluation script
3. Run it on the experiment outputs
4. Report:
   - metric values
   - sample size
   - failure cases / edge cases
   - confidence caveats
5. Store evaluation code under `evaluation/` so it can be re-run

## Discipline

- Prefer simple, inspectable code over heavy frameworks at research stage
- Always show a few concrete examples of correct and incorrect cases
- If auto-eval disagrees with human grades, investigate instead of ignoring

## Anti-patterns

- Opaque scoring functions nobody can audit
- Reporting a single number without examples
- Changing the metric definition after seeing the score without recording the change
