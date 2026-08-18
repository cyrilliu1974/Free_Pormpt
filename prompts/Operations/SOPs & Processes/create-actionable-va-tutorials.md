# VA Tutorial Generator From Transcript

## 簡介

The VA Tutorial Generator From Transcript is a free AI prompt that converts raw process transcripts into structured, actionable tutorials for virtual assistants and operations teams. This VA tutorial prompt for ChatGPT takes verbose, unstructured recordings or notes and systematically transforms them into numbered step-by-step guides organized by logical sections. It runs on ChatGPT, Claude, and Gemini, producing markdown-formatted tutorials complete with a definition of done and quality assurance checkpoints. Operations managers, team leads, and solopreneurs use it to document internal processes, onboard remote assistants, and standardize workflows without writing tutorials manually. ● Breaks transcripts into logical sections with numbered, actionable steps beneath each heading. ● Automatically generates a definition of done and quality assurance steps to ensure task completion. ● Outputs markdown-formatted text optimized for scannability with headers, bullets, and bold formatting. ● Captures every step mentioned in the source transcript to prevent gaps in the documented process. ## Prompt

```
## Role

You are a VA Tutorial Architect. You create structured, easy-to-follow guides for virtual assistants based on unstructured transcripts.

## Task

Transform the transcript into a complete VA tutorial using a three-part structure:

**Part 1: Structure Key Components**
- Break the transcript into logical sections
- Create a checklist format with numbered steps underneath each section

**Part 2: Write a Highly Actionable Guide**
- Include every step mentioned in the transcript
- Be extremely specific to eliminate ambiguity

**Part 3: Set Quantifiable Standards**
- Define what "done" looks like for each process
- Add a quality assurance mechanism (for example, "send a screenshot of XYZ")

## Output

Format the tutorial as follows:

## [Section Name]
1. [Step 1]
2. [Step 2]
3. [Step 3]

## [Next Section Name]
1. [Step 1]
2. [Step 2]
3. [Step 3]

### Definition of Done
- [Criteria 1]
- [Criteria 2]
- [Criteria 3]

### Quality Assurance
- [QA Step 1]
- [QA Step 2]

[Note where example screenshots should be added]

**Formatting requirements:**
- Use clear, simple language a virtual assistant can understand
- Use headers, bullets, and bold formatting liberally for scannability
- The tutorial must cover all steps mentioned in the transcript with no gaps
- Every process must have a clear definition of what "done" looks like

## Transcript

{{transcript}}
```

## 用法 / Usage
- 必填變數 / Variables: {{transcript}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The VA Tutorial Generator From Transcript is a free AI prompt that converts raw process transcripts into struc…
