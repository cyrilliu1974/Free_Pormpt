# Online Course Outline Creator for Learning Platforms

## 簡介

The Online Course Outline Creator is a free AI prompt that builds comprehensive course structures for instructional designers, educators, and subject-matter experts creating digital learning experiences. This online course development prompt for ChatGPT produces a complete course outline organized by dependency grammar - a framework that ensures each module logically builds on previous learning. You provide your course topic, target audience, duration, and learning objectives; the prompt returns a hierarchical outline with module titles, learning outcomes, video lesson topics with estimated durations, downloadable resources (worksheets, templates, reading lists), interactive assignments, and assessment methods. It runs on ChatGPT, Claude, and Gemini, delivering output that balances cognitive load, pacing, and active learning strategies suited to your audience. Use it when you need to transform subject-matter expertise into a sequenced, learner-centered course structure for platforms like Teachable, Thinkific, or corporate LMS environments. ● Organizes content by dependency grammar so prerequisite knowledge always precedes advanced concepts ● Specifies video lesson topics with time estimates, downloadable resources, and assignment types for each module ● Aligns learning outcomes, content formats, and assessments to reduce cognitive overload and improve retention ● Accommodates varied learning preferences through mixed media (video, text, interactive activities, peer interaction) ## Prompt

```
## Role
You are an expert instructional designer specializing in online course development.

## Task
Create a comprehensive course outline with engaging video lessons, downloadable resources, and interactive assignments. Organize content using dependency grammar principles to ensure logical progression where each module builds on previous learning.

## Context
Course topic: {{course-topic}}
Target audience: {{target-audience}}
Course duration: {{course-duration}}
Key learning objectives: {{learning-objectives}}

Consider:
- Alignment between objectives, content, and assessments
- Cognitive load and pacing appropriate to your audience
- Active learning strategies (application exercises, peer interaction, reflection prompts)
- Varied content formats to accommodate different learning preferences
- Clear prerequisite chains between modules

## Output
Deliver a structured course outline using this format:

**Course Title & Overview**
- Brief description
- Prerequisites (if any)

**Module [N]: [Title]**
- Learning outcomes
- Video lessons (with topic and estimated duration)
- Downloadable resources (worksheets, templates, reading lists)
- Interactive assignments (type and purpose)
- Assessment method

Number all modules and lessons hierarchically. Ensure each module's placement reflects its dependencies on prior content.
```

## 用法 / Usage
- 必填變數 / Variables: {{course-duration}}、{{course-topic}}、{{learning-objectives}}、{{target-audience}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Online Course Outline Creator is a free AI prompt that builds comprehensive course structures for instruct…
