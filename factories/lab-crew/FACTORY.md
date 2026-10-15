---
name: Lab Crew
description: "Hypothesis-first research factory: turn fuzzy ideas into validated understanding and clean handoff packages for product engineering."
owner: AI/Run Mission / EPAM
authors:
  - "Sergey Ryabushko <sergey_ryabushko@epam.com>"
install_script: "pip install -r requirements.txt"
install_script_unix: "pip install -r requirements.txt"
sdlc_phase: Requirements & Analysis
support_level: Best Effort Support
project_deployments:
  - AI-Run
use_cases:
  - "Hypothesis-driven research: validate product ideas before building"
  - Research package handoff to product engineering
  - Multi-agent research workflows with evaluation
---

# Lab Crew — Research & Experimentation Factory

LabCrew is a small team of AI agents that turns fuzzy product ideas into **validated research** before anyone builds a product.

It lives **before** product implementation ([DevCrew](https://github.com/camorazrushimoe/dev-crew) / Dev instances under Office).

- Dev builds software from specs.
- Lab answers: *Is this idea real? What should we measure? What data do we actually need?*

When research is solid, LabCrew produces a **Research Package** and hands it off. It does not build the product itself.

> **Agent Office:** this repo is also a **team template** under [Agent Office](https://github.com/camorazrushimoe/agent-office).  
> Multiple Lab instances can be composed from pinned refs of this template.  
> See [docs/office-template.md](docs/office-template.md) for the Office-compatible contract (shared bus, lifecycle, handoff via Office).

## Agents

| Agent | Role | SDLC Phase |
|-------|------|------------|
| **Research Lead** | Turns fuzzy ideas into clear research questions, explicit hypotheses, and high-quality research packages | Requirements & Analysis |
| **Research Engineer** | Turns hypotheses into concrete, cheap experiments — collects data, runs analysis | Development |
| **Evaluation Specialist** | Designs and runs the measurement layer — makes sure the team knows whether a hypothesis is supported | Testing & QA |

## Skills (14)

The factory includes 14 reusable skills across research lifecycle: hypothesis-crafting, experiment-design, data-collection, quick-parsing, exploratory-analysis, reproducible-notes, metric-design, auto-eval, human-grading, evaluation-critique, eval-reporting, research-tracking, synthesis, and handoff.

## Golden rules

1. **No hypothesis → no experiment**  
   Every experiment must be tied to at least one explicit hypothesis.

2. **Cheap experiments first**  
   Prefer quick scripts, temporary data, and small samples over production infrastructure.

3. **Evaluation is not optional**  
   Every research cycle must define how success/failure will be measured.

4. **Handoff is a first-class output**  
   The final artifact is a Research Package that another team can act on without needing the original researchers.