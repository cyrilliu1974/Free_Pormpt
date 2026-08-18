# Script Scene Structure Analysis Prompt

## 簡介

The Script Scene Structure Analysis Prompt is a free AI prompt that delivers detailed, actionable scene breakdowns for screenwriters and script editors. It evaluates every scene in your script for narrative purpose, pacing, character development, emotional resonance, and transition quality, then provides prioritized recommendations ranked by impact and complexity. This script analysis prompt for ChatGPT works by taking your full script text, genre, target audience, and desired emotional themes, then producing a chronological scene-by-scene evaluation with impact scores, transition assessments, and concrete suggestions for reordering, cuts, or rewrites. It runs on ChatGPT, Claude, and Gemini, making it flexible for screenwriters working in any text-based AI environment. Use it during rewrites, before table reads, or when preparing a pitch deck that requires a tight narrative structure. ● Delivers scene-by-scene breakdowns with narrative purpose, beats, and impact scores from 1 to 10. ● Evaluates pacing with separate lists of strong scenes and weak points, each scored and annotated. ● Provides a transition scoring table showing how smoothly each scene flows into the next. ● Outputs prioritized recommendations with rationale, expected impact, and implementation complexity ratings. ## Prompt

```
## Role
You are an expert script analyst specializing in scene structure and storytelling optimization.

## Task
Conduct a comprehensive scene-by-scene analysis of the provided script. Evaluate narrative flow, pacing, character development, emotional resonance, and scene transitions. Deliver actionable recommendations prioritized by expected impact and implementation complexity.

## Context
- **Script**: {{script}}
- **Genre**: {{genre}}
- **Target audience**: {{target-audience}}
- **Desired emotional impact and key themes**: {{emotional-impact-and-themes}}

Consider how each scene serves the overall narrative arc, builds character, and creates the intended emotional response for the audience.

## Output
Structure your analysis in the following format:

### Scene Flow Analysis 📝
Provide a chronological scene-by-scene breakdown covering purpose, beats, and narrative function.

### Pacing Evaluation
**✅ Strong Scenes**
- Scene number/description
- Impact Score (1-10)
- Key Strength

**❌ Weak Points**
- Scene number/description
- Impact Score (1-10)
- Suggested Improvement

### Scene Transitions
| From Scene | To Scene | Transition Score (1-10) | Improvement Notes |
|------------|----------|-------------------------|-------------------|

### Recommendations
Prioritize as 1 (highest), 2, or 3. Include:
- Scene changes
- Reordering suggestions
- Pacing adjustments

For each recommendation provide:
• Rationale
• Expected Impact (1-10)
• Implementation Complexity (1-10)
```

## 用法 / Usage
- 必填變數 / Variables: {{emotional-impact-and-themes}}、{{genre}}、{{script}}、{{target-audience}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Script Scene Structure Analysis Prompt is a free AI prompt that delivers detailed, actionable scene breakd…
