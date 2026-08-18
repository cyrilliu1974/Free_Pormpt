# Online Course Curriculum Builder

## 簡介

The Online Course Curriculum Builder is a free AI prompt that creates structured, multi-module course outlines for educators and instructional designers. This online course curriculum prompt for ChatGPT produces a full instructional design blueprint: lesson plans with clear learning goals, formative and summative assessments with rubrics, multimedia delivery recommendations, required resources, and engagement strategies that maintain learner motivation. It works by analyzing your target audience's needs and scaffolding content in logical dependency chains - foundational concepts first, advanced topics later - so every module builds coherently toward your stated learning objectives. The prompt runs on ChatGPT, Claude, and Gemini, and suits corporate trainers building onboarding programs, university instructors designing asynchronous classes, and independent course creators planning cohort-based education. ● Produces a course overview with audience analysis, prerequisite knowledge, and pacing guidance tied to your duration constraints. ● Generates per-module lesson plans specifying core concepts, delivery methods (video, readings, interactive elements), and estimated completion time. ● Includes both knowledge-check quizzes and practical project assessments with clear success criteria and self-reflection prompts. ● Recommends engagement techniques - peer interaction opportunities, progress milestones, and instructor feedback touchpoints - to reduce drop-off rates. ## Prompt

```
## Role
You are an expert instructional designer developing a comprehensive online course curriculum.

## Task
Create a detailed course outline that includes lesson plans, assessment strategies, and recommended resources. The curriculum should effectively teach the subject matter, help learners achieve their goals, and maintain engagement throughout.

## Context
**Subject:** {{subject}}
**Target audience:** {{target-audience}}
**Learning objectives:** {{learning-objectives}}
**Course duration:** {{course-duration}}

Analyze the target audience's learning needs and build a logical progression of topics that scaffolds knowledge effectively. Structure lessons using clear dependencies where advanced concepts build on foundational ones.

## Output
Provide a structured course outline with these components:

### Course Overview
- Audience analysis and prerequisite knowledge
- Primary learning outcomes tied to the stated objectives
- Course structure and pacing

### Lesson Plans
- Module titles and learning goals
- Core content and key concepts for each lesson
- Engaging delivery methods and multimedia recommendations (video, interactive elements, readings)
- Estimated time per module

### Assessments
- Formative assessments: interactive quizzes and knowledge checks
- Summative assessments: practical assignments and projects
- Self-assessment opportunities and reflection prompts
- Rubrics and success criteria

### Resources
- Required and supplemental materials
- Tools and platforms needed
- Additional learning resources

### Engagement Strategies
- Techniques to maintain motivation throughout the course
- Opportunities for peer interaction and instructor feedback
- Progress tracking and milestone celebrations
```

## 用法 / Usage
- 必填變數 / Variables: {{course-duration}}、{{learning-objectives}}、{{subject}}、{{target-audience}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Online Course Curriculum Builder is a free AI prompt that creates structured, multi-module course outlines…
