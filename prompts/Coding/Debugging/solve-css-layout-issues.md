# CSS Layout Debugging Prompt

## 簡介

The CSS Layout Debugging Prompt is a free AI prompt that walks through methodical DevTools-based analysis to identify and fix browser rendering issues, flexbox and grid conflicts, z-index problems, and cascading inheritance errors for front-end developers and designers. This CSS debugging prompt for ChatGPT, Claude, Gemini, and Grok instructs the model to act as a CSS specialist who inspects computed styles, visualizes the box model, and diagnoses root causes rather than applying surface-level patches. It produces structured output that includes problem identification, root cause analysis backed by DevTools findings, corrected code with inline explanations, technical reasoning for why the fix resolves the issue, and concrete prevention tips. Use it when standard fixes fail, when layout behavior differs across browsers, or when you need to understand why a flexbox container collapses, a grid track overflows, or positioned elements stack incorrectly. ● Inspects computed styles and box model to surface inheritance conflicts, spacing bugs, and sizing mistakes. ● Identifies common pitfalls like missing clearfix, improper flexbox/grid declarations, z-index stacking context errors, and overflow handling. ● Delivers side-by-side before/after code with inline comments explaining each change. ● Includes technical explanations of how browsers interpret the corrected styles and actionable prevention strategies. ## Prompt

```
## Role

You are a CSS debugging specialist with deep expertise in browser rendering engines, the box model, and modern layout systems (flexbox, grid, positioning).

## Task

Debug the CSS layout issue described below. Use a methodical DevTools-based approach: inspect computed styles to find inheritance conflicts, visualize the box model to expose spacing and sizing problems, and identify root causes such as missing clearfix, improper flexbox/grid usage, z-index stacking conflicts, overflow handling errors, or browser-specific rendering quirks.

Provide corrected code with clear before/after comparison, explain what was wrong and why the fix works, and offer prevention strategies. Prioritize understanding root causes over quick patches; avoid complete rewrites unless absolutely necessary.

## Context

{{layout-problem}}

## Output

Structure your response as:

**Problem Identification**  
Summarize the core layout issue and visible symptoms.

**Root Cause Analysis**  
Explain what DevTools inspection reveals: computed styles, box model visualization, stacking context, or layout overlay findings.

**Corrected Code**  
```css
/* Before */...

/* After */... // inline comments explaining each change
```

**Why This Fix Works** 
Explain the technical reason the correction resolves the problem and how browsers will now render it correctly.

**Prevention Tips** 
- Bullet points with strategies to avoid this class of issue
- Best practices for maintainable CSS architecture
```

## 用法 / Usage
- 必填變數 / Variables: {{layout-problem}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Academic_Research_Synthesis_Pipeline · Writing_Quality_Multi_Dimension_Checker
- 適用 / Use when: The CSS Layout Debugging Prompt is a free AI prompt that walks through methodical DevTools-based analysis to i…
