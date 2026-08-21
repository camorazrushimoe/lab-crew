# Skill: metric-design

## Purpose

Choose and define metrics that actually answer the research question instead of the easiest number to compute.

## When to use

- A new hypothesis is formulated
- An experiment design is being reviewed
- Results look "good" but the metric may be misleading

## Process

1. Restate the hypothesis in plain language.
2. Ask: "What would have to be true in the data for this hypothesis to be supported?"
3. Propose 1–3 candidate metrics.
4. For each metric define:
   - Exact formula or procedure
   - Required data fields
   - Known failure modes (leakage, selection bias, etc.)
   - Whether it can be automated or needs human judgment
5. Prefer simpler metrics when they are more honest.

## Output format

```markdown
### Metric: <name>
- **Linked hypothesis:** H1
- **Definition:** ...
- **Data needed:** ...
- **Automation:** auto | human | hybrid
- **Risks:** ...
- **Interpretation guide:** higher/lower means ...
```

## Anti-patterns

- Using accuracy when the class balance is extreme
- Optimizing a proxy that is easy to game
- Claiming statistical significance on tiny samples without caveats
- Changing the metric after seeing the results
