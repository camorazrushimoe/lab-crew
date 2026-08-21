# Artifacts

## ADDED Requirements

### Requirement: Standard research topic layout

Each research topic SHALL live under `workspace/<topic>/` with at least the following conventional files/directories (when applicable):

```
workspace/<topic>/
  BRIEF.md              # original request / research brief
  hypotheses.md         # living list of hypotheses + status
  experiments/          # scripts, notebooks, intermediate results
  data/                 # temporary data (usually gitignored)
  evaluation/           # evaluation design, grading protocols, results
  report.md             # Research Report
  handoff/              # package intended for DevCrew (optional)
```

#### Scenario: new research topic started

- **WHEN** Research Lead starts a new research topic
- **THEN** the conventional directory structure SHALL be created or referenced

### Requirement: Hypotheses log is the source of truth for status

The file `hypotheses.md` (or equivalent) SHALL be the canonical place to track hypothesis status (`proposed` / `in-progress` / `supported` / `rejected` / `inconclusive`) and confidence notes.

### Requirement: Handoff package is explicit

When research is intended to feed product work, a handoff package SHALL be produced under `handoff/` (or equivalent) and SHALL contain enough information for DevCrew to start without needing the original researchers present.

Minimum useful contents:
- What was validated / rejected
- Recommended data sources and collection approach
- Evaluation / metrics recommendations
- Open questions and risks
- Draft requirements or OpenSpec sketch (if ready)
