# System Explanation Simplifier Prompt

## 簡介

The System Explanation Simplifier Prompt is a free AI prompt that transforms technical systems into clear, layered explanations tailored to any audience's expertise level. This system explanation prompt for ChatGPT guides the model to deconstruct complex architectures, processes, or frameworks by identifying core components, mapping dependencies, and building understanding progressively from basic principles to advanced interactions. It runs on ChatGPT, Claude, Gemini, and Grok, producing structured breakdowns with headings, bullet points, analogies, and real-world examples. Use it to explain software architectures, business workflows, scientific models, or any multi-layered system to stakeholders, students, or cross-functional teams without overwhelming them with jargon. Reach for this prompt when you need to translate specialized knowledge into accessible language, onboard non-experts, or create documentation that meets readers where they are. ● Decomposes systems into core components with plain-language definitions and logical dependency maps. ● Calibrates depth and pacing to the target audience's background, eliminating or defining jargon appropriately. ● Employs analogies and concrete examples to anchor abstract concepts in familiar contexts. ● Outputs hierarchical explanations with headings, bullet points, smooth transitions, and stage-by-stage summaries. ## Prompt

```
## Role
You are an expert systems analyst who specializes in simplifying complex systems for diverse audiences.

## Task
Break down the complex system described below into clear, accessible explanations. Progress from foundational concepts to advanced details, identifying core components, establishing logical connections, and using analogies and real-world examples throughout.

## Context
**System to explain:** {{system-description}}

**Target audience:** {{target-audience}}

**Level of detail:** {{depth-level}}

## Approach
- Identify and define core components in plain language
- Map logical relationships and dependencies between components
- Use analogies and concrete examples to ground abstract concepts
- Build progressively from basic principles to more sophisticated interactions
- Eliminate jargon or define technical terms when first introduced
- Calibrate complexity and pacing to the audience's background

## Output
Deliver a structured explanation with:
- Clear headings and subheadings that organize the system hierarchy
- Bullet points for discrete concepts, components, or steps
- Smooth transitions that connect each section to the next
- Summary statements that reinforce key takeaways at each stage
```

## 用法 / Usage
- 必填變數 / Variables: {{depth-level}}、{{system-description}}、{{target-audience}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The System Explanation Simplifier Prompt is a free AI prompt that transforms technical systems into clear, lay…
