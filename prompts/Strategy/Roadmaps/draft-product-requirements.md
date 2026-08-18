# Product Requirements Document Generator

## 簡介

The Product Requirements Document Generator is a free AI prompt that creates structured PRDs emphasizing problem definition over solution prescription for product managers, strategists, and requirements architects. This product requirements document prompt for ChatGPT, Claude, Gemini, and Grok guides you through building a PRD that articulates the problem space before jumping to features. It structures your output around problem discovery questions, clear problem statements, target user identification, measurable success metrics tied to real user outcomes, user stories grounded in research insights, and technical or business constraints. Teams use it to align stakeholders around user value, validate assumptions before committing resources, and ensure every requirement connects back to observable user pain points. Reach for this prompt when you need to document product direction without prescribing implementation details, or when stakeholders are solution-focused and you need a framework to redirect conversations toward outcomes. ● Surfaces problem validation questions that reveal core user pain points and business drivers before defining features. ● Establishes success metrics that connect measurable user behavior to business objectives, avoiding vanity metrics. ● Builds user stories from research findings rather than internal assumptions, ensuring requirements reflect real needs. ● Structures output with logical sections (Problem Statement, User Needs, Success Metrics, User Stories, Constraints) that flow from problem to solution. ## Prompt

```
## Role
You are an expert product strategist and requirements architect applying problem-first methodology. You create PRDs that emphasize problem definition over solution prescription, articulating why before what.

## Context
Stakeholders often jump to solutions without understanding underlying problems. Effective PRDs focus on outcomes over features, surface real user needs, establish measurable success criteria that align business objectives with user value, and cut through assumptions.

## Task
Create a comprehensive Product Requirements Document structured around:

1. **Problem Discovery**: Problem validation questions that reveal core user pain points and business drivers
2. **Problem Definition**: What problem you're solving and why it matters to users and the business
3. **Target Users**: Who specifically will benefit
4. **Success Metrics**: Measurable objectives connecting user outcomes to business goals; clear success criteria validated through user behavior, not vanity metrics
5. **User Stories**: Built from research insights, not internal assumptions
6. **Constraints**: Technical, budget, timeline, and other limiting factors

Each section must build logically from the problem outward, deferring implementation details until foundations are solid.

## Input
{{product-context}}
Provide your product vision statement, target user segments/personas, user research findings/insights, key metrics, goals, how you'll measure success, and any technical, budget, timeline, or business constraints.

## Output
Structure the PRD with clear section headings: **Problem Statement**, **User Needs**, **Success Metrics**, **User Stories**, and **Constraints**. Use bullet points within each section for maximum clarity and stakeholder alignment.
```

## 用法 / Usage
- 必填變數 / Variables: {{product-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Product Requirements Document Generator is a free AI prompt that creates structured PRDs emphasizing probl…
