# Script Structure Analysis Prompt for Screenwriters

## 簡介

The Script Structure Analysis Prompt for Screenwriters is a free AI prompt that delivers detailed scene-level diagnostics and concrete structural improvements for screenplays, teleplays, and scripts. This script structure prompt for ChatGPT analyzes your screenplay and returns a multi-section evaluation: a scene analysis table scoring each scene's purpose, pacing impact (1-10), and flow rating (1-10) alongside specific actions required; a narrative assessment examining plot progression, momentum, suspense-building techniques, climax effectiveness, and transition quality; categorized lists of strong scenes and problem areas with explicit reasons drawn from the script; and prioritized recommendations for reordering, cutting, or editing each grounded in three-act structure, scene economy, dramatic tension curves, Save the Cat, Story Grid, and classical dramatic principles. It runs on ChatGPT, Claude, and Gemini, returning markdown with headers, tables, and emojis for quick navigation. Screenwriters use it to diagnose pacing bottlenecks, tighten narrative momentum, and ensure every scene serves a clear dramatic function before production, pitch, or table reads. ● Scene-by-scene table with numeric pacing and flow scores plus required actions for each beat ● Narrative assessment covering plot momentum, suspense techniques, climax strength, and transition quality ● Separate lists identifying strong scenes and problem areas with specific script examples and reasons ● Prioritized, actionable recommendations tied to industry frameworks like three-act structure, Save the Cat, Story Grid, and dramatic tension curves ## Prompt

```
## Role
You are an expert scriptwriter specializing in narrative structure and pacing optimization.

## Task
Analyze the provided script and deliver a scene-by-scene breakdown with concrete action items for improvement. Structure your analysis as follows:

### Scene Analysis Table
Create a table with these columns:
- Scene #
- Purpose
- Pacing Impact (1-10)
- Flow Rating (1-10)
- Action Required

### Narrative Assessment
Provide a comprehensive evaluation covering:

**🎭 Story Elements**
- Plot progression and momentum
- Suspense building techniques
- Climax effectiveness
- Scene transition quality

**✅ Strong Scenes**
List scenes that effectively drive the story forward, with specific reasons why they work.

**⚠️ Problem Areas**
Identify scenes requiring improvement, explaining the structural or pacing issues.

**📝 Recommendations**
Provide detailed, actionable suggestions for scene reordering, cutting, or editing. Ground each recommendation in industry-standard screenplay principles (three-act structure, scene economy, dramatic tension curves).

## Context
{{script-details}}

## Output
Deliver the analysis in markdown format with clear headers, tables, and emoji for readability. Include specific examples from the script and reference established screenwriting principles (Save the Cat, Story Grid, or classical dramatic structure) to justify each recommendation.
```

## 用法 / Usage
- 必填變數 / Variables: {{script-details}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Academic_Research_Synthesis_Pipeline · Writing_Quality_Multi_Dimension_Checker
- 適用 / Use when: The Script Structure Analysis Prompt for Screenwriters is a free AI prompt that delivers detailed scene-level …
