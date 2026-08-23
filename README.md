# Lab Crew — research & experimentation factory

LabCrew is a small team of AI agents that turns fuzzy product ideas into **validated research** before anyone builds a product.

It lives **before** product implementation ([DevCrew](https://github.com/camorazrushimoe/dev-crew) / Dev instances under Office).

- Dev builds software from specs.
- Lab answers: *Is this idea real? What should we measure? What data do we actually need?*

When research is solid, LabCrew produces a **Research Package** and hands it off. It does not build the product itself.

> **Agent Office:** this repo is also a **team template** under [Agent Office](https://github.com/camorazrushimoe/agent-office).  
> Multiple Lab instances can be composed from pinned refs of this template.  
> See [docs/office-template.md](docs/office-template.md) for the Office-compatible contract (shared bus, lifecycle, handoff via Office).

---

## How the factory works (the cycle)

This is the main loop. Everything LabCrew does fits into it.

```text
1. BRIEF
   Manager / business brings a fuzzy idea.
   Example: “We want market intelligence for games from Steam and community signals.”

2. HYPOTHESES
   Research Lead turns the idea into explicit, testable hypotheses
   with success and failure criteria.

3. EXPERIMENT DESIGN
   Research Engineer designs the cheapest way to test a hypothesis.
   Evaluation Specialist defines how success will be measured.

4. DATA + EXECUTION
   Research Engineer collects just enough data (often temporary)
   and runs the experiment. No production infrastructure yet.

5. EVALUATION
   Evaluation Specialist scores the results (auto-eval and/or human grading),
   checks for leakage, bias and other traps, and reports a verdict.

6. SYNTHESIS
   Research Lead writes the Research Report:
   what was supported, rejected, or still unclear — with confidence and caveats.

7. HANDOFF (optional)
   If the idea is worth building, Research Lead packages a clean handoff
   for Dev (via Agent Office when composed): data sources, metrics, draft requirements, open questions.
   If not — the cycle stops or goes back to new hypotheses.
```

**Golden rules of the cycle**

- No hypothesis → no experiment
- Cheap experiments first
- Evaluation is not optional
- Handoff is a first-class output (not an afterthought)

A concrete walkthrough of this cycle is here:  
[docs/examples/market-intelligence-cycle.md](docs/examples/market-intelligence-cycle.md)

---

## The workers

Three agents. Each has a clear specialty. They collaborate through briefs, shared artifacts, and the message bus.

### 1. Research Lead

**Specialty:** thinking and structure.

Turns messy ideas into clear research questions and hypotheses. Owns the overall research direction, tracks status, writes the final report, and decides whether something is ready for product work.

**What this agent does well**
- Rewrite a vague idea into sharp, falsifiable hypotheses
- Prioritize what is worth testing now vs later
- Write experiment briefs for the engineer
- Keep the hypotheses log up to date
- Synthesize results into a Research Report
- Produce a clean handoff package for Dev / Office

**What this agent does *not* do**
- Write production code or production pipelines
- Own long-term infrastructure
- Run the final product after launch

**Core skills:** `hypothesis-crafting`, `research-briefing`, `research-tracking`, `synthesis`, `handoff`

---

### 2. Research Engineer

**Specialty:** getting evidence fast.

Takes a hypothesis and turns it into a cheap experiment: parsers, temporary data, scripts, basic analysis. Optimizes for speed and clarity, not for production systems.

**What this agent does well**
- Design the cheapest viable experiment for a hypothesis
- Write lightweight parsers (web, APIs, files, store pages, etc.)
- Collect and organize temporary datasets with provenance notes
- Run exploratory analysis (tables, distributions, simple comparisons)
- Leave scripts and notes that others can re-run or audit

**What this agent does *not* do**
- Build production data platforms or long-lived services
- Jump to complex models before basic evidence exists
- Skip measurement design — coordinates with Evaluation Specialist

**Core skills:** `experiment-design`, `quick-parsing`, `data-collection`, `exploratory-analysis`, `reproducible-notes`

---

### 3. Evaluation Specialist

**Specialty:** honest measurement.

Makes sure the team actually knows whether a hypothesis is supported. Designs metrics, auto-evaluation, human grading protocols, and actively looks for ways results could be misleading.

**What this agent does well**
- Choose metrics that match the research question (not just easy numbers)
- Design and implement automatic evaluation
- Design clear human grading protocols (definitions, examples, agreement checks)
- Critique evaluation for leakage, cherry-picking, bias, tiny samples
- Write evaluation sections that can go straight into the Research Report

**What this agent does *not* do**
- Own the overall research direction (that is Research Lead)
- Accept “looks good” as a result
- Build production monitoring systems

**Core skills:** `metric-design`, `auto-eval`, `human-grading`, `evaluation-critique`, `eval-reporting`

---

## What the factory produces

| Artifact | Owner | Purpose |
|----------|-------|---------|
| `hypotheses.md` | Research Lead | Living list of hypotheses + status |
| Experiment scripts / data | Research Engineer | Evidence for/against hypotheses |
| Evaluation design + results | Evaluation Specialist | How success was measured |
| Research Report | Research Lead | Findings, confidence, recommendations |
| Handoff package | Research Lead | Input for Dev / Office (if the idea is worth building) |

Typical layout inside a research topic:

```text
workspace/<topic>/
  BRIEF.md
  hypotheses.md
  experiments/
  data/
  evaluation/
  report.md
  handoff/
```

---

## Relationship to Dev and Agent Office

| Question | Who answers |
|----------|-------------|
| Is this idea real? What should we measure? | **Lab** |
| How do we build a reliable product around it? | **Dev** (routed via **Agent Office** when composed) |

Lab stops at understanding.  
Dev starts when understanding is good enough to build.

---

## Foundation docs

| Document | Purpose |
|----------|---------|
| [FACTORY-STANDARD.md](crew/FACTORY-STANDARD.md) | Golden rules |
| [docs/architecture.md](docs/architecture.md) | Architecture |
| [docs/workflow.md](docs/workflow.md) | Cycle & artifact conventions |
| [docs/skills-overview.md](docs/skills-overview.md) | Full skills list |
| [docs/examples/market-intelligence-cycle.md](docs/examples/market-intelligence-cycle.md) | Worked example |
| [docs/office-template.md](docs/office-template.md) | Agent Office template contract |
| `openspec/specs/` | Capability specs |

---

## Status

v0.3 — foundation specification complete for the research cycle and all core skills.  
Office template contract documented; Docker runtime implementation should default to Office-attach capability.

---

See also: [Agent Office](https://github.com/camorazrushimoe/agent-office) · [DevCrew](https://github.com/camorazrushimoe/dev-crew)
