# Personalized Study Guide Generator for Students

## 簡介

The Personalized Study Guide Generator is a free AI prompt that creates custom study materials matched to a student's learning style, knowledge level, and study goals. This study guide prompt for ChatGPT analyzes any subject to extract core concepts, essential terminology, and practice questions, then structures them for maximum comprehension and retention. It runs on ChatGPT, Claude, Gemini, and Grok, delivering organized study plans for everything from high-school biology to graduate-level statistics. Use it whenever you need study materials that respect how you learn best - visual, auditory, kinesthetic, or reading-focused - and that balance review with new content appropriate to your current mastery. ● Identifies core concepts, essential terms, and common misconceptions specific to the subject you provide. ● Adapts content format to match your learning style - whether you need visual diagrams, auditory mnemonics, kinesthetic examples, or written summaries. ● Generates practice questions that progress from fundamental to advanced, targeting your declared focus areas and difficulty zones. ● Organizes output into labeled sections (Key Concepts, Important Terms, Practice Questions) so you can navigate and review efficiently during timed study sessions. ## Prompt

```
## Role
You are an expert educational content creator specializing in personalized study guides.

## Task
Create a comprehensive, tailored study guide for {{subject}} that adapts to the student's learning approach and current knowledge level.

## Context
Student profile:
- Learning approach: {{learning-style}}
- Current knowledge level: {{knowledge-level}}
- Focus areas (topics of interest or difficulty): {{focus-areas}}
- Preferred study duration per session: {{study-duration}}

Analyze the subject matter to identify:
- Core concepts that form the foundation
- Essential terminology and definitions
- Connections between ideas
- Common misconceptions or challenging areas

Adapt content presentation to match the stated learning approach (visual, auditory, kinesthetic, reading/writing, or mixed). Balance review of fundamentals with introduction of new material appropriate to the knowledge level.

## Output
Deliver the study guide as a bullet-point list organized into clearly labeled sections:

**Key Concepts**
- [Core ideas explained in a way that suits the learning approach]

**Important Terms**
- [Definitions and context for essential vocabulary]

**Practice Questions**
- [Questions progressing from fundamental to advanced, targeting focus areas]

Ensure each section is easy to navigate and the difficulty curve matches the student's current level.
```

## 用法 / Usage
- 必填變數 / Variables: {{focus-areas}}、{{knowledge-level}}、{{learning-style}}、{{study-duration}}、{{subject}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Personalized Study Guide Generator is a free AI prompt that creates custom study materials matched to a st…
