# BRIEF — Customer Support Chat Analysis

> **From:** Product Manager, E-commerce Platform
> **To:** Lab Crew (Research Lead)

---

## Context

We run a customer support operation for an online retail platform. We have **1,000 real support chat transcripts** between customers and support agents. Each chat covers one support interaction — questions, complaints, disputes, simple queries.

I have lots of ideas about what's broken in support, but I need someone to **actually look at the data** and tell me which ideas hold water and which don't.

I don't need perfect answers — I need honest, evidence-backed answers.

---

## Data

**File:** `test-run/data/abcd_1000_pool.jsonl` (1,000 chats, JSONL format)

Each record has:
- `chat_id` — unique identifier
- `tenant` — category of the issue (e.g. `single_item_query`, `purchase_dispute`, `order_issue`, `shipping_issue`, `product_defect`, etc.)
- `unlock` / `unlock_guideline` — fine-grained issue type
- `n_turns` — total number of turns in the conversation
- `turns` — array of messages, each with `speaker` (`agent`, `customer`, or `action`) and `text`

---

## My Ideas (hypotheses)

These are rough. Some might be nonsense. You tell me.

### Hypothesis 1: Top Problems and Their Load

> "20% of issue types generate 80% of support load. If we fix those, we cut tickets in half."

I want to know: **which types of issues dominate?** Cluster the chats by what they're actually about (not just the `tenant` label — those are shallow). Then rank by frequency. Are there a small number of clusters that drive most of the volume?

If yes — what are those clusters? What are customers actually saying in them?

### Hypothesis 2: Invisible Features / Hidden Expectations

> "Users regularly describe workflows or features that don't exist in the product — or exist but nobody can find them."

I want to know: what are customers **asking for** that we don't offer? Look for language like "I want to...", "why can't I...", "do you have...", "is there a way to...". Cluster these, rank by frequency and intensity of sentiment. 

Is there a pattern? A feature we keep getting asked about?

### Hypothesis 3: Self-Service Potential

> "A big chunk of these chats could have been resolved without a human agent — with better docs, in-app help, or an auto-response."

Look at the chats and classify them: **could this have been solved by a knowledge base article, an in-app tooltip, or a chatbot?** 

What percentage of chats fall into this category? Which `tenant` types are the most "auto-solvable"?

### Hypothesis 4: Expectation Gaps

> "Some negativity comes not from real bugs, but from users expecting the product to do X when it actually does Y."

Find chats where the customer expresses confusion or disappointment about product behavior — phrases like "I thought that...", "I expected...", "I assumed...", "it should...", "why doesn't it...".

Are these expectation gaps correlated with specific `tenant` types? Do they lead to longer conversations (higher `n_turns`)? Is this a real problem or just noise?

---

## What I Want From You

For **each hypothesis**, give me:

1. **Verdict:** Supported / Rejected / Needs more data — with confidence level
2. **Evidence:** What you found in the data (numbers, patterns, examples)
3. **Caveats:** What you couldn't check, what assumptions you made, what the data doesn't capture
4. **Recommendation:** Should we act on this, investigate further, or drop it?

Then a **synthesis** across all four: what's the single most impactful thing we should fix in support?

---

Go.