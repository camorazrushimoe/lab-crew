# Skill: evaluation-critique

## Purpose

Actively look for ways an evaluation (or experiment result) could be misleading.

## When to use

- Before treating results as conclusive
- When reviewing experiment design
- When a metric looks “too good” or surprisingly clean

## Common failure modes to check

- **Leakage** — information from the future or from the label leaked into features
- **Selection bias** — the sample is not representative of the claimed population
- **Cherry-picking** — only favorable slices are reported
- **Metric mismatch** — the metric does not measure the actual hypothesis
- **Tiny sample** — confidence is overstated
- **Confounding** — an alternative explanation fits the data equally well
- **Non-reproducibility** — results depend on hidden choices or unstable code

## Output

Write a short critique note:

```markdown
## Evaluation Critique

**Target:** <experiment or metric>
**Risks found:**
- ...
**Severity:** low / medium / high
**Recommendation:** accept with caveats / re-run / redesign measurement
```

## Discipline

- Be specific. “Might be biased” is not enough.
- Prefer actionable recommendations over pure skepticism.
