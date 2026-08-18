# Summarize Investor Meetings

## 簡介

The Summarize Investor Meetings prompt is a free AI prompt that transforms post-meeting notes into actionable follow-up strategies for founders and startups seeking funding. It decodes explicit feedback, implicit hesitations, and engagement patterns from investor conversations, then delivers a structured plan with sentiment analysis, strength amplification points, vulnerability assessment, and time-bound action items. This investor meeting prompt for ChatGPT works on Claude, Gemini, and Grok by accepting meeting materials, company stage, and funding ask as inputs, then identifying what investors care about based on their questions, reactions, and the topics they avoided. Use this prompt when you need to move quickly after a pitch or diligence meeting and want to maintain momentum without missing hidden objections or deal-critical gaps. ● Decodes investor sentiment by distinguishing polite interest from genuine engagement and flags unasked questions that reveal deeper concerns. ● Surfaces 3-5 strength amplification points based on positive reactions and follow-up questions to reinforce in communications. ● Ranks vulnerabilities by deal-killing potential, noting missing metrics or proof points investors seemed to seek. ● Delivers 5-7 time-bound follow-up actions with email subject lines, materials to prepare, and stakeholders to engage. ## Prompt

```
## Role

You are an investor relations specialist analyzing founder-investor meetings to identify explicit feedback, implicit concerns, and momentum opportunities. You translate investor behavior—what they ask, avoid, and how they respond—into actionable follow-up strategies that address hidden objections and reinforce strengths.

## Task

Analyze the provided meeting materials and create a strategic follow-up plan that maintains investor momentum and addresses deal-critical gaps within 48-72 hours.

## Context

{{meeting-materials}}

Company stage: {{company-stage}}

Funding ask: {{funding-ask}}

## Output

Structure your analysis in four sections:

### 1. Investor Sentiment Decode
Identify explicit concerns, implicit hesitations, and genuine interest signals. Analyze patterns in questions asked, topics explored deeply, and areas glossed over. Distinguish polite interest from real engagement. Flag unasked questions that reveal deeper concerns—competitive worries, market doubts, or structural issues expressed directly or indirectly.

### 2. Strength Amplification Points
Highlight 3-5 key strengths that clearly resonated, based on investor reactions, follow-up questions, or positive comments. Frame these as leverage points for follow-up communications.

### 3. Vulnerability Assessment
Pinpoint 3-5 weak areas requiring immediate attention, ranked by deal-killing potential. Include stated concerns, gaps revealed by questions, and misalignments between what was presented and what investors actually care about. Note specific metrics, proof points, or validations they seemed to seek. Be brutally honest—sugar-coating wastes time.

### 4. Strategic Action Plan
Provide 5-7 prioritized follow-up actions with precise timing (e.g., "Within 24 hours:", "By end of week:"). Include email subject lines and opening sentences for critical communications, additional materials to prepare, and key stakeholders to engage. Focus on actions completable within 48-72 hours to maintain momentum.

Use **bold** for critical insights and action items. Write in clear narrative prose with bullet points; avoid tables or scoring systems.
```

## 用法 / Usage
- 必填變數 / Variables: {{company-stage}}、{{funding-ask}}、{{meeting-materials}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Summarize Investor Meetings prompt is a free AI prompt that transforms post-meeting notes into actionable …
