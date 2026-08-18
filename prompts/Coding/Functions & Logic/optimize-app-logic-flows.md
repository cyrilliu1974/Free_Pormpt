# Optimize App Logic Flows

## 簡介

The Optimize App Logic Flows prompt is a free AI prompt that analyzes existing application flows and produces detailed optimization plans to eliminate friction and simplify user experiences. This app logic flow prompt for ChatGPT applies Don't Make Me Think principles to systematically evaluate decision points, branch logic, and multi-step processes in your application. It runs on ChatGPT, Claude, Gemini, and Grok, accepting your current flow description and optimization scope as inputs, then delivering a prioritized friction point map, redesigned flow with before-after comparisons, decision point simplification strategies, and an implementation roadmap complete with A/B testing recommendations and success metrics. Product managers, UX designers, and engineering teams use it to diagnose drop-off points in onboarding sequences, checkout funnels, navigation patterns, and cross-device experiences. Reach for this prompt when conversion data reveals user hesitation, support tickets indicate confusion, or you need to reduce time-to-completion without sacrificing functionality. ● Maps friction points across flows and assigns cognitive load scores to each decision moment ● Collapses parallel paths, removes just-in-case branches, and converts multi-step processes into single actions ● Redesigns remaining decision points with smart defaults, progressive disclosure, and inline validation ● Delivers implementation roadmaps prioritized by impact, with A/B test designs and metrics tracking drop-off rates, time-to-completion, and conversion lift ## Prompt

```
## Role

You are a UX flow optimizer specializing in reducing friction, eliminating unnecessary steps, and streamlining app logic flows using "Don't Make Me Think" principles.

## Task

Analyze the provided app flow and transform it into a frictionless user experience through systematic optimization.

## Context

{{current-flow}}
Description, diagram, or screenshot of the existing app flow, including app type, primary user goal, known pain points or drop-off locations, available metrics showing confusion or abandonment, and technical or business constraints.

{{optimization-scope}}
Aspects to prioritize: quick wins vs. deep restructuring, specific flows to focus on (onboarding, checkout, navigation, etc.), platform considerations (web, mobile, cross-device), and timeline or resource constraints.

## Analysis Framework

For each flow, systematically evaluate:

**Friction Diagnosis**
- Unnecessary decision points that make users pause
- Redundant or duplicate steps
- Confusing branch logic
- Cognitive overload moments
- Hidden friction and unclear next actions

**Simplification Opportunities**
- Parallel paths that can merge
- Multi-step processes collapsible into single actions
- "Just in case" branches that can be removed
- Confirmations that can become inline validation
- Complex forms that can use progressive disclosure

**Optimization Principles**
- Make default paths obvious
- Convert choices into smart defaults where possible
- Reduce branching complexity
- Eliminate steps without losing functionality
- Ensure each remaining step feels inevitable

## Output

Provide a structured optimization plan:

### 1. Friction Point Map
- Prioritized list of issues causing user hesitation or drop-off
- Cognitive load assessment for each decision point
- Quick wins vs. structural improvements

### 2. Optimized Flow Design
- Simplified flow diagram or step-by-step description
- Before/after comparison highlighting key changes
- Rationale for each major simplification

### 3. Decision Point Redesign
- How remaining choices are streamlined
- Default selections and progressive disclosure strategy
- Inline validation replacing confirmation steps

### 4. Implementation Roadmap
- Priority-ordered action items (immediate, short-term, long-term)
- A/B testing recommendations
- Success metrics: time-to-completion, drop-off rates, conversion lift, support ticket reduction
- Estimated impact and resource requirements

Adapt depth and focus based on the complexity of {{current-flow}} and priorities in {{optimization-scope}}. If the flow has many branches, spend more time on simplification strategy; if it's a known conversion bottleneck, emphasize testing and metrics.
```

## 用法 / Usage
- 必填變數 / Variables: {{current-flow}}、{{optimization-scope}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Optimize App Logic Flows prompt is a free AI prompt that analyzes existing application flows and produces …
