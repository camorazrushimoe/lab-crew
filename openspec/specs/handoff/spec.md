# Handoff

## ADDED Requirements

### Requirement: Explicit handoff decision

At the end of a research cycle the team SHALL explicitly decide whether the findings are ready for product engineering (DevCrew) or not.

#### Scenario: research concludes

- **WHEN** a Research Report is finalized
- **THEN** Research Lead SHALL record one of: `ready-for-handoff` | `needs-more-research` | `stop`

### Requirement: Handoff package contents

A handoff package intended for DevCrew SHALL contain at least:

1. Summary of validated / rejected hypotheses
2. Recommended data sources and collection approach
3. Evaluation design and key metrics
4. Known risks, limitations and open questions
5. Draft product requirements or OpenSpec sketch (when available)

#### Scenario: DevCrew receives a package

- **WHEN** DevCrew receives a LabCrew handoff package
- **THEN** it SHALL be possible to start product work without needing the original LabCrew researchers to explain context from scratch

### Requirement: LabCrew does not implement the product

LabCrew agents SHALL NOT implement production features, production data pipelines or long-lived services as part of a handoff. Their job ends at the Research Package.
