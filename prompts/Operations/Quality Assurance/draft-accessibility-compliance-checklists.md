# Accessibility Compliance Checklist Builder

## 簡介

The Accessibility Compliance Checklist Builder is a free AI prompt that creates tailored compliance checklists and phased implementation roadmaps for web developers, QA teams, and product managers working toward ADA, WCAG, or EN 301 549 conformance. This accessibility compliance prompt for ChatGPT produces a structured checklist covering visual accessibility (alt text, color contrast ratios, focus indicators), keyboard navigation, ARIA labeling, form accessibility, and media captioning requirements. It also delivers a prioritized roadmap with testing tools, timelines, and validation checkpoints. The prompt adapts to your team size, experience level, current maturity, and target standard, and runs on ChatGPT, Claude, Gemini, and Grok. Use it when launching a new product, preparing for an audit, or remediating an existing site to meet legal and usability standards. ● Maps regional standards (WCAG 2.1 AA/AAA, ADA, EN 301 549) to actionable compliance criteria organized by accessibility area. ● Generates testing procedures with recommended automated and manual tools, including cost tiers and best-use scenarios. ● Delivers a numbered implementation roadmap with phase objectives, sub-tasks, timeframes, dependencies, and success metrics. ● Identifies common pitfalls and prioritizes quick wins in early phases, scaling technical depth to team experience. ## Prompt

```
## Role
You are an accessibility compliance specialist translating regional standards into practical implementation plans.

## Task
Create a comprehensive accessibility compliance checklist and phased implementation roadmap tailored to the user's requirements.

## Context
Compliance requirements:
{{compliance-context}}

*Specify: target standard (ADA, WCAG 2.1 AA/AAA, EN 301 549, etc.), website/application type, team size and experience level, current accessibility maturity, and desired timeline.*

## Requirements
Cover all core compliance areas:
- **Visual accessibility**: alt text implementation, color contrast ratios (minimum thresholds per standard), focus indicators
- **Navigation accessibility**: keyboard navigation patterns, skip links, logical tab order
- **Content accessibility**: ARIA labeling strategies, semantic HTML, heading hierarchy
- **Form accessibility**: label associations, error identification, screen reader optimization
- **Media accessibility**: video captioning and audio descriptions per standard requirements

For each area, include:
- Specific success criteria from the target standard
- Testing procedures with recommended evaluation tools (automated and manual)
- Common implementation pitfalls and how to avoid them

## Output
Structure your response with:

1. **Regional Standard Summary**: Key requirements and conformance levels for the specified context

2. **Compliance Checklist**: Organized by accessibility area, with testable criteria in bullet format

3. **Testing Tools Table**: 
   - Tool name
   - Type (automated/manual/assistive tech)
   - Best use case
   - Cost tier

4. **Implementation Roadmap**: Numbered phases with:
   - Phase objectives
   - Specific sub-tasks
   - Estimated timeframe based on stated team capacity
   - Success metrics and validation checkpoints
   - Dependencies between phases

Prioritize quick wins in early phases and complex remediation in later phases. Tailor technical depth to the team's stated experience level.
```

## 用法 / Usage
- 必填變數 / Variables: {{compliance-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Accessibility Compliance Checklist Builder is a free AI prompt that creates tailored compliance checklists…
