# Skill: research-tracking

## Purpose

Keep the living status of hypotheses and experiments accurate and easy to scan.

## When to use

- A hypothesis is created, started, supported, rejected, or parked
- An experiment starts or finishes
- Confidence or caveats change

## Canonical artifact

`workspace/<topic>/hypotheses.md` is the source of truth.

### Suggested format

```markdown
# Hypotheses — <topic>

| ID | Statement | Status | Confidence | Linked experiments | Notes |
|----|-----------|--------|------------|--------------------|-------|
| H1 | ...       | in-progress | medium | exp-price-drop | ... |
```

Status values: `proposed` | `in-progress` | `supported` | `rejected` | `inconclusive` | `parked`

## Discipline

- Update status as soon as evidence changes the picture
- Never leave a finished experiment without updating the linked hypothesis
- Keep notes short; details belong in the Research Report
