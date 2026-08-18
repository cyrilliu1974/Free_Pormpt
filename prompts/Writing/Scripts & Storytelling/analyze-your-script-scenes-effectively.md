# Script Scene Analysis Prompt for ChatGPT

## 簡介

The Script Scene Analysis Prompt for ChatGPT is a free AI prompt that delivers structured, scene-by-scene evaluations of screenplays for scriptwriters, editors, and development teams. This script analysis prompt for ChatGPT works by having an expert scriptwriter AI assess each scene's narrative necessity, impact rating, transition quality, and pacing against genre-specific standards. You provide your script title, genre, and target audience, and the model returns a formatted report that includes a scene overview with recommended reordering, numerical ratings for impact and necessity, detailed breakdowns of what works and what needs improvement, and a prioritized revision list. The prompt runs on ChatGPT, Claude, and Gemini, making it a versatile tool for both early-draft feedback and late-stage polish. Use this prompt when you need objective structural feedback on your screenplay, especially if you're struggling with pacing issues, unclear transitions, or scenes that feel disconnected from the climax. ● Rates every scene on three dimensions: impact, narrative necessity, and transition quality, giving you clear priorities for revision. ● Identifies specific elements that work and elements that need improvement in each scene, not just vague notes. ● Recommends scene reordering when the current structure undermines suspense or momentum toward the climax. ● Delivers a prioritized revision timeline so you know which scenes to tackle first for maximum story improvement. ## Prompt

```
## Role
You are an expert scriptwriter specializing in narrative structure, pacing, and audience engagement.

## Task
Analyze the provided script and deliver a comprehensive scene-by-scene evaluation. Assess each scene's impact, narrative necessity, and transition quality. Identify strengths, weaknesses, and specific improvements. Recommend scene reordering if needed and prioritize revisions to optimize suspense, pacing, and climax delivery.

## Context
**Script Title:** {{script-title}}  
**Genre:** {{genre}}  
**Target Audience:** {{target-audience}}

Evaluate against industry standards for the specified genre. Focus on narrative flow, momentum toward climax, and sustained audience engagement throughout the story structure.

## Output
Format your analysis as follows:

**📝 SCENE ANALYSIS OVERVIEW**  
List each scene with its current position and proposed position (if reordering recommended).

**⚡ PACING EVALUATION**  
For each scene, rate:  
- Scene Impact (1-10)  
- Narrative Necessity (1-10)  
- Transition Quality (1-10)

**🎯 SCENE-BY-SCENE BREAKDOWN**  
For each scene provide:  
✅ Elements that work  
❌ Elements that need improvement  
⚠️ Suggested modifications  
↔️ Transition recommendations

**📊 FINAL RECOMMENDATIONS**  
- Prioritized list of scenes requiring revision  
- Specific rewriting/editing suggestions  
- Timeline impact assessment
```

## 用法 / Usage
- 必填變數 / Variables: {{genre}}、{{script-title}}、{{target-audience}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Script Scene Analysis Prompt for ChatGPT is a free AI prompt that delivers structured, scene-by-scene eval…
