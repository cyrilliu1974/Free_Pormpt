# Recruitment Automation Workflow Builder for Marketing

## 簡介

The Recruitment Automation Workflow Builder for Marketing is a free AI prompt that creates structured, end-to-end hiring workflows tailored to marketing positions. This recruitment automation prompt for ChatGPT generates detailed, dependency-mapped processes that connect job posting through onboarding, specifying which steps must complete before others begin and identifying automation touchpoints at every stage. It runs on ChatGPT, Claude, Gemini, and Grok, and accepts three variables: the specific marketing role and company context, your existing automation tools (ATS platforms, AI screening software, communication systems), and your hiring timeline. Use this prompt when you need to systematize marketing recruitment, reduce manual handoffs, or integrate multiple HR tools into a coherent workflow that respects task dependencies. ● Generates numbered recruitment phases with alphabetical sub-steps showing specific actions, tool integrations, and decision gates ● Maps dependencies so you know which tasks unlock others and where bottlenecks may occur ● Tailors output to your actual automation stack, whether you use Greenhouse, Lever, HireVue, or custom platforms ● Delivers immediately actionable workflows that align job posting, screening criteria, interview logistics, and onboarding in a single coherent system ## Prompt

```
## Role
You are an expert human resources manager specializing in recruitment automation for marketing positions.

## Task
Design a step-by-step automated hiring workflow that covers job posting creation, candidate screening, interview scheduling, and onboarding. Structure each step using dependency grammar principles: establish what must happen first, what depends on it, and how components connect. Optimize for efficiency and integration across systems.

## Context
**Role & Organization:**
{{marketing-role-and-company}} (include the specific marketing position, company size, and industry)

**Automation Landscape:**
{{automation-tools}} (list your preferred or available automation tools: applicant tracking systems, AI resume screening, communication platforms, etc.)

**Timeline:**
{{hiring-timeline}}

## Output
Deliver a numbered list with:
- Each main recruitment phase as a numbered step (1, 2, 3...)
- Sub-steps as alphabetical bullets (a, b, c...) detailing specific actions, tool integrations, and decision points
- Clear dependencies showing which steps must complete before others begin
- Practical automation touchpoints at each stage

Ensure the workflow is immediately actionable and tailored to the context provided.
```

## 用法 / Usage
- 必填變數 / Variables: {{automation-tools}}、{{hiring-timeline}}、{{marketing-role-and-company}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Recruitment Automation Workflow Builder for Marketing is a free AI prompt that creates structured, end-to-…
