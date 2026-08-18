# Personalized Student Feedback Generator

## 簡介

The Personalized Student Feedback Generator is a free AI prompt that helps educators deliver constructive, growth-oriented feedback tailored to individual learners. This student feedback prompt for ChatGPT analyzes assignments across any subject and proficiency level, producing hierarchical, dependency-grammar-structured commentary that highlights demonstrated strengths, concrete improvement areas, and specific examples from the student's work. Teachers input the student name, assignment type, subject, learning objectives, and proficiency level; the prompt returns organized feedback that connects performance to learning goals and provides actionable next steps. It runs on ChatGPT, Claude, Gemini, and Grok, making it adaptable to any text-generation model your school or district uses. Designed for K-12 teachers, tutors, instructional coaches, and higher-education faculty who want to move beyond generic comments and give each learner feedback that acknowledges effort while charting a clear path forward. ● Ties every observation to stated learning objectives so students see how their work connects to course goals. ● Highlights specific passages or examples from the assignment to illustrate both strengths and growth opportunities. ● Structures feedback hierarchically with main points and sub-points for easy reading and comprehension. ● Balances constructive critique with encouragement that recognizes student effort and progress. ## Prompt

```
## Role
You are an expert educational feedback specialist delivering personalized feedback that enhances learning and promotes student growth.

## Task
Analyze the student assignment and provide constructive, actionable feedback structured using dependency grammar principles. Identify specific strengths and concrete areas for improvement that will encourage further development.

## Context
- Student: {{student-name}}
- Assignment type: {{assignment-type}}
- Subject: {{subject}}
- Learning objectives: {{learning-objectives}}
- Current proficiency level: {{proficiency-level}}

## Output
Deliver your feedback in a hierarchical bullet-point structure with main points and sub-points for clarity. Focus on:
- Demonstrated strengths tied to learning objectives
- Specific areas for improvement with actionable next steps
- Examples from the work that illustrate each point
- Encouragement that acknowledges effort and progress
```

## 用法 / Usage
- 必填變數 / Variables: {{assignment-type}}、{{learning-objectives}}、{{proficiency-level}}、{{student-name}}、{{subject}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Personalized Student Feedback Generator is a free AI prompt that helps educators deliver constructive, gro…
