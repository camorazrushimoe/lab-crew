# Skills Overview (v0)

This document lists the intended skills for each role.  
Skills will be implemented as `SKILL.md` files under each agent's `skills/` directory (same pattern as DevCrew).

## research-lead

| Skill | Purpose |
|-------|---------|
| `hypothesis-crafting` | Turn fuzzy ideas into sharp, testable hypotheses with success criteria |
| `research-briefing` | Write clear experiment briefs for Research Engineer |
| `synthesis` | Produce Research Reports from experiment results |
| `handoff` | Package findings into a form DevCrew can act on |
| `research-tracking` | Maintain hypotheses log and experiment status |

## research-engineer

| Skill | Purpose |
|-------|---------|
| `quick-parsing` | Lightweight parsers for common sources (web, APIs, files, Steam-like data) |
| `experiment-design` | Design the cheapest viable experiment for a hypothesis |
| `data-collection` | Collect and organize temporary datasets |
| `exploratory-analysis` | Basic EDA, tables, simple stats, visualizations |
| `reproducible-notes` | Leave enough scripts + notes for others to audit/re-run |

## evaluation

| Skill | Purpose |
|-------|---------|
| `metric-design` | Choose and define metrics that match the research question |
| `auto-eval` | Design and implement automatic evaluation pipelines |
| `human-grading` | Design clear human grading protocols (guidelines, examples, checks) |
| `evaluation-critique` | Find leakage, cherry-picking, non-reproducibility and other evaluation risks |
| `eval-reporting` | Write clear evaluation sections for the Research Report |

## Shared / cross-cutting (later)

- `research-communication` — how agents talk about experiments without losing context
- `workspace-hygiene` — conventions for naming, cleanup of temporary data

These lists are starting points. We will refine them as we run real research cycles.
