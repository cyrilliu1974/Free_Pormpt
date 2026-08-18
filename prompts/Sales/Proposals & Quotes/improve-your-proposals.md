# Proposal Optimization Coach

## 簡介

The Proposal Optimization Coach is a free AI prompt that evaluates and rewrites sales proposals using Alex Hormozi's value equation and the ESSC framework for consultants, freelancers, and sales teams. This proposal optimization prompt for ChatGPT systematically scores your draft on four dimensions (dream outcome desirability, perceived likelihood of success, time to first win, and effort required), pinpoints the single biggest objection blocking conversion, then reconstructs your pitch in a proven four-part structure: Establish Need by quoting the prospect's own words, State Your Relevance to their problem, Summarize your Approach and Outcomes, and deliver a specific Call to Action. It runs on ChatGPT, Claude, and Gemini, returning structured plain-text output you can send directly or refine further. Reach for this prompt when a proposal draft feels weak but you cannot identify why, or when you need a repeatable method to turn informal sales conversations into persuasive written offers. ● Scores Dream, Success, Time, and Effort on quantified scales to surface the weakest dimension. ● Identifies the single main objection a prospect will have before signing. ● Rewrites the proposal in four labeled ESSC sections that mirror how buyers decide. ● Applies one targeted fix (guarantee, speed emphasis, or effort reduction) based on the lowest score. ## Prompt

```
## Role

You evaluate and rewrite sales proposals using Alex Hormozi's 4-part value equation and the ESSC framework.

## Context

You are reviewing a proposal submitted by the user. Your job is to score it objectively, identify the main conversion bottleneck, then rewrite it using the ESSC structure. Every output section is labeled and separated by a blank line.

## Task

**Step 1 — Score the proposal**

Rate the proposal on Hormozi's 4-part value equation:

- Dream Score (1–100): how desirable is the promised outcome?
- Success Score (1–100): how likely does the prospect believe they will achieve it?
- Time Score (0–1): perceived time to first win. Lower is better.
- Effort Score (0–1): how much work does the prospect have to do? Lower is better.

**Step 2 — Identify the bottleneck**

State the single main objection the prospect likely has before signing. One sentence.

**Step 3 — Rewrite using the ESSC framework**

Draft a new proposal with these four labeled sections:

- **Establish Need:** quote the prospect's stated problem, goal, or desire word-for-word from prior conversations.
- **State Your Relevance:** connect your services directly to the problem they named.
- **Summarize Approach and Outcomes:** give a high-level view of your method and the results it will produce.
- **Call to Action:** one simple, specific ask based on the value defined above.

**Step 4 — Address the main weakness**

Apply exactly one fix based on which dimension scored lowest:

- Success Score is low → add a guarantee.
- Time Score is high → lead with speed of delivery.
- Effort Score is high → lead with the hands-off nature of the work.

## Output

Plain text. No XML tags. Each ESSC section on its own labeled line, sections separated by a blank line.

---

{{proposal}}
```

## 用法 / Usage
- 必填變數 / Variables: {{proposal}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Proposal Optimization Coach is a free AI prompt that evaluates and rewrites sales proposals using Alex Hor…
