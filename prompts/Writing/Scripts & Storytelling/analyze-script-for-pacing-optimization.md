# Script Pacing and Narrative Flow Analyzer

## 簡介

The Script Pacing and Narrative Flow Analyzer is a free AI prompt that delivers detailed scene-by-scene evaluations of screenplays for writers, directors, and story editors. This script analysis prompt for ChatGPT produces a structured breakdown of every scene in your screenplay, scoring each on purpose, impact, pacing, and momentum. It identifies specific strengths and weaknesses, assesses transitions and character development, and generates a recommendations table that suggests which scenes to reorder - complete with rationale grounded in rising action, payoff setup, and genre conventions. It works on ChatGPT, Claude, and Gemini, requiring only your script title, genre, target audience, length, and analysis objective (such as tightening Act 2 or improving climax build). Use this prompt when your script feels uneven, feedback points to pacing problems, or you need an objective structural audit before a pitch or production meeting. ● Scores every scene on duration, purpose, impact, pacing, and momentum using a 1–10 scale. ● Identifies transition problems, tonal inconsistencies, and character-development gaps that slow narrative drive. ● Outputs a recommendations table with current position, suggested position, rationale, and priority for each change. ● Grounds all feedback in established screenwriting principles - rising action, payoff setup, and genre expectations - rather than subjective opinion. ## Prompt

```
## Role
You are an expert script analyst specializing in narrative structure, pacing optimization, and story flow.

## Task
Provide a detailed scene-by-scene evaluation of the submitted script, analyzing structure, identifying issues, and recommending concrete improvements to optimize pacing and narrative flow.

## Context
{{script-details}} should include: script title, genre, target audience, length, and your main objective for this analysis (e.g., tighten Act 2, improve climax build, balance character arcs).

## Analysis Framework

For each scene, assess:

**Scene Structure Analysis**
- 📝 Scene Number
- ⏱️ Duration
- 🎯 Purpose
- 💫 Impact Score (1-10)
- ⚡ Pacing Score (1-10)

**Scene Evaluation**
- ✅ Strengths
- ❌ Weaknesses
- ⚠️ Potential Issues
- 💡 Improvement Suggestions

**Flow Assessment**
- ➡️ Scene Transitions
- 🔄 Narrative Progression
- 🎭 Character Development
- 🏃 Momentum Score (1-10)

## Output

Deliver your analysis in the structure above for each scene, followed by:

**Recommendations Table**

| Scene | Current Position | Suggested Position | Rationale | Priority (1-10) |
|-------|-----------------|-------------------|-----------|-----------------|
| [scene ID] | [act/position] | [act/position] | [justification grounded in pacing, narrative logic, or audience engagement] | [urgency] |

Base all recommendations on established screenwriting principles: rising action, payoff setup, tonal consistency, and genre conventions appropriate to the script.

---

**Script Details:**
{{script-details}}
```

## 用法 / Usage
- 必填變數 / Variables: {{script-details}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Script Pacing and Narrative Flow Analyzer is a free AI prompt that delivers detailed scene-by-scene evalua…
