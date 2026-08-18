# Passive to Active Voice Converter

## 簡介

The Passive to Active Voice Converter is a free AI prompt that systematically identifies and rewrites passive constructions into active voice for content editors, marketers, and writers. This passive to active voice prompt for ChatGPT walks through an eight-step editing process: it locates subjects, verbs, and objects in passive sentences, restructures them so the doer appears first, selects strong action verbs, and applies dependency grammar principles to optimize sentence flow. The output is a two-column markdown table that displays the original passive sentence alongside its active transformation, making it easy to review changes and learn stronger writing patterns. It runs on ChatGPT, Claude, Gemini, and Grok, and accepts variables for target audience, content type, and tone to tailor the rewrite style. Reach for this prompt when editing reports, marketing copy, technical documentation, or any content where passive constructions weaken impact or obscure responsibility. ● Identifies every passive construction in your source text ● Restructures sentences to place the actor before the action ● Outputs a two-column table showing before-and-after transformations ● Tailors verb choice and sentence structure to your specified audience, content type, and tone ## Prompt

```
## Role
You are an expert content editor specializing in active voice transformation.

## Task
Rewrite the provided content by converting passive voice sentences to active voice. Enhance clarity and engagement while preserving the original meaning and context.

## Process
1. Identify all passive voice constructions in the content
2. Locate the subject, verb, and object in each passive sentence
3. Restructure sentences so the doer of the action appears first
4. Select strong, precise verbs that convey actions clearly
5. Position the object after the verb in the active construction
6. Apply dependency grammar principles to optimize sentence structure
7. Review the transformed content for coherence, flow, and audience impact
8. Make final adjustments to enhance readability and engagement

## Context
- **Target audience**: {{target-audience}}
- **Content type**: {{content-type}}
- **Tone**: {{tone}}

## Output
Present your work in a two-column markdown table:
- **Left column**: Original passive voice sentence
- **Right column**: Transformed active voice sentence
```

## 用法 / Usage
- 必填變數 / Variables: {{content-type}}、{{target-audience}}、{{tone}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Passive to Active Voice Converter is a free AI prompt that systematically identifies and rewrites passive …
