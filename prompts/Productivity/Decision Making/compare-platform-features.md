# Platform Comparison Decision Matrix Prompt

## 簡介

The Platform Comparison Decision Matrix Prompt is a free AI prompt that builds systematic side-by-side platform evaluations using weighted scoring to help teams and consultants choose the right software or service. This platform comparison prompt for ChatGPT takes your list of candidate platforms, priority features, and business context, then produces a structured decision matrix that assigns importance weights to each criterion, scores every platform's performance, and calculates objective totals to surface the strongest match. It runs on ChatGPT, Claude, Gemini, and Grok, and is designed for teams evaluating SaaS tools, CRMs, marketing automation systems, project management platforms, or any multi-option technology decision where clarity and objectivity matter. Reach for this prompt when you need to move beyond gut feeling and justify platform recommendations with measurable criteria - ideal for consultants, product managers, IT leaders, and procurement teams. ● Assigns 1–10 importance weights to features like automation, API access, scalability, pricing, and integrations based on your business priorities. ● Scores each platform's performance on every criterion, calculates weighted totals, and ranks options from strongest to weakest. ● Delivers a markdown comparison table and summary showing the top differentiators and key trade-offs between contenders. ● Surfaces hidden strengths and gaps across platforms, ensuring your final choice aligns with real requirements rather than marketing claims. ## Prompt

```
## Role
You are an expert decision analyst specializing in weighted comparison matrices and platform evaluation.

## Task
Create a systematic side-by-side comparison matrix that objectively scores multiple platforms against weighted criteria to identify the best option for the user's needs.

## Context
**Platforms under consideration:** {{platforms}}

**Priority features and requirements:** {{priority-features}}

**Business context:** {{business-context}}

## Method
1. Extract all essential features from the stated requirements
2. Assign importance weights (1-10 scale) to each feature based on the business context and stated priorities
3. Score each platform's performance on every feature (1-10 scale)
4. Calculate weighted scores (feature score × weight) for each platform
5. Sum totals to produce objective rankings
6. Provide brief justifications for each score

Focus on measurable capabilities including automation, data limits, API access, templates, mobile experience, pricing, integrations, UI quality, support, and scalability. Call out specific strengths and weaknesses that drive the recommendation.

## Output
Deliver your analysis as a comprehensive markdown comparison table:

**Weighted Decision Matrix:**

| Feature | Weight | [Platform 1] Score | [Platform 1] Weighted | [Platform 2] Score | [Platform 2] Weighted | ... |

Followed by a **Summary Ranking Table** showing:
- Total weighted scores for each platform (highest to lowest)
- Top 3 differentiating factors for the winner
- Key trade-offs between top contenders
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}}、{{platforms}}、{{priority-features}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Platform Comparison Decision Matrix Prompt is a free AI prompt that builds systematic side-by-side platfor…
