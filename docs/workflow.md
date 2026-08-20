# LabCrew Workflow

## Input

- Research Brief from manager / business
- Or a fuzzy product idea that needs validation before engineering

Example briefs:
- “We want market intelligence for games. Can community signals (reviews, discussions, price changes) predict anything useful?”
- “We want to build an agentic loop. How should we evaluate it? What data do we need for auto-eval and human grading?”

## Output

A **Research Package** containing some or all of:

1. Hypotheses log (what we tested, status, confidence)
2. Data sources map (what we collected, how, limitations)
3. Experiment artifacts (scripts, notebooks, key results)
4. Evaluation design (metrics, auto-eval approach, human grading protocol)
5. Research Report (findings + recommendations)
6. Handoff note for DevCrew (if the idea is worth productizing)

## Roles in the cycle

### Research Lead
- Owns the research questions and hypothesis list
- Prioritizes what to test
- Runs the synthesis and final report
- Produces the handoff package

### Research Engineer
- Turns hypotheses into concrete experiments
- Writes quick parsers and collection scripts
- Runs analysis and produces intermediate results
- Keeps experiments lightweight and reproducible enough

### Evaluation Specialist
- Designs how we will know if a hypothesis is supported
- Builds auto-evaluation where possible
- Defines human grading protocols when needed
- Guards against common research pitfalls (leakage, cherry-picking, non-reproducible metrics)

## Artifact conventions (v0)

Suggested structure inside `workspace/<research-topic>/`:

```
workspace/<topic>/
  BRIEF.md
  hypotheses.md
  experiments/
  data/                 # temporary, usually gitignored
  evaluation/
  report.md
  handoff/              # package for DevCrew
```

Exact conventions will be refined as we implement the agents.
