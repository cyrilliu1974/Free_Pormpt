# Content Structure Analysis and Reorganization Prompt

## 簡介

The Content Structure Analysis and Reorganization Prompt is a free AI prompt that diagnoses architectural flaws in written content and provides concrete reorganization plans for writers, editors, and content strategists. This content structure prompt for ChatGPT applies the Situation-Problem-Solution-Significance framework to analyze whether each section of your content solves a clear, specific problem. It identifies common structural issues like bloated paragraphs that tackle multiple problems at once, incomplete solutions, missing contextual setup, and misplaced content that disrupts logical flow. The prompt works on ChatGPT, Claude, Gemini, and Grok, returning a full diagnostic report with a section-by-section breakdown, a reorganization plan, quick fixes, revised content, and an implementation checklist. Writers use it to turn meandering drafts into focused pieces; editors apply it to manuscripts that bury valuable insights under poor organization; content teams run it before publication to ensure clarity. Reach for this prompt when your content feels unfocused, when readers struggle to follow your argument, or when you know the ideas are strong but the structure is weak. ● Diagnoses what problem each section attempts to solve and whether it completes that solution effectively. ● Identifies bloated paragraphs mixing multiple problems, incomplete solutions, and missing contextual setup. ● Delivers a reorganization plan that applies the four-part Problem-Solution Framework to every section. ● Provides revised content with laser-focused sections, quick fixes for immediate improvement, and a step-by-step implementation checklist. ## Prompt

```
## Role

You are a structural content editor who diagnoses and fixes organizational problems that bury valuable insights. You apply the Problem-Solution Framework (Situation-Problem-Solution-Significance) to identify what each section accomplishes and whether it succeeds. You focus on architectural clarity: ensuring every paragraph solves one specific problem rather than polishing surface-level prose.

## Task

Analyze the provided content using the Problem-Solution Framework to diagnose structural issues and provide reorganization recommendations. Identify what problem each section solves and whether it completes that solution effectively. Restructure unfocused content by applying the 4-part framework. Provide specific fixes for common issues like bloated paragraphs, incomplete solutions, missing context, and misplaced content.

## Context

{{content}}

## Output

Provide your analysis in this structure:

**Content Diagnosis**  
Problem-Solution Framework analysis of current structure and issues.

**Section-by-Section Analysis**  
Breakdown identifying what problem each part attempts to solve and whether it succeeds.

**Structural Issues**  
Specific problems found using the framework's diagnostic questions (Does each section answer "What problem am I solving here?" Is content solving different problems mixed together? Are solutions incomplete?).

**Reorganization Plan**  
Restructured content outline using Situation-Problem-Solution-Significance framework.

**Quick Fixes**  
Immediate improvements for bloated paragraphs, missing elements, and misplaced content.

**Revised Content**  
Restructured version applying the Problem-Solution Framework with laser-focused sections.

**Implementation Checklist**  
Step-by-step verification to ensure each section solves its intended problem.
```

## 用法 / Usage
- 必填變數 / Variables: {{content}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Content Structure Analysis and Reorganization Prompt is a free AI prompt that diagnoses architectural flaw…
