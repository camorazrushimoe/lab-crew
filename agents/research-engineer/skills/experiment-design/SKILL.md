# Skill: experiment-design

## Purpose

Design the cheapest viable experiment that can produce evidence for or against a hypothesis.

## When to use

- Research Lead hands over a hypothesis
- An existing experiment is too expensive or slow and needs a lighter version

## Process

1. Read the hypothesis and its success/failure criteria.
2. List the minimum data required to test it.
3. Prefer:
   - Existing public data or quick scrapes over long collection campaigns
   - Small samples over complete historical data
   - Scripts over services
   - Local / temporary storage over production databases
4. Write a short experiment plan:
   - What will be collected
   - How it will be collected
   - What analysis will be run
   - What result would support / reject the hypothesis
   - Estimated effort and risks
5. Coordinate with Evaluation Specialist on measurement before starting heavy collection.

## Output format

```markdown
### Experiment: <short name>
- **Hypothesis:** H1
- **Goal:** ...
- **Data plan:** ...
- **Method:** ...
- **Success signal:** ...
- **Failure signal:** ...
- **Effort estimate:** ...
- **Risks / caveats:** ...
```

## Anti-patterns

- Building a full pipeline "just in case"
- Collecting months of data before any signal is observed
- Starting analysis without knowing how success will be measured
