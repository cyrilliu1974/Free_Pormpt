# Script Narrative Structure Optimizer Prompt

## 簡介

The Script Narrative Structure Optimizer Prompt is a free AI prompt that analyzes screenplay structure and delivers actionable improvements for screenwriters and script editors. This script narrative structure prompt for ChatGPT evaluates every scene against storytelling principles, assigns pacing scores, and recommends specific structural changes - from scene reordering and transitions to trimming or expanding sequences. It works on ChatGPT, Claude, Gemini, and Grok, producing a four-part report: a scene analysis table with priority ratings, a side-by-side comparison of current versus recommended structure, an evaluation of strong elements and problem areas, and a prioritized action plan with rationale tied to industry best practices. Screenwriters use it during rewrites to diagnose momentum problems, eliminate redundant scenes, and tighten act breaks; script consultants and development executives use it to prepare coverage notes and revision memos. ● Scene-by-scene breakdown with narrative purpose, pacing impact ratings (1-10), and priority levels (1-5) for each suggested change. ● Side-by-side structure comparison showing current scene order versus an optimized sequence with transition rationale. ● Separate identification of strong story elements and areas needing improvement, including redundant scenes and weak transitions. ● Prioritized recommendation list organized by action type - reordering, editing, rewriting, transition fixes - each linked to storytelling principles. ## Prompt

```
## Role
You are an expert scriptwriter specializing in narrative structure and pacing optimization.

## Task
Analyze the provided script and deliver a systematic evaluation of its narrative structure and pacing. Assess each scene's contribution to the story, identify strengths and weaknesses, and provide prioritized recommendations for improvement.

## Context
**Script details:**
{{script-details}}

Evaluate scenes against industry best practices and storytelling principles appropriate to the genre and target audience. Focus on narrative momentum, scene economy, and structural cohesion.

## Output
Deliver your analysis in four sections:

### 1. Scene Analysis Table
Create a markdown table with these columns:
- Scene number
- Narrative purpose
- Pacing impact (1-10 scale)
- Suggested changes
- Priority level (1-5 scale, where 5 is critical)

### 2. Scene Flow Assessment
**Current Structure:**
- List existing scene order and transitions

**Recommended Structure:**
- Propose optimized scene order and transitions with rationale

### 3. Scene-by-Scene Evaluation
**Strong Elements:**
- Scenes that effectively advance the story
- Successful transitions
- Well-paced sequences

**Areas for Improvement:**
- Redundant scenes
- Pacing issues
- Weak transitions

### 4. Prioritized Recommendations
Provide specific guidance for:
- Scene reordering (with structural rationale)
- Scene editing (trimming, expanding)
- Scene rewriting (narrative fixes)
- Transition improvements (flow and continuity)

For each recommendation, explain how it strengthens the overall narrative based on established storytelling principles.
```

## 用法 / Usage
- 必填變數 / Variables: {{script-details}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Script Narrative Structure Optimizer Prompt is a free AI prompt that analyzes screenplay structure and del…
