# Sales Negotiation Preparation Plan Generator

## 簡介

The Sales Negotiation Preparation Plan Generator is a free AI prompt that creates structured negotiation plans for sales professionals preparing for high-stakes client conversations. This sales negotiation prompt for ChatGPT produces a comprehensive three-column reference table covering client background research, anticipated objections, and specific counter-tactics aligned with your deal objectives. You provide the client context, your unique selling points, and negotiation goals; the prompt returns 5-7 detailed scenarios mapping key facts about the client's business priorities and decision-makers against likely objections - price resistance, timing concerns, competitive alternatives, risk aversion, capability questions - paired with concrete responses, value demonstrations, and closing techniques. Sales teams use it before enterprise deals, contract renewals, and partnership negotiations to walk into meetings with a structured playbook. It runs on ChatGPT, Claude, Gemini, and Grok. Reach for this prompt when you need to prepare for a complex B2B negotiation where multiple objections and decision-makers are in play. ● Maps client pain points, buying patterns, and decision-maker priorities into a single reference view ● Anticipates specific objection categories - price, timing, competition, risk, capability - with tailored responses ● Aligns negotiation tactics and concession strategies directly to your stated deal objectives ● Delivers 5-7 scenario rows detailed enough to reference during live negotiation sessions ## Prompt

```
## Role
You are an expert sales strategist preparing a client for high-stakes negotiations.

## Task
Create a comprehensive negotiation preparation plan structured as a three-column reference table. Research the client background, anticipate objections they will raise, and develop counter-tactics aligned with the negotiation goals.

## Context
**Client & Deal:**
{{client-and-deal}}
(Include: client name, product/service being sold, industry context)

**Your Position:**
{{unique-selling-points}}
(Your company's key differentiators and competitive advantages)

**Objectives:**
{{negotiation-goals}}
(What you need to achieve from this negotiation)

## Output
Present your preparation plan as a markdown table with three columns:

| Client Information | Potential Objections | Negotiation Tactics |
|-------------------|---------------------|--------------------|

Each row should provide:
- **Client Information**: Key facts about their business, priorities, pain points, decision-makers, and buying patterns
- **Potential Objections**: Specific concerns or pushback they are likely to raise (price, timing, competition, risk, capability)
- **Negotiation Tactics**: Concrete responses, value demonstrations, concession strategies, and closing techniques that address the objection and advance your goals

Include 5–7 rows covering the most critical negotiation scenarios. Make each cell detailed and actionable—specific enough to reference during live negotiation.
```

## 用法 / Usage
- 必填變數 / Variables: {{client-and-deal}}、{{negotiation-goals}}、{{unique-selling-points}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Sales Negotiation Preparation Plan Generator is a free AI prompt that creates structured negotiation plans…
