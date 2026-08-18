# Content Guidelines Framework Builder for ChatGPT

## 簡介

The Content Guidelines Framework Builder is a free AI prompt that creates structured content guideline tables for marketing teams and content strategists. This content guidelines prompt for ChatGPT produces a markdown-formatted framework with 5-8 rows mapping specific content types to target audiences, goals, tone and style requirements, and distribution channels. It works by analyzing your business context, content goals, brand voice, and existing distribution channels, then delivers actionable guidance teams can immediately apply to content planning. Marketing teams use it to align content production with business objectives, ensure consistent brand voice across channels, and identify which content formats serve each audience segment. The prompt runs on ChatGPT, Claude, Gemini, and Grok. Reach for this prompt when launching a content program, onboarding content creators, or standardizing production across multiple teams and channels. ● Maps 5-8 strategic content types to specific audience segments with clear goals for each pairing ● Defines tone and style variations needed across different channels and content formats ● Analyzes audience content consumption preferences before generating the framework ● Outputs immediately usable markdown tables that content teams can reference during planning and production ## Prompt

```
## Role
You are an expert content strategist specializing in developing scalable content frameworks for businesses.

## Task
Create a comprehensive content guideline framework in markdown table format that covers content types, audience segments, goals, tone and style, and distribution channels. The framework should be structured, actionable, and aligned with the business's marketing objectives.

## Context
Business and audience overview:
{{business-context}}

Content goals:
{{content-goals}}

Brand voice and tone:
{{brand-voice}}

Current distribution channels:
{{distribution-channels}}

## Analysis
Before creating the guidelines, analyze:
- Core audience needs and content consumption preferences
- How each content goal maps to business objectives
- Which content types best serve each audience segment
- Tone variations needed across different channels and content types

## Output
Deliver the content guidelines as a markdown table with these columns:

| Content Type | Target Audience | Goals | Tone and Style | Distribution Channels |

Include 5-8 rows covering the most strategic content types for this business. Each row should provide specific, actionable guidance that teams can immediately apply to content planning and creation.
```

## 用法 / Usage
- 必填變數 / Variables: {{brand-voice}}、{{business-context}}、{{content-goals}}、{{distribution-channels}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Content Guidelines Framework Builder is a free AI prompt that creates structured content guideline tables …
