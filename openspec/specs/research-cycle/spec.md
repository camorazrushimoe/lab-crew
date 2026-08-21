# Research Cycle

## ADDED Requirements

### Requirement: Hypothesis-first entry

Every research cycle SHALL begin with at least one explicit, testable hypothesis written by Research Lead (or reviewed and accepted by Research Lead).

#### Scenario: task without hypothesis

- **WHEN** a research request arrives without an explicit hypothesis
- **THEN** Research Lead SHALL formulate or request hypotheses before any experiment is started

### Requirement: Cheap experiments first

Experiments SHALL prefer temporary data, lightweight scripts and small samples over production infrastructure.

#### Scenario: infrastructure request during research

- **WHEN** a need for production databases, vector stores or full pipelines appears during research
- **THEN** the team SHALL first ask whether the hypothesis has already been validated enough to justify the investment
- **AND** SHALL default to a cheaper alternative unless the manager explicitly overrides

### Requirement: Evaluation is mandatory

Every hypothesis that is tested SHALL have an associated evaluation approach (auto, human, or both) defined before or during the experiment.

#### Scenario: experiment without measurement

- **WHEN** an experiment is proposed without success/failure criteria
- **THEN** Evaluation Specialist SHALL block or require definition of measurement before results are treated as conclusive

### Requirement: Research Package as primary output

A completed research cycle SHALL produce a Research Package containing:

- Hypotheses log with status and confidence
- Summary of data sources and limitations
- Key experiment results
- Evaluation design and outcomes
- Research Report with recommendations
- Optional handoff section for DevCrew

#### Scenario: successful cycle ends with package

- **WHEN** a research cycle reaches a conclusion (supported / rejected / inconclusive)
- **THEN** Research Lead SHALL produce or update the Research Package
