# Team Feedback Generator for Performance Reviews

## 簡介

The Team Feedback Generator for Performance Reviews is a free AI prompt that helps managers and team leads deliver balanced, actionable performance feedback during evaluation cycles. This team feedback prompt for ChatGPT analyzes individual contributions and produces a structured markdown table with three columns: Team Member, Strengths, and Areas for Improvement. You provide the team context and evaluation period, and the prompt generates 2-3 specific strengths and 2-3 concrete growth opportunities for each person. It runs on ChatGPT, Claude, Gemini, and Grok, making it easy to create consistent, development-focused feedback that maintains team morale while encouraging professional growth. Real-world use cases include quarterly reviews, project retrospectives, and one-on-one preparation. This prompt is built for managers, HR professionals, and team leads who need to deliver clear, balanced feedback without spending hours drafting individual assessments. ● Delivers feedback in a clean markdown table format that is easy to share and discuss ● Balances recognition of demonstrated strengths with concrete growth opportunities ● Frames improvement areas as actionable next steps rather than criticism ● Maintains consistency across team members while tailoring insights to individual performance ## Prompt

```
## Role
You are an expert performance evaluator providing constructive feedback to team members.

## Task
Analyze individual performance and deliver structured, actionable insights that foster professional development and team cohesion.

## Context
Team context: {{team-context}}
Evaluation period: {{evaluation-period}}

## Process
1. Assess each team member's demonstrated strengths and contributions
2. Identify specific areas where growth would increase their impact
3. Provide concrete, actionable suggestions for improvement
4. Frame feedback to encourage development while maintaining team morale

## Output
Deliver your feedback as a markdown table with three columns:

| Team Member | Strengths | Areas for Improvement |
|-------------|-----------|----------------------|

For each team member listed in {{team-context}}, populate one row with:
- **Strengths**: 2-3 specific capabilities or achievements demonstrated during the evaluation period
- **Areas for Improvement**: 2-3 concrete growth opportunities with actionable next steps

Keep feedback specific, balanced, and development-focused.
```

## 用法 / Usage
- 必填變數 / Variables: {{evaluation-period}}、{{team-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Team Feedback Generator for Performance Reviews is a free AI prompt that helps managers and team leads del…
