# Trigger-Based Email Campaign Strategy Builder

## 簡介

The Trigger-Based Email Campaign Strategy Builder is a free AI prompt that designs complete automated email sequences for marketers and growth teams looking to nurture leads through behavior-driven campaigns. This trigger-based email prompt for ChatGPT walks you through six critical dimensions: mapping customer actions to trigger events, architecting multi-step sequences with precise cadence, crafting personalized subject lines and body copy for each audience segment, setting timing logic and delivery windows, defining CTAs and conditional follow-up paths, and establishing performance metrics with A/B test recommendations. The output is a numbered, implementation-ready plan that works with standard email automation platforms like HubSpot, ActiveCampaign, or Mailchimp. It runs on ChatGPT, Claude, Gemini, and Grok, and accepts three variables: trigger actions, sales context, and target audience. Use this prompt when you need to transform manual email workflows into scalable, behavior-driven automation that responds to sign-ups, cart abandonment, demo requests, content downloads, or any customer touchpoint. ● Maps specific customer actions to trigger events and sequence activation logic ● Defines email cadence, timing intervals, and dependency flows (Day 0, Day 3, Day 7) ● Provides draft themes, personalization tokens, and dynamic content recommendations ● Outlines conditional paths, CTAs, and handoff rules for sales follow-up ## Prompt

```
## Role
You are an expert email marketing strategist specializing in trigger-based campaigns that nurture leads and drive conversions.

## Task
Design a comprehensive trigger-based email campaign strategy delivered as a numbered, step-by-step plan. Cover:

1. **Trigger Event Mapping** – Identify which customer actions activate each sequence
2. **Email Sequence Architecture** – Number of emails, cadence, and dependency flow
3. **Message Content & Personalization** – Subject lines, body copy, and dynamic elements tailored to audience segments
4. **Timing & Delivery Logic** – Delays between emails and optimal send windows
5. **Follow-Up & Conversion Actions** – CTAs, conditional paths, and handoff to sales
6. **Performance Optimization** – Key metrics to track and A/B test recommendations

## Context
**Customer Journey & Triggers:**  
{{trigger-actions}}

**Sales Process & Goals:**  
{{sales-context}}

**Target Audience:**  
{{audience}}

## Output
Deliver a numbered list with clear section headings. Each section should provide actionable detail: specific trigger logic, draft email themes, timing intervals (e.g., "Day 0, Day 3, Day 7"), and next-step recommendations. Ensure the strategy is ready to implement in standard email automation platforms.
```

## 用法 / Usage
- 必填變數 / Variables: {{audience}}、{{sales-context}}、{{trigger-actions}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Trigger-Based Email Campaign Strategy Builder is a free AI prompt that designs complete automated email se…
