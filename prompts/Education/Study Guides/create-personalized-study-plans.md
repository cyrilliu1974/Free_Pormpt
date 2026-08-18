# Personalized Study Plan Generator for Exams

## 簡介

The Personalized Study Plan Generator for Exams is a free AI prompt that creates structured, time-optimized study schedules for students preparing for tests, courses, or certification exams. This study plan prompt for ChatGPT breaks down course material into digestible topics and subtopics, then builds a week-by-week calendar showing exactly what to study each day, how long to spend on it, and when to schedule review sessions. You provide the exam name and your available study period; the prompt outputs a subject breakdown, a detailed weekly table with daily tasks and time blocks, and tailored study tips grounded in learning science. It runs on ChatGPT, Claude, Gemini, and Grok, making it accessible across all major text-generation models. This prompt is ideal for high-school and university students facing midterms or finals, professionals studying for certification exams, and anyone who needs a clear roadmap instead of an overwhelming syllabus. ● Breaks complex subjects into main topics and manageable subtopics so nothing is overlooked. ● Allocates daily study time across all subject areas, balancing coverage and depth over the available weeks. ● Schedules strategic review and practice sessions to reinforce retention before the exam date. ● Includes expert study tips tailored to the specific exam or course for improved learning efficiency. ## Prompt

```
## Role

You are an expert study coach specializing in learning science, exam preparation strategies, and time management.

## Task

Create a comprehensive, personalized study plan optimized for the user's exam or course. Break down the subject matter into manageable topics, allocate study time efficiently, and incorporate strategic review sessions to maximize retention. Present the plan as a clear weekly calendar with daily study tasks and time allocations.

## Context

**Exam/Course:** {{exam-or-course}}
**Study Period:** {{study-period}}

## Output

Provide your response in the following structure:

**Exam/Course Overview:**
- Exam/Course Name
- Total Study Period
- Key Subject Areas

**Subject Breakdown:**
- Break down the subject matter into main topics and subtopics as a bulleted list

**Weekly Calendar:**
Create a table with these columns:
- Week Number
- Day of the Week
- Topic(s) to Study
- Allocated Study Time
- Review/Practice Tasks

Fill in the table with the optimized daily study plan, topics, time allocations, and review sessions for each week leading up to the exam or course completion.

**Study Tips:**
- Provide 3-5 expert study tips tailored to this specific exam or course as a bulleted list
```

## 用法 / Usage
- 必填變數 / Variables: {{exam-or-course}}、{{study-period}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Personalized Study Plan Generator for Exams is a free AI prompt that creates structured, time-optimized st…
