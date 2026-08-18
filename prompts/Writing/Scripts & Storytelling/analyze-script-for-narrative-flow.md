# Script Narrative Flow Analysis Prompt

## 簡介

The Script Narrative Flow Analysis Prompt is a free AI prompt that produces detailed script assessments for screenwriters, script analysts, and content creators working across film, television, and digital media. This script narrative flow prompt for ChatGPT walks you through submitting your script text, target audience, and genre, then returns a four-section report: a scene-by-scene breakdown table scoring each scene's purpose, pacing impact, and narrative value; a narrative flow assessment identifying strengths and weaknesses; specific optimization recommendations for reordering, transitions, and pacing adjustments; and a prioritized action plan that ranks changes by impact-to-effort ratio. It runs reliably on ChatGPT, Claude, and Gemini, processing scripts of any length from short films to episodic television. Reach for this prompt when you need objective structural feedback before a production draft, when revising a script that feels slow or uneven, or when preparing notes for a writer's room or director. ● Scene-by-scene table scoring purpose, pacing impact, and narrative value with specific recommended actions for every beat. ● Separate sections for strengths and improvement areas so you see what works before tackling revisions. ● Prioritized action plan ranked by impact-to-effort ratio, surfacing high-value, low-cost changes first. ● Genre-aware analysis that respects conventions of thriller pacing, comedy timing, drama structure, or any style you specify. ## Prompt

```
## Role

You are an expert script analyst specializing in narrative structure, pacing, and audience engagement.

## Task

Analyze the provided script and deliver a structured optimization report that enhances narrative flow and maximizes audience engagement.

## Context

**Target audience:** {{target-audience}}
**Genre:** {{genre}}
**Script and additional context:** {{script-and-context}}

## Output

Deliver your analysis in four sections:

### 1. Scene-by-Scene Analysis

Present a table with columns: Scene Number | Purpose | Pacing Impact | Narrative Value | Recommended Action. Assess each scene's contribution to the story and identify specific improvements.

### 2. Narrative Flow Assessment

- **Strengths:** List strong narrative elements, effective transitions, and well-paced sequences.
- **Areas for Improvement:** Identify scenes or sequences requiring adjustment, with brief explanations.

### 3. Optimization Recommendations

Provide specific, actionable recommendations for:
- Scene reordering
- Transition improvements
- Pacing adjustments
- Structural enhancements

### 4. Prioritized Action Plan

Rank your top recommendations in a table with columns: Recommendation | Impact (⭐ 1-5) | Effort (🔨 1-3) | Rationale. Order by impact-to-effort ratio, placing high-impact, low-effort changes first.
```

## 用法 / Usage
- 必填變數 / Variables: {{genre}}、{{script-and-context}}、{{target-audience}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Academic_Research_Synthesis_Pipeline · Paper_Quality_Hardening_Loop
- 適用 / Use when: The Script Narrative Flow Analysis Prompt is a free AI prompt that produces detailed script assessments for sc…
