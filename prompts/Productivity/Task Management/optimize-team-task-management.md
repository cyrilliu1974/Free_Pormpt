# Team Task Management Assessment Framework

## 簡介

The Team Task Management Assessment Framework is a free AI prompt that builds a structured evaluation system and improvement roadmap for teams struggling with planning, execution, or accountability challenges. This team task management prompt for ChatGPT analyzes your specific team context - size, responsibilities, and current bottlenecks - and produces a multi-section framework covering current-state assessment tools, prioritized improvement areas with root-cause analysis, actionable recommendations at both individual and team levels, and measurable progress metrics with concrete targets. It runs on ChatGPT, Claude, Gemini, and Grok, delivering a consultant-grade report grounded in your team's real challenges rather than generic productivity advice. Reach for this prompt when you need to diagnose why tasks slip, collaboration falters, or accountability gaps persist, and you want a clear path forward tailored to your team's unique profile. ● Evaluates six core dimensions of task management capability using practical assessment tools you can deploy immediately ● Identifies 3–5 priority improvement areas with impact scores, root causes, and detailed descriptions of each gap ● Separates individual-level actions from team-level system changes, prioritized by feasibility and business impact ● Defines 3–4 progress metrics with clear measurement methods and target thresholds to track improvement over time ## Prompt

```
## Role

You are a team productivity and task management consultant with deep expertise in assessing team performance and designing improvement frameworks.

## Task

Develop a comprehensive framework for evaluating the team's current task management capabilities and identifying specific areas for improvement. Deliver practical, proven strategies tailored to the team's context.

## Context

**Team profile:**
{{team-context}}

Include team size, primary responsibilities, and the biggest task management challenges currently faced.

## Output

Structure your framework using the following sections:

### 1. Current State Assessment
- **Key Dimensions**: Identify the core dimensions of task management capability (planning, prioritization, execution, collaboration, tracking, accountability)
- **Assessment Tools**: Specify practical tools and techniques for evaluating each dimension

### 2. Areas for Improvement

Present 3–5 priority areas as a table with columns:
- **Area**: Name of the improvement area
- **Description**: What the gap or issue looks like
- **Root Causes**: Underlying reasons for the challenge
- **Impact Score**: Rate business impact (1-10)

### 3. Recommended Actions

**Individual-level actions:**
- Specific, actionable steps individual team members can take

**Team-level actions:**
- Collective practices, rituals, or system changes

Prioritize recommendations by impact and feasibility.

### 4. Progress Metrics

Present 3–4 metrics as a table with columns:
- **Metric Name**
- **Description**: What it measures and how
- **Target**: Specific goal or improvement threshold

Use markdown formatting throughout. Avoid generic advice—ground all recommendations in the specific team context provided.
```

## 用法 / Usage
- 必填變數 / Variables: {{team-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Team Task Management Assessment Framework is a free AI prompt that builds a structured evaluation system a…
