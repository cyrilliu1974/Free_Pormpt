# Exam Prep Study Plan Builder

## 簡介

The Exam Prep Study Plan Builder is a free AI prompt that creates structured, adaptive study schedules for students, tutors, and educational consultants preparing for any exam. This exam prep prompt for ChatGPT guides the model to act as an expert educational consultant who sequences topics using dependency grammar principles - foundational concepts are scheduled before advanced material that builds on them. You provide the exam name, student background, weekly study time, key topics, and available resources; the AI returns a markdown study schedule table (week, topics, resources, time allocation, prerequisites) plus a bullet list of retention techniques, motivation tactics, pacing strategies, and exam-day tips. It works on ChatGPT, Claude, Gemini, and Grok, adapting to any exam from high-school finals to professional certifications. Reach for this prompt when you need a logical, student-centered study roadmap that maximizes retention and understanding within real-world time constraints. ● Sequences topics so prerequisites come first, ensuring students master foundational concepts before tackling advanced material. ● Outputs a markdown table with weekly phases, resource recommendations, time allocations, and clear dependencies. ● Includes spaced repetition, active recall, motivation tactics, and exam-day preparation advice in every plan. ● Adapts to any learner profile - high school, undergraduate, professional certification - and any available study time per week. ## Prompt

```
## Role

You are an expert educational consultant specializing in exam preparation and study plan design.

## Task

Create a comprehensive study plan tailored to the exam and learner profile provided. Structure the plan using dependency grammar principles—sequence topics so that foundational concepts precede those that build on them, ensuring logical progression and mastery.

## Context

**Exam details:**  
{{exam-and-learner-profile}}  
(Include: exam name, target student level/background, available study time per week, key topics to cover, and available resources such as textbooks, online courses, practice tests, etc.)

## Output

Deliver your study plan in two parts:

1. **Study schedule table** (markdown format) with columns:  
   - Week / Phase  
   - Topic(s)  
   - Resources  
   - Time allocation  
   - Prerequisites / Dependencies  

2. **Study strategies and tips** (bullet-point list) covering:  
   - Retention techniques (spaced repetition, active recall, etc.)  
   - Motivation and accountability tactics  
   - Adaptation strategies for different learning paces  
   - Exam-day preparation advice

Ensure the plan is adaptable, motivating, and designed to maximize retention and understanding.
```

## 用法 / Usage
- 必填變數 / Variables: {{exam-and-learner-profile}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Exam Prep Study Plan Builder is a free AI prompt that creates structured, adaptive study schedules for stu…
