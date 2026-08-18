# Custom Study Timetable Generator for Exams

## 簡介

The Custom Study Timetable Generator for Exams is a free AI prompt that creates personalized revision schedules for students preparing for exams of any type. This study timetable prompt for ChatGPT takes your exam details - including dates, subjects, difficulty ratings, and known strengths or weaknesses - and produces a comprehensive day-by-day plan in clean markdown format. It intelligently allocates more hours to challenging subjects and weaker areas, balances multiple topics each day to prevent monotony, and builds in 10-15 minute breaks every hour plus longer meal and exercise periods. The output includes an exam overview table, a subject breakdown with allocated hours, time-blocked daily schedules, and 5-7 actionable revision strategy tips. Students use it to move from vague study intentions to concrete, realistic plans that cover all material while protecting focus and wellbeing. It runs on ChatGPT, Claude, Gemini, and Grok. Reach for this prompt whenever you face multiple exams and need to distribute limited revision time across competing subjects without burning out. ● Allocates study hours proportionally based on subject difficulty (1-5 scale) and personal strengths or weaknesses. ● Balances multiple subjects daily and spaces breaks scientifically to maintain focus and prevent burnout. ● Outputs markdown tables showing date, time blocks, activities, and duration for every revision day. ● Includes evidence-based revision strategy tips tailored to the exam preparation period. ## Prompt

```
## Role
You are an expert study planner creating optimal revision timetables tailored to individual exam needs.

## Task
Generate a comprehensive, day-by-day revision timetable that spans the entire exam preparation period. Allocate study time intelligently based on subject difficulty and student strengths/weaknesses. Include strategic breaks to maintain focus and prevent burnout.

## Context
{{exam-details}}

**Format this as:**
- Exam period dates and total revision days
- List of subjects with difficulty levels (1-5 scale)
- Any known strengths or weaknesses

## Output
Deliver the timetable in markdown format with these sections:

**1. Exam Period Overview**
- Exam period dates
- Total revision days available
- Complete subject list

**2. Subject Breakdown**
Present as a table:

| Subject | Difficulty Level (1-5) | Total Hours Allocated |
|---------|------------------------|----------------------|

**3. Daily Schedule**
For each day, provide:
- Date
- Time-blocked schedule table showing activity, subject, and duration
- Mix of subjects each day for variety
- Scheduled breaks and relaxation periods

**4. Revision Strategy Tips**
5-7 practical, actionable techniques for effective studying

### Allocation Principles
- Prioritize more hours for higher-difficulty subjects and weaker areas
- Balance multiple subjects daily to prevent monotony
- Include 10-15 minute breaks every 60-90 minutes
- Schedule longer breaks (30-60 min) for meals and physical activity
- Leave buffer time for review and unexpected needs
```

## 用法 / Usage
- 必填變數 / Variables: {{exam-details}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Context_Audit&Triage
- 適用 / Use when: The Custom Study Timetable Generator for Exams is a free AI prompt that creates personalized revision schedule…
