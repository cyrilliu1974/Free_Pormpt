# Sales Follow-Up Schedule Builder for Lead Nurturing

## 簡介

The Sales Follow-Up Schedule Builder for Lead Nurturing is a free AI prompt that creates structured follow-up schedules to systematically nurture leads and improve conversion rates for sales and marketing teams. This follow-up schedule prompt for ChatGPT takes your product or service details, lead information (including engagement levels and funnel stages), and typical sales cycle length, then generates a markdown table organizing every lead by priority, current stage, last contact date, next contact date, and recommended follow-up method. It runs on ChatGPT, Claude, Gemini, and Grok, producing actionable schedules that help sales professionals maintain consistent engagement across their pipeline. Real use cases include managing B2B sales cycles with multiple touchpoints, coordinating outreach for SaaS trial users, and ensuring high-value prospects receive timely, personalized follow-up at each stage of their buyer journey. This prompt is for sales representatives, account executives, and marketing teams who need to track multiple leads simultaneously and want a data-driven system for timing their outreach based on engagement signals and sales complexity. ● Categorizes leads by priority level (High/Medium/Low) and current funnel stage (Awareness/Consideration/Decision) to focus effort where it matters most ● Calculates optimal next-contact dates based on engagement history, sales cycle length, and lead behavior patterns ● Assigns specific follow-up methods (email, call, demo, proposal review) matched to each lead's stage and needs ● Provides personalized notes on value propositions, pain points to address, and specific touchpoints to reference in outreach ## Prompt

```
## Role
You are a sales and marketing strategist specializing in lead nurturing and conversion optimization.

## Task
Develop a strategic follow-up schedule that organizes leads by priority and funnel stage, assigns appropriate contact intervals based on engagement level and sales complexity, and provides personalized outreach strategies for each lead.

## Context
**Product/Service:** {{product-service}}

**Lead Information:** {{lead-details}}
(Include for each lead: name, current stage, engagement level, last contact date, and any relevant notes about their situation or interests)

**Sales Cycle Length:** {{sales-cycle-length}}

## Output
Create a markdown table with these columns: Lead Name | Priority | Funnel Stage | Last Contact | Next Contact | Follow-Up Method | Notes

For each lead:
- Assign priority (High/Medium/Low) based on engagement and fit
- Identify current funnel stage (Awareness/Consideration/Decision)
- Calculate next contact date using appropriate intervals for their stage and engagement
- Specify the follow-up method (email, call, demo, proposal review, etc.)
- Include personalized notes on value propositions, pain points to address, or specific touchpoints to reference

Provide at least 5 complete entries that demonstrate varied lead scenarios, stages, and follow-up strategies. Include a brief summary below the table explaining the logic behind interval timing and prioritization for this sales cycle.
```

## 用法 / Usage
- 必填變數 / Variables: {{lead-details}}、{{product-service}}、{{sales-cycle-length}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Sales Follow-Up Schedule Builder for Lead Nurturing is a free AI prompt that creates structured follow-up …
