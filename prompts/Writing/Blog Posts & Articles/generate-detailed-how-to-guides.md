# How-to Guide Generator

## 簡介

The How-to Guide Generator is a free AI prompt that creates comprehensive topic trees and step-by-step guide outlines for any niche you specify. This how-to guide prompt for ChatGPT, Claude, and Gemini builds a structured hierarchy of 3–5 main topics with subtopics, then produces detailed outlines for each guide using dependency grammar principles - every step anchored by a clear action verb with modifiers that clarify how, when, and why. The prompt is designed for content creators, educators, and documentation teams who need to produce tutorial content that progresses logically from foundational to advanced skills. Each outline includes an introduction with a purpose statement, numbered steps broken into substeps, and a conclusion with a call to action, so you can draft instructional content faster without sacrificing clarity. ● Produces a multi-level topic tree that organizes niche knowledge from beginner to advanced ● Generates guide outlines with dependency grammar structure, making each step easy to follow and act on ● Includes introduction, substeps with action-verb clarity, and conclusion with next-step guidance ● Works across any niche - software tutorials, DIY projects, professional skills, hobby instruction, or business processes ## Prompt

```
## Role
You are an expert instructional designer specializing in how-to guides and tutorials.

## Task
Generate a comprehensive topic tree and detailed guide outlines for creating how-to content in {{niche}}. Apply dependency grammar principles—building each sentence and section on clear core statements with modifiers that extend meaning logically—to ensure clarity and coherence.

## Structure

**Topic Tree:** Identify 3–5 main topics within the niche, each with 3–4 subtopics that cover essential skills and common user questions. Progress from foundational to advanced concepts.

**Guide Outlines:** For each subtopic, create a step-by-step outline that:
- Opens with an introduction anchored by a clear purpose statement (dependency grammar: main clause → supporting details)
- Breaks each step into substeps, each built on a single action verb with modifiers clarifying how, when, or why
- Closes with a summary that ties back to the introduction and a concrete call to action

## Output
Format your response exactly as:

**Niche:** {{niche}}

**Topic Tree:**
- Main Topic 1
  - Subtopic 1.1
  - Subtopic 1.2
  - Subtopic 1.3
- Main Topic 2
  - Subtopic 2.1
  - Subtopic 2.2
  - Subtopic 2.3

**Guide Outlines:**

**Guide 1: [Title for Subtopic 1.1]**
1. Introduction
   - Core statement: What the guide achieves
   - Context modifiers: Why it matters, who benefits
2. Step 1: [Action Verb]
   - Substep A (Core action + method modifier)
   - Substep B (Core action + condition modifier)
3. Step 2: [Action Verb]
   - Substep A (Core action + location/tool modifier)
   - Substep B (Core action + result modifier)
4. Conclusion
   - Summary: Restate core outcome achieved
   - Call to action: Next logical step or practice exercise

**Guide 2: [Title for Subtopic 1.2]**
[Same structure as Guide 1]

Continue for all subtopics in the tree.
```

## 用法 / Usage
- 必填變數 / Variables: {{niche}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The How-to Guide Generator is a free AI prompt that creates comprehensive topic trees and step-by-step guide o…
