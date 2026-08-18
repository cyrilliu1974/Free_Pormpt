# Audience-Tailored Speech Writer

## 簡介

The Audience-Tailored Speech Writer is a free AI prompt that analyzes your audience demographics, interests, and knowledge level to craft speeches optimized for maximum resonance and impact. This audience analysis prompt for ChatGPT combines traditional audience research with dependency grammar principles to structure your speech hierarchically - every supporting point extends logically from a governing idea, creating clarity and flow. You provide the audience context, topic, purpose, and time limit; the prompt generates a multi-level bullet-point outline complete with main points, sub-points, evidence, and optional delivery notes in brackets. It runs reliably on ChatGPT, Claude, and Gemini. Writers, speakers, educators, and corporate trainers use it to tailor vocabulary, tone, examples, and pacing to their specific listeners, whether they're addressing board members, conference attendees, or classroom students. ● Analyzes audience demographics, interests, expectations, and knowledge to inform content decisions ● Structures speeches using dependency grammar so each idea clearly connects to and extends its governing concept ● Adapts vocabulary, tone, rhetorical devices, and examples to audience preferences ● Generates hierarchical outlines with main points, sub-points, evidence, and delivery notes ● Adjusts pacing and depth to fit your specified time constraint ## Prompt

```
## Role
You are an expert speech analyst and writer specializing in audience-tailored communication.

## Task
Analyze the target audience and craft a compelling speech structured using dependency grammar principles—ensuring each idea clearly connects to its governing concept and flows logically throughout.

## Context
{{audience-and-context}}

Topic: {{speech-topic}}

Purpose: {{speech-purpose}}

Time limit: {{time-limit}}

## Process
1. Analyze the audience's demographics, interests, expectations, and knowledge level
2. Identify the core message and key supporting points
3. Adapt vocabulary, tone, examples, and rhetorical devices to audience preferences
4. Structure content using dependency grammar: each point depends on and extends a governing idea, creating clear hierarchical relationships
5. Ensure pacing and depth fit the time constraint

## Output
Deliver the speech as a hierarchical bullet-point outline:
- Main points (governing ideas)
  - Sub-points (dependent supporting ideas)
    - Evidence, examples, or elaboration (terminal nodes)

Maintain clear syntactic dependencies so each level reinforces its parent concept. Include stage directions or delivery notes in [brackets] where helpful.
```

## 用法 / Usage
- 必填變數 / Variables: {{audience-and-context}}、{{speech-purpose}}、{{speech-topic}}、{{time-limit}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Audience-Tailored Speech Writer is a free AI prompt that analyzes your audience demographics, interests, a…
