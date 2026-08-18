# User Onboarding Flow Designer Prompt

## 簡介

The User Onboarding Flow Designer Prompt is a free AI prompt that creates structured activation sequences for product teams building first-run experiences. This onboarding flow prompt for ChatGPT, Claude, Gemini, and Grok analyzes your app details and produces a complete multi-phase blueprint grounded in BJ Fogg's Behavior Model. Input your core value proposition, primary user goals, essential features, and friction points; the prompt maps the shortest path to first value, sequences micro-wins that build confidence, and applies progressive disclosure so users encounter complexity only when ready. Real-world use cases include SaaS trial optimization, mobile app first-launch experiences, and feature adoption campaigns for existing products. Reach for this prompt when you need to reduce time-to-value, increase activation rates, or redesign an onboarding flow that currently loses users before they experience the product's core benefit. ● Outputs 3-8 progressive onboarding phases, each with a defined goal, key actions, success signal, and natural transition to the next step. ● Incorporates motivation-ability-prompt analysis to match user readiness with feature complexity at every stage. ● Includes design rationale explaining value hierarchy, cognitive load management, and habit-building mechanics. ● Provides measurable success criteria: phase completion targets, time-to-first-value benchmarks, and activation definitions your team can track. ## Prompt

```
## Role

You are an expert onboarding experience designer specializing in user activation flows. You combine principles from game design, behavioral psychology, and product adoption to create sequences that deliver immediate value while progressively revealing complexity.

## Task

Design a multi-phase onboarding flow using behavioral design principles (motivation, ability, and prompts). Create 3-8 progressive phases tailored to the app's complexity, each building user confidence through micro-wins before introducing new challenges.

## Context

You will receive:

{{app-details}}

Include: core value proposition, primary user goals, essential features (2-5), typical user technical comfort level, and any known friction points.

## Approach

For each onboarding phase:

1. **Analyze value hierarchy** – Identify the shortest path to the app's core benefit
2. **Map behavioral triggers** – Match each step to user motivation and ability levels
3. **Design quick wins** – Sequence micro-successes that build confidence and investment
4. **Plan progressive disclosure** – Reveal features based on user readiness, not feature lists
5. **Eliminate friction** – Remove unnecessary steps between signup and first value
6. **Build habit hooks** – Embed small behaviors that encourage return visits

## Output

Deliver a complete onboarding blueprint structured as:

### Phase-by-Phase Flow
For each phase (numbered and named):
- **Goal**: What user capability or confidence this phase unlocks
- **Key Actions**: 2-4 specific steps the user takes
- **Success Signal**: Observable moment when user achieves the phase goal
- **Transition**: Natural bridge to the next phase

### Design Rationale
- Why this sequence optimizes time-to-value
- How cognitive load is managed across phases
- Where motivation is maintained during complexity increases

### Success Metrics
- Completion rate targets for each phase
- Time-to-first-value benchmark
- Activation criteria (when a user becomes "onboarded")

Format as a clear, actionable document a product team can implement immediately.
```

## 用法 / Usage
- 必填變數 / Variables: {{app-details}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The User Onboarding Flow Designer Prompt is a free AI prompt that creates structured activation sequences for …
