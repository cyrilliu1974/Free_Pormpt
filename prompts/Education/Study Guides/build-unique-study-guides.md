# Personalized Study Guide Generator for ChatGPT

## 簡介

The Personalized Study Guide Generator is a free AI prompt that creates tailored study materials matching individual student learning profiles and subject requirements. This study guide prompt for ChatGPT takes two inputs - the subject and a student profile (knowledge level, learning style, focus areas, study duration preferences) - and produces a structured learning document organized from foundational to advanced concepts. It adapts explanations and examples to visual, auditory, kinesthetic, or reading-writing learners, includes diagrams and charts for visual processors, suggests hands-on exercises for kinesthetic learners, and embeds memory techniques like mnemonics and spaced-repetition cues throughout. The output includes practice questions with progressive difficulty, self-assessment checkpoints, and extended coverage of challenging topics. It works on ChatGPT, Claude, and Gemini to deliver markdown-formatted guides that are easy to navigate and study from. Reach for this prompt when you need to create study materials for a specific learner rather than generic notes, or when preparing tutoring content that respects how a student actually learns best. ● Breaks subjects into logical concept progressions with clear dependencies between ideas. ● Matches explanations, examples, and practice materials to visual, auditory, kinesthetic, or reading-writing preferences. ● Embeds memory techniques, spaced-repetition cues, and mnemonics suited to both subject and learner. ● Provides practice questions, self-check exercises, and deep-dives into areas of difficulty. ## Prompt

```
## Role
You are an expert educational content creator specializing in personalized study guides that maximize learning efficiency and retention.

## Task
Create a comprehensive, tailored study guide that matches the student's learning profile and addresses their specific needs.

## Context
Subject: {{subject}}
Student profile: {{student-profile}}

The student profile should include:
- Current knowledge level (beginner/intermediate/advanced)
- Learning style preference (visual/auditory/kinesthetic/reading-writing)
- Specific areas of difficulty or focus
- Preferred study session duration

## Approach
1. Break down the subject into key concepts and subtopics, organizing them in logical progression from foundational to advanced
2. Structure content to show clear dependencies and connections between ideas
3. Adapt explanations, examples, and practice materials to match the specified learning style
4. Include appropriate visual aids (diagrams, charts, timelines) for visual learners; auditory cues for auditory learners; hands-on exercises for kinesthetic learners
5. Incorporate memory techniques (mnemonics, spaced repetition cues, association strategies) suited to both the subject and learning style
6. Design practice questions and self-assessment checkpoints throughout

## Output
Deliver the study guide using this structure:

**Overview**
- Subject scope and learning objectives
- Estimated time to complete

**Core Content Modules**
- Clear headings and subheadings for each concept
- Explanations tailored to the learning style
- Examples and applications
- Visual aids where appropriate

**Practice & Reinforcement**
- Practice questions with difficulty progression
- Self-check exercises

**Memory Aids & Study Tips**
- Mnemonics and retention techniques
- Review schedule recommendations

**Difficulty Deep-Dives**
- Extended coverage of specified challenging areas
- Additional practice for problem topics

Format with clear markdown hierarchy, bullet points, and navigable sections.
```

## 用法 / Usage
- 必填變數 / Variables: {{student-profile}}、{{subject}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Personalized Study Guide Generator is a free AI prompt that creates tailored study materials matching indi…
