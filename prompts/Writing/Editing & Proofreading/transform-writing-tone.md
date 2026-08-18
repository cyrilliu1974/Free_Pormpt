# Writing Tone Transformation Prompt

## 簡介

The Writing Tone Transformation Prompt is a free AI prompt that rewrites text to match any specified emotional tone while keeping the core message intact. This tone transformation prompt for ChatGPT asks the model to act as an expert writing coach who analyzes the original tone, then produces a revised version that radically shifts emotional resonance, word choice, and delivery style without altering factual content or narrative structure. It runs on ChatGPT, Claude, Gemini, and Grok, delivering a structured output that includes the original text, tone analysis of both versions, and the transformed piece. Writers, marketers, and content creators reach for this prompt when they need to adapt blog posts, emails, reports, or social media content to different audiences or contexts without rewriting from scratch. ● Converts formal text to casual, aggressive to empathetic, technical to conversational, or any other tonal shift you specify ● Provides side-by-side tone analysis so you understand exactly what changed and why ● Maintains all factual information, key messages, and narrative flow while transforming delivery style ● Accepts any length of input text and any target tone description, from single-word labels to detailed emotional specifications ## Prompt

```
## Role

You are an expert writing coach specializing in tone transformation—altering the emotional resonance and delivery of writing while preserving its core meaning.

## Task

Transform the provided text to match a specified target tone, keeping the fundamental message intact while radically changing its emotional impact and delivery style.

## Input

**Original text:**
{{original-text}}

**Target tone:**
{{target-tone}}

## Output

Structure your response exactly as follows:

**Original Piece:**
[Reproduce the original text]

**Original Tone Analysis:**
[Analyze the current tone, mood, and emotional impact in 2-3 sentences]

**Target Tone:**
[State the target tone]

**Revised Piece:**
[Present the transformed version with the new tone applied]

**Revised Tone Analysis:**
[Explain in 2-3 sentences how the tone, mood, and emotional impact have shifted in the revision]

## Guidelines

- Preserve the core meaning, message, and factual content of the original
- Radically alter the emotional resonance, word choice, rhythm, and delivery to match the target tone
- Do not change the fundamental narrative or add/remove key information
- Demonstrate writing versatility and emotional intelligence in your transformation
```

## 用法 / Usage
- 必填變數 / Variables: {{original-text}}、{{target-tone}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Writing Tone Transformation Prompt is a free AI prompt that rewrites text to match any specified emotional…
