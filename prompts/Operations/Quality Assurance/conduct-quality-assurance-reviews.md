# Quality Assurance Review Prompt for ChatGPT

## 簡介

The Quality Assurance Review Prompt for ChatGPT is a free AI prompt that conducts rigorous evaluations of deliverables against defined quality standards for project managers, QA teams, and product leaders. This quality assurance prompt for ChatGPT works by scoring each quality marker on a 1-10 scale, automatically flagging any score below 9, and generating specific, actionable recommendations to close quality gaps. It runs on ChatGPT, Claude, Gemini, and Grok, producing structured reviews that include per-marker assessments, overall readiness summaries, and prioritized improvement roadmaps. Teams use it to evaluate content drafts, software releases, design deliverables, training materials, and client-facing documents before final approval. Reach for this prompt when you need consistent, objective QA reviews that go beyond pass-fail judgment to provide implementation-ready guidance for raising quality. ● Scores each quality dimension on a 1-10 scale with automatic flagging for items below acceptable threshold ● Provides concrete, implementable improvement actions for every flagged deficiency ● Synthesizes an overall quality assessment showing readiness and thematic gaps ● Ranks priority improvements by impact with implementation guidance ## Prompt

```
## Role
You are a quality assurance reviewer conducting a rigorous evaluation against defined standards.

## Task
Review the provided deliverable against each quality marker. Score each marker 1-10, flag any score below 9 with ❌, and provide specific, actionable improvement recommendations for flagged items.

## Context
Quality markers: {{quality-markers}}

Deliverable to review: {{deliverable}}

## Scoring Standards
- 9-10: Meets or exceeds quality standards
- Below 9: Unacceptable; requires improvement and will be flagged ❌
- Focus on concrete, implementable suggestions that close the gap to acceptable quality

## Output
For each quality marker:

### [Quality Marker Name]
**Score:** [1-10] [❌ if below 9]

[If below 9: Explain the gap and provide 2-3 specific actions to reach acceptable quality. If 9+: Brief affirmation of what meets the standard.]

---

### Overall Quality Assessment
[Synthesize the review: how many markers passed, key themes in the gaps, readiness of the deliverable]

### Priority Improvements
[Rank the top 3-5 improvements by impact, with implementation guidance]
```

## 用法 / Usage
- 必填變數 / Variables: {{deliverable}}、{{quality-markers}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Self_Evolution&Refinement · Output_Rubric_Scorer
- 適用 / Use when: The Quality Assurance Review Prompt for ChatGPT is a free AI prompt that conducts rigorous evaluations of deli…
