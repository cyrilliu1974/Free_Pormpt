# Performance Review Evaluation Prompt

## 簡介

The Performance Review Evaluation Prompt is a free AI prompt that helps HR managers and team leaders conduct fair, structured performance reviews aligned with company goals. This performance review prompt for ChatGPT produces a markdown table for each employee that breaks down their strengths, areas for improvement, and a concrete action plan with measurable steps and timelines. You provide your team roster, company context (industry, KPIs, values), and review period, and the prompt generates balanced evaluations that recognize achievements while offering actionable development guidance. It runs on ChatGPT, Claude, Gemini, and Grok, making it simple to create consistent, objective assessments that tie individual contributions to team dynamics and organizational success. Use this prompt when you need to evaluate multiple team members systematically, ensure fairness across reviews, or translate performance observations into development roadmaps that employees can act on immediately. ● Creates a separate three-column table (Strengths | Areas for Improvement | Action Plan) for every team member ● Aligns individual assessments with your company's KPIs, values, and strategic objectives ● Balances recognition of achievements with concrete, measurable development steps and timelines ● Maintains consistency and fairness across all evaluations while addressing each person's unique contributions ## Prompt

```
## Role
You are an expert Human Resources Manager conducting performance reviews.

## Task
Evaluate team members' performance and provide constructive feedback. For each person, assess contributions, achievements, and growth opportunities, then create a fair and balanced evaluation aligned with company goals.

## Context
- Team members and roles: {{team-roster}}
- Company context: {{company-context}} (include company name, industry, key performance indicators, and core values)
- Review period: {{review-period}}

Consider how each individual's performance affects team dynamics and company success. Balance recognition of strengths with actionable guidance for development.

## Output
Present your evaluation as a markdown table for each team member with three columns:

| Strengths | Areas for Improvement | Action Plan |
|-----------|----------------------|-------------|
| [specific achievements and capabilities] | [concrete growth opportunities] | [measurable steps with timelines] |

Provide a separate table for each team member, with their name as a heading above their table.
```

## 用法 / Usage
- 必填變數 / Variables: {{company-context}}、{{review-period}}、{{team-roster}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Domain_Specific_Reasoning · Multi_Perspective_Simulation
- 適用 / Use when: The Performance Review Evaluation Prompt is a free AI prompt that helps HR managers and team leaders conduct f…
