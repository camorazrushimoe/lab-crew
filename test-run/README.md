# Test Run: Customer Support Chat Analysis

A complete end-to-end test for the Lab Crew factory. Use this to verify the factory works correctly, or as a reference for designing your own briefs.

---

## What This Test Does

A Product Manager brings **1,000 customer support chats** and **4 rough hypotheses** about what's wrong with support. Lab Crew runs the full research cycle:

```
BRIEF → Hypotheses → Experiment Design → Data + Execution → Evaluation → Synthesis → Handoff
```

The output is a **Research Report** with evidence-backed verdicts on each hypothesis.

---

## Data

- **Source:** `test-run/data/abcd_1000_pool.jsonl` — 1,000 real support chat transcripts
- **Format:** JSONL, each line = one chat with `chat_id`, `tenant`, `n_turns`, `turns[]`
- **Tenants:** 10 types — `single_item_query`, `purchase_dispute`, `order_issue`, `shipping_issue`, `product_defect`, `troubleshoot_site`, `manage_account`, `subscription_inquiry`, `account_access`, `storewide_query`
- **Size:** 1.7 MB

---

## Hypotheses Under Test

| # | Hypothesis | Type of Analysis |
|---|-----------|-----------------|
| 1 | Top Problems and Load (80/20 rule) | Clustering + frequency ranking |
| 2 | Invisible Features / Hidden Expectations | Intent extraction + clustering |
| 3 | Self-Service Potential | Classification (auto-solvable vs. human-needed) |
| 4 | Expectation Gaps | Phrase pattern search + correlation with tenant/n_turns |

Full brief: [`test-run/BRIEF.md`](BRIEF.md)

---

## How to Run

### Prerequisites

1. Factory is running (`docker compose up -d` from repo root)
2. Agents are reachable:
   - Research Lead: `http://localhost:8651`
   - Research Engineer: `http://localhost:8652`
   - Evaluation Specialist: `http://localhost:8653`

### Send the Brief

Send the brief to the Research Lead via webhook:

```bash
# Read the brief and send it
BRIEF=$(cat test-run/BRIEF.md)
curl -X POST http://localhost:8651/webhooks/inbox \
  -H "Content-Type: application/json" \
  -d "{\"message\": \"$BRIEF\"}"
```

Or send it in chunks if the full brief is too long for one message.

### Expected Output

After processing, the workspace will contain:

```
workspace/support-chat-analysis/
  hypotheses.md          ← Refined, testable hypotheses
  experiments/           ← Experiment scripts & data
  evaluation/            ← Evaluation results
  report.md              ← Final Research Report
  handoff/               ← Dev handoff package (if worth building)
```

### Expected Duration

On a local 14B model (Qwen 2.5), the full cycle across all 4 hypotheses may take **30–90 minutes** depending on hardware. Each agent processes sequentially: Research Lead → Engineer → Evaluation → Lead (synthesis).

---

## Success Criteria

The factory is working correctly if the output contains:

- [ ] All 4 hypotheses are addressed with explicit verdicts
- [ ] Verdicts are backed by evidence from the data (numbers, not opinions)
- [ ] Caveats and limitations are documented
- [ ] A synthesis report ties findings together
- [ ] Artifacts are in the expected workspace layout

---

## Troubleshooting

| Symptom | Check |
|---------|-------|
| No response from agent | `docker ps` — all three running? |
| Agent returns error | `docker logs lab-crew-research-lead` — LLM reachable? |
| Slow processing | 14B model on CPU — normal. Wait. |
| Webhook connection refused | Agents take ~10s to start after `docker compose up -d` |

---

## Reuse

To run a different brief with the same structure:

1. Replace `test-run/data/` with your own data
2. Edit `test-run/BRIEF.md` with your own context and hypotheses
3. Send the new brief to Research Lead