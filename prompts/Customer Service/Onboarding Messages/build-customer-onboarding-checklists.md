# Customer Onboarding Checklist Builder

## 簡介

The Customer Onboarding Checklist Builder is a free AI prompt that creates a phased 30-day customer journey designed to transform confused new users into confident power users while addressing the specific reasons customers drop off early. This customer onboarding prompt for ChatGPT, Claude, Gemini, and Grok takes your product description, customer goals, core features, and common churn reasons, then outputs a three-phase checklist: Day 1 focuses on immediate setup and quick wins that build early confidence, Days 2–7 introduce the core features that deliver primary value without overwhelming, and Days 8–30 expand into advanced capabilities, integrations, and community touchpoints that deepen long-term engagement. Each task includes a one-line motivation that explains why completing it matters, turning a static to-do list into a value-driven journey. Product managers, customer success teams, and SaaS founders use it to standardize onboarding, reduce time-to-value, and systematically address the friction points that cause users to abandon a product in the first month. ● Structures onboarding into three distinct phases tied to psychological momentum: quick wins on Day 1, core value in the first week, and advanced engagement through Day 30. ● Requires you to input common drop-off reasons so the prompt explicitly designs Phase 1 tasks that counteract each churn risk. ● Outputs each task with an actionable title and a one-line impact statement that shows the customer why it matters, not just what to do. ● Focuses on specific, immediately actionable items and filters out vague or optional tasks that dilute focus. ## Prompt

```
## Role

You are an expert onboarding specialist with a decade of experience reducing early churn by designing structured customer journeys that transform first-time users into confident power users.

## Task

Create a comprehensive 30-day onboarding checklist that eliminates overwhelm, builds momentum through quick wins, and guides new customers to meaningful success. Structure the checklist in three distinct phases:

- **Phase 1 (Day 1)**: Immediate setup tasks that create quick wins and early confidence
- **Phase 2 (Days 2–7)**: Core features that deliver primary value without distraction
- **Phase 3 (Days 8–30)**: Advanced capabilities, integrations, and community connection that deepen engagement

For each task, include a one-line explanation that motivates the customer by showing why completing it matters to their success—don't just list actions, sell the value.

## Context

**Product or service**: {{product-description}}

**Customer's main goal**: {{customer-goal}}

**Most essential features** (top 3–5): {{core-features}}

**Common early drop-off reasons**: {{churn-reasons}}

Infer the product's core value proposition from the description above and reinforce it throughout the checklist. Design at least one Phase 1 task that directly counteracts each early drop-off reason listed.

## Output

Format the checklist with clear headings for each phase (Day 1, Days 2–7, Days 8–30). Present each task as:

- **[Actionable task]** – *Brief one-line explanation of its impact*

Ensure every item is specific, immediately actionable, and avoids vague or "nice to have" tasks.
```

## 用法 / Usage
- 必填變數 / Variables: {{churn-reasons}}、{{core-features}}、{{customer-goal}}、{{product-description}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Customer Onboarding Checklist Builder is a free AI prompt that creates a phased 30-day customer journey de…
