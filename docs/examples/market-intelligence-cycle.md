# Example Research Cycle: Market Intelligence for Games

This is a worked example of how LabCrew should run a research cycle.  
It is intentionally lightweight and hypothesis-first.

---

## 0. Research Brief (from manager)

> We want a market intelligence product for games.  
> Idea: use public signals (Steam pages, reviews, price changes, community discussion) to understand trends and possibly predict interesting movements.  
> Before building anything serious, we need to know what actually works.

---

## 1. Research Lead — Hypotheses

Research Lead rewrites the fuzzy idea into testable hypotheses.

### H1 — Review volume reacts to price changes
**Statement:** When a game’s price drops significantly, review volume increases within 7 days.  
**Success criteria:** Median review count in the 7 days after a ≥20% price drop is meaningfully higher than the 7 days before.  
**Failure criteria:** No consistent increase across a sample of games.  
**Cheapest first test:** Take 30–50 recent price-drop events and compare review counts before/after.  
**Status:** proposed

### H2 — Negative review spikes precede visible rating damage
**Statement:** A short spike in negative reviews appears before the overall rating moves noticeably.  
**Success criteria:** Detectable negative-review burst occurs ≥3 days before a ≥0.1 drop in overall score (on a 0–10 style scale).  
**Failure criteria:** Rating moves without a prior negative spike, or spikes are mostly noise.  
**Cheapest first test:** Manual + scripted inspection of 20 games that had recent rating drops.  
**Status:** proposed

### H3 — Community discussion volume is a leading indicator of sales interest
**Statement:** (Deferred — too expensive / too vague for first cycle.)  
**Status:** parked

Research Lead prioritizes **H1** as the first experiment.

---

## 2. Research Lead → Research Engineer (Brief)

```markdown
## Experiment Brief: price-drop-review-volume

**Hypothesis:** H1 — Review volume reacts to price changes
**Goal:** Check whether review volume rises after significant price drops.
**Success signal:** Clear increase in median daily reviews after ≥20% price drops.
**Failure signal:** No consistent pattern across ~30–50 events.
**Constraints:**
- Temporary data only
- No production DB
- Prefer public Steam (or similar) pages / simple APIs
- Max effort: 1–2 focused days of collection + analysis
**Out of scope:** Full historical crawler, real-time monitoring, ML models
**Report back when:** First sample analyzed and summary table ready
```

---

## 3. Research Engineer — Experiment design & execution

### Experiment plan
- Collect a list of games that had recent price drops (≥20%).
- For each event: record date of drop, price before/after, daily review counts for 7 days before and 7 days after.
- Produce a simple before/after comparison table + distribution of changes.

### What gets produced
- `experiments/price-drop-review-volume/` scripts
- `data/price-drop-sample/` (temporary)
- Intermediate summary: median change, % of events with increase, obvious outliers

---

## 4. Evaluation Specialist — Measurement

### Metric
- **Primary:** % of price-drop events where post-7d average daily reviews > pre-7d average daily reviews
- **Secondary:** median relative increase
- **Sample size note:** report confidence only with explicit sample size and caveats

### Critique points
- Selection bias (only games we could easily find price history for)
- Confounding (major updates / launches happening at the same time as price drops)
- Review bombs vs organic volume

Evaluation Specialist writes a short critique and confirms whether the metric is honest enough for a first decision.

---

## 5. Synthesis (Research Lead)

### Possible outcomes (examples)

**Supported (with caveats)**  
H1 shows a consistent pattern on the sample. Worth deeper data collection and possibly a product feature that watches price→review reactions.

**Rejected / weak**  
No reliable pattern. Do not build product features around this signal yet.

**Inconclusive**  
Signal exists only on certain genres / price ranges. Needs a second, better-sampled experiment.

Research Lead updates `hypotheses.md` and writes `report.md`.

---

## 6. Handoff decision

If H1 is strong enough:

`handoff/` contains:
- What was validated
- Recommended data sources and fields
- Evaluation metric to carry forward
- Draft requirement: “System should detect significant price drops and track subsequent review volume changes”
- Open questions (confounders, genre differences, etc.)

If not strong enough → more research or stop. No fake handoff.

---

## What this example demonstrates

- Fuzzy idea → explicit hypotheses
- One cheap experiment instead of a platform
- Evaluation is designed, not improvised after the fact
- Clear stop / continue / handoff decision
- LabCrew does not build the product; it produces understanding
