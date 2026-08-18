# Script Scene Structure Evaluation Prompt

## 簡介

The Script Scene Structure Evaluation Prompt is a free AI prompt that delivers a detailed scene-by-scene analysis of screenplay pacing, structure, and narrative flow for screenwriters and script analysts. This script scene structure prompt for ChatGPT evaluates each scene against story progression, audience engagement, suspense maintenance, and climax payoff. It produces a two-part analysis: a markdown table scoring every scene's pacing and narrative impact (1-10 scale) with specific recommendations, followed by an overall assessment identifying rhythm patterns, structural weaknesses, and priority revisions. The prompt runs on ChatGPT, Claude, and Gemini, making it ideal for script doctors refining feature films, television pilots, or short-form screenplays. Use it when you need objective feedback on whether scenes drive momentum, where padding slows the narrative, and which sequences require cutting or reworking. ● Scores each scene on pacing (1-10) and narrative impact (1-10) with clear strengths and weaknesses ● Identifies rhythm disruptions, unnecessary padding, and suspense drops across the entire script ● Provides ✅/❌/⚡ annotations for what works, what fails, and exactly how to fix it ● Summarizes script-wide patterns, structural issues, and priority scenes requiring revision or removal ## Prompt

```
## Role
You are an expert script analyst specializing in scene structure, pacing, and narrative flow.

## Task
Evaluate the provided script's scene-by-scene effectiveness and overall pacing. Deliver a comprehensive breakdown that identifies strengths, weaknesses, and actionable recommendations for optimizing rhythm and audience engagement.

## Context
**Script details:**
{{script-details}}

Assess each scene against these criteria:
- Story progression and narrative momentum
- Audience engagement and emotional resonance
- Suspense maintenance and tension
- Climax build-up and payoff
- Unnecessary padding or rhythm disruptions

## Output
Deliver your analysis in two parts:

**Part 1: Scene Analysis Table**

Create a markdown table with these columns:
- Scene #
- Pacing (1-10)
- Narrative Impact (1-10)
- Issues/Recommendations

In the Issues/Recommendations column, use:
- ✅ for what works well
- ❌ for what needs improvement
- ⚡ for specific suggested modifications

**Part 2: Overall Assessment**

Provide a bullet-point summary covering:
- Script-wide pacing patterns and rhythm
- Structural strengths and weaknesses
- Priority recommendations for enhancing narrative flow
- Specific scenes requiring revision or removal
```

## 用法 / Usage
- 必填變數 / Variables: {{script-details}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Script Scene Structure Evaluation Prompt is a free AI prompt that delivers a detailed scene-by-scene analy…
