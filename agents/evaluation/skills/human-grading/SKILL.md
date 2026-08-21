# Skill: human-grading

## Purpose

Design clear human grading protocols when automatic metrics are insufficient or misleading.

## When to use

- The research question involves quality, relevance, usefulness, or other subjective judgments
- Auto-eval exists but needs calibration or validation
- Building evaluation for agent outputs, summaries, recommendations, etc.

## What a good protocol includes

1. **Grading goal** — what decision the grades will support
2. **Scale** — binary, Likert, rubric categories (keep it simple)
3. **Definitions** — precise meaning of each score
4. **Examples** — positive, negative, and borderline cases
5. **Process** — how graders work, how disagreements are handled
6. **Quality checks** — inter-rater agreement, spot checks, gold examples

## Template

```markdown
## Human Grading Protocol: <name>

**Linked hypothesis / metric:** ...
**Scale:** ...
**Definitions:**
- Score 1: ...
- Score 2: ...
**Examples:**
- Good: ...
- Bad: ...
- Borderline: ...
**Process:** ...
**Agreement check:** ...
```

## Anti-patterns

- Vague labels (“good / bad”) without definitions
- No examples
- No plan for disagreement between graders
- Changing the rubric after seeing results without recording it
