# Lab Crew — Architecture

> Draft. Will evolve as we implement.

## Overview

LabCrew is a portable agent factory focused on **hypothesis-driven research**.
It produces validated understanding and Research Packages that can be handed to DevCrew for product engineering.

```text
Manager / Business Idea
        │
        ▼
┌───────────────────────────────────────────────────────┐
│                    Lab Crew                           │
│                                                       │
│  research-lead  ◄──►  research-engineer  ◄──►  evaluation │
│         │                    │                    │   │
│         └──────────── shared-memory (Redis) ──────┘   │
│                                                       │
│  workspace/  ← temporary data, notebooks, reports     │
└───────────────────────────────────────────────────────┘
        │
        ▼
 Research Package (handoff)
        │
        ▼
     DevCrew (product engineering)
```

## Components

### Agents (one container each)

| Agent | Role | Port |
|-------|------|------|
| `research-lead` | Research questions, hypotheses, synthesis, handoff | 8751 |
| `research-engineer` | Experiments, data collection, analysis scripts | 8752 |
| `evaluation` | Metrics, auto-eval, human grading protocols | 8753 |

Each agent has:
- Its own Hermes runtime
- `SOUL.md` (identity + discipline)
- Role-specific skills
- Webhook door (`POST /webhooks/inbox`)

### Shared infrastructure

- **shared-memory** — Redis (message bus + shared state)
- **workspace/** — bind-mounted shared directory for experiments, temporary data, reports

### Entry point

Same pattern as DevCrew: `crew-send.py` signs and POSTs messages to any agent's door.

## Communication

- Human → agent: via `crew-send.py`
- Agent ↔ agent: via webhook doors (container DNS) or Redis bus events
- Discussion of substance: preferably in structured artifacts (hypotheses.md, reports) rather than only chat

## Separation of concerns

| Layer | What lives there |
|-------|------------------|
| Foundation (this repo) | Roles, SOULs, skills, factory rules, communication protocol |
| Instance config | Secrets, tokens, door registry (gitignored) |
| Research work | `workspace/<topic>/` — temporary data, notebooks, reports (usually gitignored or separate) |

Project/research work never mixes into the foundation.

## Key differences from DevCrew

| Aspect | DevCrew | LabCrew |
|--------|---------|---------|
| Primary mode | Spec-first | Hypothesis-first |
| Main artifact | Working code + PRs | Research Package |
| Environment focus | dev-env / staging-env | Temporary experiment space |
| Success criteria | Spec compliance + tests | Hypothesis support + evaluation quality |
| Downstream | Production product | Handoff to DevCrew |

## Open questions (to resolve later)

- Exact message schema for research events on the bus
- How formal the planning gate should be in research mode
- Whether we need a fourth agent (Data/Infra) in v1
- Experiment tracking tool choice (simple markdown vs MLflow-like)
