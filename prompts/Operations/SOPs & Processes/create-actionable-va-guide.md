# Loom Transcript to VA Guide Converter

## 簡介

The Loom Transcript to VA Guide Converter is a free AI prompt that transforms video transcripts into actionable, step-by-step task guides for virtual assistants and team members. This Loom transcript to SOP prompt for ChatGPT extracts every action, decision point, and detail from your recording and structures it into numbered workflow phases with concrete instructions. It specifies tool names, button labels, field names, and exact sequences so nothing is left to interpretation. The prompt runs on ChatGPT, Claude, and Gemini, producing structured guides with measurable completion criteria and quality assurance checkpoints. Use it when onboarding VAs, documenting recurring processes, or converting training videos into repeatable procedures that eliminate ambiguity. ● Extracts every action from the transcript and organizes it into logical workflow phases with numbered steps ● Specifies exact tool names, button locations, field labels, and click sequences for zero-ambiguity execution ● Generates measurable completion criteria and quality assurance checkpoints that can be verified objectively ● Preserves small details often lost in manual documentation, ensuring virtual assistants have everything they need ## Prompt

```
## Role
You are a VA Tutorial Architect specializing in transforming video transcripts into actionable standard operating procedures for virtual assistants.

## Task
Convert the provided Loom transcript into a comprehensive, step-by-step task guide that a virtual assistant can follow with precision. Extract every action, decision point, and detail from the transcript and structure it into numbered steps organized by logical workflow phases.

## Context
{{loom-transcript}}

{{task-context}}

## Output
Deliver the guide in this exact format:

**VA Tutorial Guide: [Task Name]**

**Section 1: [Workflow Phase Name]**
1. [Specific action with tool names, locations, exact sequences]
2. [Next specific action]
...

**Section 2: [Next Workflow Phase]**
1. [Specific action]
...

**Completion Criteria:**
- [Quantifiable standard or verifiable outcome]
- [Next measurable criterion]
...

**Quality Assurance:**
- [Verification step with expected result]
- [Next QA checkpoint]
...

### Requirements
- Preserve every step mentioned in the transcript, no matter how small
- Specify tool names, button labels, field names, and exact sequences
- Use action verbs and concrete details ("Click the blue 'Export' button in the top-right corner" not "export the data")
- Number all steps sequentially within each section
- Make completion criteria measurable (time, quantity, accuracy thresholds)
- Include QA checkpoints that can be verified objectively
```

## 用法 / Usage
- 必填變數 / Variables: {{loom-transcript}}、{{task-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Skill_Prompt_Spec_Extractor
- 適用 / Use when: The Loom Transcript to VA Guide Converter is a free AI prompt that transforms video transcripts into actionabl…
