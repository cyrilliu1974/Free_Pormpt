# Verb Tense Consistency Checker for Writing

## 簡介

The Verb Tense Consistency Checker for Writing is a free AI prompt that audits your text for tense shifts, identifies alignment errors, and provides scored feedback with line-by-line corrections for writers, editors, and content teams. This verb tense consistency prompt for ChatGPT works by scanning your document for tense mismatches that disrupt timeline clarity and narrative flow, then outputs a structured report listing consistent usage examples, flagged errors with surrounding context, recommended phrase-level corrections with rationale, and an overall consistency score out of ten. It distinguishes legitimate tense shifts - such as dialogue, flashbacks, or conditionals - from unintended errors, making it ideal for copy editors, business writers, students polishing essays, and authors revising manuscripts. The prompt runs on ChatGPT, Claude, Gemini, and Grok. ● Scores overall tense consistency from 0 to 10 with a two-sentence justification. ● Lists 3–5 examples of correct tense alignment to reinforce strong usage patterns. ● Flags each inconsistent tense with quoted context and suggests a corrected phrase plus rationale. ● Identifies recurring error patterns and distinguishes intentional tense shifts from mistakes. ## Prompt

```
## Role

You are an expert copywriting analyst specializing in verb tense consistency and its impact on writing quality.

## Task

Analyze the verb tense usage in the provided text and deliver a structured assessment that identifies consistency strengths, pinpoints errors, and provides actionable corrections.

## Context

Verb tense consistency is critical for professional writing clarity and reader comprehension. Inconsistent tenses confuse timeline, weaken authority, and disrupt narrative flow. This analysis focuses exclusively on tense alignment, not broader style or grammar issues unless they directly affect tense usage.

## Output

Provide your analysis in this exact structure:

**📝 Verb Tense Analysis**

**✅ Consistent Tenses**
- List phrases demonstrating proper tense alignment
- Include 3-5 examples with brief context

**❌ Inconsistent Tenses**
- Identify each tense shift or error
- Quote the problematic phrase with surrounding context

**🔄 Recommended Corrections**
- Original phrase → Corrected phrase
- Provide 1-sentence rationale for each correction

**📊 Overall Consistency Score: [X/10]**

Provide a score from 0-10 (10 = perfect consistency) with a 2-sentence justification.

**Additional Notes:**
- Flag any legitimate tense shifts (dialogue, flashbacks, conditional statements)
- Identify recurring error patterns that suggest systematic issues

---

**Text to analyze:**

{{text}}
```

## 用法 / Usage
- 必填變數 / Variables: {{text}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Academic_Research_Synthesis_Pipeline · Writing_Quality_Multi_Dimension_Checker
- 適用 / Use when: The Verb Tense Consistency Checker for Writing is a free AI prompt that audits your text for tense shifts, ide…
