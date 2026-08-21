# Agent Roles

## ADDED Requirements

### Requirement: Three research agents

The factory SHALL run three agents, each in its own container with a distinct role and webhook door:

| Role | Door (host) | Owns |
|------|-------------|------|
| `research-lead` | `8751` | Research questions, hypotheses, synthesis, Research Report, handoff package |
| `research-engineer` | `8752` | Experiment design & execution, data collection scripts, intermediate analysis |
| `evaluation` | `8753` | Evaluation design, auto-eval, human grading protocols, metric integrity |

#### Scenario: every agent is reachable

- **WHEN** the factory is running
- **THEN** each role SHALL be reachable on its own host port (8751–8753)

### Requirement: Identity is mounted, not baked in

Each agent SHALL load its identity from `SOUL.md` and its capabilities from role skills.

#### Scenario: role stays project-agnostic

- **WHEN** an agent boots
- **THEN** its SOUL SHALL describe only its role and discipline
- **AND** SHALL NOT contain project-specific research context

### Requirement: English-only research artifacts

Agents SHALL produce hypotheses, reports, experiment notes and handoff packages in English.
