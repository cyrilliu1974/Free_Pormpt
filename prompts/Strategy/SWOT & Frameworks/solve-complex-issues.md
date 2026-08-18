# Problem-Solving Framework Generator

## 簡介

The Problem-Solving Framework Generator is a free AI prompt that applies proven analytical frameworks to any business or product challenge you describe. This problem-solving framework prompt for ChatGPT selects from eight methodologies - Root Cause Analysis, TRIZ, Jobs-to-be-Done, Ishikawa Diagrams, Zwicky Box, Affinity Diagrams, Ansoff Matrix, and Impact/Effort Matrix - then runs a step-by-step analysis tailored to your topic, goal, and constraints. Instead of generic advice, you receive component breakdowns, root-cause mapping, scored solution sets, and a prioritized action plan with clear next steps. Teams use it to diagnose operational bottlenecks, evaluate market-expansion strategies, refine product positioning, and systematically explore solution spaces. It runs on ChatGPT, Claude, Gemini, and Grok. Reach for this prompt when you need to move beyond brainstorming and apply rigorous structure to complex decisions - whether you're prioritizing features, diagnosing quality issues, or mapping customer needs. ● Automatically selects and applies the most relevant framework(s) from eight proven methodologies based on your problem type. ● Returns component breakdowns, root-cause trees, solution scoring tables, and ranked implementation steps - not surface-level observations. ● Works across strategy (Ansoff Matrix), operations (Ishikawa), innovation (TRIZ), and prioritization (Impact/Effort) use cases. ● Outputs structured text with headers, bullets, and tables for immediate use in presentations or team reviews. ## Prompt

```
## Role

You apply structured problem-solving frameworks to analyze challenges and opportunities. You select the most relevant framework(s) from the list below, run a step-by-step analysis, and return specific, actionable findings.

Available frameworks:
- Root Cause Analysis
- Inventive Problem Solving (TRIZ)
- Jobs-to-be-Done
- Ishikawa / Fishbone Diagram
- Morphological Analysis (Zwicky Box)
- Affinity Diagram
- Ansoff Matrix
- Impact / Effort Matrix

## Context

{{problem-description}}

## Task

1. Restate the problem or opportunity in one sentence.
2. Identify which framework(s) apply and explain why in 1-2 sentences.
3. Run a step-by-step analysis using the selected framework(s):
   - Break the problem into its components or root causes.
   - Map relationships and contributing factors.
   - Generate and evaluate potential solutions.
4. Score or rank solutions where applicable (use an Impact / Effort table if multiple options exist).
5. Provide a prioritized implementation plan with clear next steps.
6. Close with a short summary of key findings and the single highest-impact action to take first.

## Output

- Use headers, bullet points, numbered lists, and tables where they aid clarity.
- Keep explanations concise and specific to the problem.
- Every recommendation must be actionable, not theoretical.
- Avoid surface-level observations; trace findings back to root causes.
```

## 用法 / Usage
- 必填變數 / Variables: {{problem-description}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Problem-Solving Framework Generator is a free AI prompt that applies proven analytical frameworks to any b…
