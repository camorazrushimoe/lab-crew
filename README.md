# Lab Crew — research & experimentation factory

A portable team of isolated agents (Docker containers) focused on **hypothesis-driven research** before product development.

LabCrew lives **before** [DevCrew](https://github.com/camorazrushimoe/dev-crew).  
Its job is to turn fuzzy business ideas into validated understanding, evaluation designs, and clear handoff packages that DevCrew can implement.

## The team (v0)

| Container | Role | Door (webhook) |
|-----------|------|----------------|
| `research-lead` | Formulates research questions & hypotheses, tracks experiments, writes research reports & handoff specs | `:8751` |
| `research-engineer` | Executes experiments: quick parsers, data collection, scripts, baseline analysis | `:8752` |
| `evaluation` | Designs and runs evaluation (auto-eval, human grading protocols, metrics, reproducibility) | `:8753` |

**Infrastructure**

| Container | Purpose |
|-----------|---------|
| `shared-memory` | Redis message bus + shared state |

## Core idea

DevCrew builds software **spec-first**.  
LabCrew works **hypothesis-first**.

Typical flow:

1. Manager / business brings a fuzzy idea  
   (“Want market intelligence for games from Steam + community signals”  
   or “Want an agentic loop with solid evaluation”).
2. LabCrew runs a research cycle:
   - formulate hypotheses
   - design cheap experiments
   - collect just enough data (often temporary / local)
   - measure & evaluate
   - decide what is real vs noise
3. Output = **Research Package** that can be handed to DevCrew:
   - validated / rejected hypotheses
   - data sources & collection approach
   - evaluation design
   - recommended metrics
   - draft product requirements / OpenSpec sketch

## High-level workflow

```text
Idea / Research Brief
        ↓
Research Lead → Research Questions + Hypotheses
        ↓
Research Engineer → Experiments + Data Collection (quick & dirty)
        ↓
Evaluation Specialist → Metrics, auto-eval, human grading design
        ↓
Joint review → Research Report + Handoff Package
        ↓
(optional) → DevCrew receives clean input and builds the product
```

Key principle: **cheap experiments first**.  
No production databases, vector stores, or full pipelines until a hypothesis is worth the investment.

## What LabCrew produces (artifacts)

| Artifact | Owner | Purpose |
|----------|-------|---------|
| `hypotheses.md` / experiment log | research-lead | Living list of hypotheses + status |
| Experiment scripts / notebooks | research-engineer | Reproducible (enough) experiments |
| Evaluation design | evaluation | How we will measure success |
| Research Report | research-lead + team | Final findings, confidence, recommendations |
| Handoff Package | research-lead | Ready-to-use input for DevCrew (data sources, metrics, draft requirements) |

## Relationship to DevCrew

- LabCrew answers: *“Is this idea real? How do we measure it? What data do we actually need?”*
- DevCrew answers: *“How do we build a reliable product around this?”*

LabCrew should never try to become a product engineering team.  
When the research is solid, it hands off and steps back.

## Foundation docs & specs

| Document | Purpose |
|----------|---------|
| [FACTORY-STANDARD.md](crew/FACTORY-STANDARD.md) | Golden rules |
| [docs/architecture.md](docs/architecture.md) | Architecture overview |
| [docs/workflow.md](docs/workflow.md) | Research cycle & artifact layout |
| [docs/skills-overview.md](docs/skills-overview.md) | Skills per role |
| [docs/examples/market-intelligence-cycle.md](docs/examples/market-intelligence-cycle.md) | Worked example of a full research cycle |
| `openspec/specs/` | Capability specs (`agent-roles`, `research-cycle`, `artifacts`, `handoff`) |

## Project layout

```
agents/
  research-lead/
  research-engineer/
  evaluation/
crew/
  FACTORY-STANDARD.md
openspec/
  config.yaml
  specs/
docs/
  examples/
workspace/               # temporary experiment data & notebooks (gitignored)
```

## Status

v0.2 — foundation specification largely in place.  
Roles, SOULs, core capability specs, main skills and a concrete Market Intelligence example cycle are drafted.  
Next: remaining skills, then implementation (compose, doors, bus) when you are ready to deploy and try it on a real project.

---

See also: [DevCrew](https://github.com/camorazrushimoe/dev-crew) — the product engineering factory that receives LabCrew’s handoff packages.
