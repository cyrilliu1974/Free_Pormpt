# Onboarding Progress Monitoring System Design Prompt

## 簡介

The Onboarding Progress Monitoring System Design Prompt is a free AI prompt that builds data-driven onboarding tracking frameworks for SaaS customer success teams. It transforms raw user behavior into actionable intelligence that prevents churn by distinguishing genuine progress signals from vanity metrics, detecting struggles before they trigger abandonment, and creating centralized customer intelligence accessible across your organization. This onboarding progress prompt for ChatGPT runs on ChatGPT, Claude, Gemini, and Grok, helping customer success architects design systems tailored to their product's typical onboarding duration, critical success milestones, current tracking tools, and known pain points. Reach for this prompt when silent abandonment plagues your onboarding journey and existing metrics fail to guide intervention. ● Creates milestone maps that measure customer-perceived value realization rather than arbitrary completion percentages, connecting progress signals to retention outcomes. ● Builds pain point detection frameworks that surface friction through hesitation patterns, backtracking behavior, help-seeking signals, and workflow slowdowns before customers abandon. ● Designs centralized intelligence hubs that consolidate quantitative tracking data, qualitative customer goals, stated pain points, preferences, and interaction history into coherent customer narratives. ● Establishes actionability frameworks linking specific data patterns to intervention triggers, personalized guidance sequences, and proactive support actions that improve outcomes. ## Prompt

```
## Role

You are an onboarding intelligence architect who designs systems that transform raw onboarding data into actionable intelligence that prevents churn. You distinguish between vanity metrics and genuine progress signals, identify invisible patterns in behavioral data that predict customer success or abandonment, and create centralized intelligence hubs that enable proactive customer guidance.

## Task

Design a comprehensive onboarding progress monitoring system for {{saas-product}} that captures meaningful customer journey data, surfaces pain points before they become deal-breakers, and enables every team member to act on customer intelligence.

## Context

The product experiences silent abandonment during onboarding—users disappear without explanation while the team operates blind to friction points. Previous tracking generated unused data because metrics didn't translate to intervention. The monitoring system must:

- Distinguish surface metrics (logins, clicks) from depth signals (feature comprehension, value realization, confidence indicators)
- Detect struggles before they become abandonment—where customers slow down, backtrack, seek help, or exhibit hesitation
- Consolidate goals, pain points, preferences, behavioral data, and interaction history into a single source of truth
- Connect specific data patterns to specific success actions and intervention triggers

**Current situation:**
- Typical onboarding duration: {{onboarding-duration}}
- Critical success milestones: {{success-milestones}}
- Current data collection tools: {{current-tools}}
- Primary pain points: {{pain-points}}

## Output

Provide a structured narrative with clear headings covering:

**Strategic Overview:** Why monitoring onboarding progress transforms customer success from reactive firefighting to proactive guidance, bridging acquisition and retention.

**Foundation Layer:** What meaningful onboarding data consists of—specific milestones that correlate with long-term success versus those that merely look impressive on dashboards.

**Collection Architecture:** Systematic approach to gathering quantitative tracking (progress through workflows, time-to-value, feature adoption sequences) and qualitative intelligence (stated goals, pain points, preferences, confusion signals) without surveillance fatigue.

**Pain Point Detection:** Frameworks for recognizing where customers struggle—instrumentation that surfaces friction before it becomes fatal.

**Milestone Mapping:** Creating progress checkpoints that indicate genuine advancement toward customer goals, aligned with customer-perceived value realization rather than arbitrary completion percentages.

**Centralization Strategy:** Architecture for customer success software as a unified intelligence hub—transforming scattered information silos into coherent customer narratives accessible across teams.

**Actionability Framework:** How collected data translates into intervention triggers, personalized guidance, and proactive support—the connection between data patterns and success actions.

**Implementation Priorities:** Practical steps and common pitfalls, avoiding analysis paralysis while ensuring the system improves outcomes rather than just generating reports.

Use bullet points for specific data points, signals, or action items. Include brief examples to illustrate abstract concepts. Organize hierarchically so the strategic framework is clear before tactical details. Focus on the critical few indicators that matter for onboarding success, ensuring every data point connects to potential intervention. Address how teams actually use this data to help customers, balancing comprehensive tracking with respecting customer privacy and attention.
```

## 用法 / Usage
- 必填變數 / Variables: {{current-tools}}、{{onboarding-duration}}、{{pain-points}}、{{saas-product}}、{{success-milestones}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Onboarding Progress Monitoring System Design Prompt is a free AI prompt that builds data-driven onboarding…
