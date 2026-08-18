# App Requirements Writer Prompt for Agile Teams

## 簡介

The App Requirements Writer Prompt for Agile Teams is a free AI prompt that translates raw app concepts into structured, testable user stories and acceptance criteria for product managers and development teams. This app requirements prompt for ChatGPT, Claude, Gemini, and Grok takes a high-level app idea and produces a complete requirements document organized by user personas, prioritized user stories in the "As a [user], I want [goal] so that [benefit]" format, and measurable acceptance criteria ready for sprint planning. It applies the MoSCoW prioritization framework (Must have, Should have, Could have, Won't have) to every feature based on user impact and business value, ensuring development teams focus on what matters most. Product managers use it to transform stakeholder vision into developer-ready specifications; Agile coaches use it to standardize backlog structure; technical leads use it to estimate effort and scope sprints. ● Extracts user personas with pain points from vague app concepts ● Writes user stories focused on value delivery, not technical implementation ● Generates testable acceptance criteria that support effort estimation and test case creation ● Applies MoSCoW prioritization to align feature development with business impact ## Prompt

```
## Role

Product requirements analyst translating app concepts into structured, testable Agile requirements.

## Task

Analyze the app concept and produce user stories with acceptance criteria. Prioritize all features using MoSCoW (Must have, Should have, Could have, Won't have) based on user impact and business value.

## Context

{{app-concept}}

Include target users, core functionality, business goals, technical constraints (platform, budget, timeline), and competitive differentiation.

## Process

1. Identify core user personas and their primary pain points
2. Write user stories: "As a [user type], I want [goal] so that [benefit]"
3. Focus stories on user value, not technical implementation
4. Define acceptance criteria using measurable, testable conditions
5. Ensure requirements support effort estimation and test case creation
6. Apply MoSCoW prioritization to all features

## Output

Structure your response:

### User Personas
List personas with key characteristics and pain points.

### Prioritized User Stories
Group by MoSCoW category. For each story:
- User story statement
- Acceptance criteria (bulleted, testable conditions)
- Priority/impact assessment

### Feature Priority Matrix
Summarize Must/Should/Could/Won't features in a clear hierarchy.

Use clear headings, bullet points, and formatting for development team readability.
```

## 用法 / Usage
- 必填變數 / Variables: {{app-concept}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Skill_Prompt_Spec_Extractor
- 適用 / Use when: The App Requirements Writer Prompt for Agile Teams is a free AI prompt that translates raw app concepts into s…
