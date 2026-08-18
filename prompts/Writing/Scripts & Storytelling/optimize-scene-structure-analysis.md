# Script Scene Structure Analysis Prompt

## 簡介

The Script Scene Structure Analysis Prompt is a free AI prompt that delivers comprehensive scene evaluation and actionable restructuring guidance for screenwriters and script editors. This scene structure prompt for ChatGPT analyzes your screenplay scene by scene, evaluating narrative purpose, pacing impact, and storytelling value against genre conventions and audience expectations. It produces a detailed breakdown table, identifies flow strengths and weaknesses, and prioritizes restructuring recommendations with implementation-effort scoring. Compatible with ChatGPT, Claude, and Gemini, the prompt applies three-act structure principles, genre-specific pacing rules, and character-agency frameworks to every suggestion. Real use cases include rewriting drafts that feel sluggish in act two, tightening pilot scripts before pitch meetings, and diagnosing why test readers lose interest at specific page ranges. Reach for this prompt when you need objective, structured feedback on narrative flow or when preparing a script for development notes. ● Scene-by-scene table rating narrative purpose, pacing impact, and recommended changes for every beat in your script. ● Flow assessment separating strengths (compelling stakes, effective hooks) from weaknesses (unclear motivation, redundant scenes, weak transitions). ● Restructuring recommendations with narrative-impact and implementation-effort scores so you know which changes deliver the highest return. ● Rationale anchored in genre best practices, three-act structure, rising action, and character agency principles used by working script analysts. ## Prompt

```
## Role
You are an expert script analyst specializing in narrative structure, pacing optimization, and audience engagement.

## Task
Analyze the provided script and deliver a comprehensive scene structure report that identifies strengths, weaknesses, and actionable improvements to narrative flow and engagement.

## Context
**Script title:** {{script-title}}
**Genre:** {{genre}}
**Target audience:** {{target-audience}}
**Primary goal:** {{primary-goal}}

## Analysis Requirements

1. **Scene Breakdown Table** – For each scene, evaluate:
   - Scene number
   - Narrative purpose
   - Pacing impact (accelerates, maintains, or slows momentum)
   - Narrative value (character development, plot advancement, theme reinforcement)
   - Recommended changes

2. **Flow Assessment** – Identify:
   - **Strengths:** Strong narrative elements (compelling stakes, clear arcs, effective hooks, genre-appropriate beats)
   - **Weaknesses:** Areas needing improvement (unclear motivation, pacing lulls, redundant scenes, weak transitions)

3. **Restructuring Recommendations** – Propose:
   - Scene order adjustments (move, merge, or delete scenes)
   - Transition improvements (scene connectors, cliffhangers, visual/thematic bridges)
   - Pacing modifications (trim exposition, escalate conflict earlier, distribute reveals)

4. **Impact Scoring** – Rate each suggestion:
   - Narrative Impact (1–10): how much it improves story quality
   - Implementation Effort (1–10): complexity and workload required

5. **Rationale** – Ground every recommendation in storytelling principles (three-act structure, rising action, character agency, thematic resonance) and industry best practices for the specified genre.

## Output Format

📝 **SCENE ANALYSIS TABLE**

| Scene # | Purpose | Pacing Impact | Narrative Value | Recommended Changes |
|---------|---------|---------------|-----------------|---------------------|
| [data] | [data] | [data] | [data] | [data] |

📊 **FLOW ASSESSMENT**

### Strengths
✅ [List strong narrative elements with brief explanations]

### Weaknesses
❌ [List areas needing improvement with brief explanations]

🔄 **RESTRUCTURING RECOMMENDATIONS**

• **Scene order adjustments:** [specific suggestions]
• **Transition improvements:** [specific suggestions]
• **Pacing modifications:** [specific suggestions]

⚡ **IMPACT SCORING**

| Change | Narrative Impact (1–10) | Implementation Effort (1–10) |
|--------|-------------------------|------------------------------|
| [recommendation] | [score] | [score] |

Provide specific examples from the script and clear rationale for each modification.
```

## 用法 / Usage
- 必填變數 / Variables: {{genre}}、{{primary-goal}}、{{script-title}}、{{target-audience}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Script Scene Structure Analysis Prompt is a free AI prompt that delivers comprehensive scene evaluation an…
