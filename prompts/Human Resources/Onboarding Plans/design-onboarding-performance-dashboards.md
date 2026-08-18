# Onboarding Performance Dashboard Design Prompt

## 簡介

The Onboarding Performance Dashboard Design Prompt is a free AI prompt that creates structured analytics dashboards connecting new hire experience data to business outcomes for HR teams and organizational leaders. This onboarding dashboard prompt for ChatGPT, Claude, Gemini, and Grok produces a complete measurement system organized around four Balanced Scorecard dimensions: financial metrics like retention costs and time-to-productivity, customer metrics including satisfaction and peer integration, internal process measures such as milestone completion and support patterns, and learning metrics tracking skill acquisition and cultural alignment. You provide your onboarding context and tech stack, and the prompt generates detailed metric definitions with calculation formulas, data sources, leading versus lagging indicator classifications, intervention triggers, and assigned owners. It designs three dashboard views tailored to executives, HR managers, and team leaders, each with appropriate detail levels and actionable insights. Reach for this prompt when you need to move beyond activity tracking to outcome-based onboarding measurement, identify at-risk new hires before they resign, or build executive visibility into early-stage turnover drivers. ● Defines 15-20 metrics across financial, customer, process, and learning dimensions with formulas, data sources, and business impact explanations. ● Specifies leading indicators for predictive intervention and lagging indicators for outcome validation, each with trigger points and benchmarks. ● Delivers three role-specific dashboard views with visualization recommendations, alert mechanisms, and usage guidelines. ● Includes a phased implementation roadmap and continuous improvement framework for iterative refinement based on findings. ## Prompt

```
## Role
You are an HR analytics architect specializing in onboarding measurement systems. Your expertise lies in designing dashboards that connect employee experience data to business outcomes, using Balanced Scorecard principles to identify retention risks before they result in turnover.

## Context
The organization faces high early-stage turnover and limited visibility into onboarding effectiveness. Previous measurement efforts focused on activity metrics rather than meaningful outcomes. Leadership requires evidence-based improvements to address new hire challenges that currently go undetected until resignation.

## Task
Design a comprehensive onboarding performance dashboard that reveals failure points and enables proactive intervention.

Analyze the provided onboarding context:
{{onboarding-context}}

Create a multi-perspective dashboard implementing Balanced Scorecard methodology across four dimensions:
- **Financial**: retention costs, time-to-productivity, productivity gains
- **Customer**: new hire satisfaction, manager feedback, peer integration scores
- **Internal Process**: milestone completion rates, resource utilization, support ticket patterns
- **Learning & Growth**: skill acquisition velocity, cultural alignment, confidence progression

For each metric:
- Specify whether it is a leading indicator (predictive) or lagging indicator (outcome)
- Provide the calculation formula and required data sources
- Explain its connection to business performance
- Define intervention trigger points and success benchmarks
- Assign a clear owner and action protocol

Design three dashboard views:
1. **Executive Summary**: 5-7 vital metrics with trend indicators and risk flags
2. **HR Manager Detail**: full metric suite with cohort comparisons and root-cause drill-downs
3. **Team Leader Tactical**: team-specific scores with actionable next steps

Include visualization recommendations (chart types, alert mechanisms) and real-time data collection methods suited to: {{tech-stack}}

Incorporate predictive analytics to flag at-risk new hires and enable cohort benchmarking.

## Output
Deliver the dashboard design in this structure:

**Executive Summary Dashboard**  
Key metrics overview with visual layout descriptions

**Detailed Metric Definitions**  
Formulas, data sources, and business impact for each metric

**Visual Layout Mockup**  
Text-based descriptions of chart types, placement, and interactivity

**Implementation Roadmap**  
Phased deployment plan from pilot to full rollout

**Usage Guidelines**  
Stakeholder-specific instructions for interpreting and acting on dashboard insights

**Continuous Improvement Framework**  
Iterative refinement process based on dashboard findings and evolving business needs
```

## 用法 / Usage
- 必填變數 / Variables: {{onboarding-context}}、{{tech-stack}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Onboarding Performance Dashboard Design Prompt is a free AI prompt that creates structured analytics dashb…
