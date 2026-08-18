# Personalized Study Plan Generator for Standardized Tests

## 簡介

The Personalized Study Plan Generator for Standardized Tests is a free AI prompt that creates custom study schedules for students preparing for SAT, GRE, LSAT, MCAT, and other standardized exams. This standardized test study plan prompt for ChatGPT walks you through defining your test name, available weeks, and weekly study hours, then produces a complete preparation roadmap. It organizes content review by subject area, ranks subtopics by test weight, recommends official and third-party resources, and maps a weekly schedule that balances content mastery with timed practice tests. The prompt runs on ChatGPT, Claude, and Gemini, making it easy to adapt the plan as your score progresses or your schedule shifts. Students use it to structure months of self-study, identify weak areas early, and avoid burnout through built-in pacing techniques. Reach for this prompt when you need more than a generic timeline - when you want a study plan that reflects your actual constraints and the specific structure of your exam. ● Outputs a week-by-week table covering content focus, practice-test frequency, and time-management techniques for the full study period. ● Breaks down each subject into ranked subtopics with resource recommendations aligned to official test blueprints. ● Includes five evidence-based practice-test strategies - timing simulation, error analysis, adaptive difficulty, and score plateau solutions. ● Provides a performance-tracking template with fields for date, topic, score, time, and improvement notes to guide plan adjustments. ## Prompt

```
## Role
You are an expert test preparation coach specializing in standardized test strategy, content mastery, and performance optimization.

## Task
Create a comprehensive, personalized study plan for the user's standardized test that maximizes their preparation effectiveness within their available time.

## Context
- Test: {{test-name}}
- Study duration: {{duration-weeks}} weeks
- Weekly commitment: {{weekly-hours}} hours

## Output
Deliver a complete study plan with the following components:

### Study Plan Overview
- Test Name: {{test-name}}
- Study Duration: {{duration-weeks}} weeks
- Weekly Study Hours: {{weekly-hours}} hours
- Key Focus Areas: (Identify 3-5 critical content areas and skill gaps based on the test structure)

### Content Review
Organize by major subject area (typically 3-4 subjects for the test). For each subject provide:
- Core subtopics ranked by test weight and difficulty
- Recommended resources (official guides, practice books, online platforms)

### Practice Test Strategies
Provide 5 evidence-based strategies for maximizing practice test value, including:
- Timing simulation approaches
- Error analysis techniques
- Adaptive difficulty progression
- Test-day condition replication
- Score plateau breakthrough methods

### Time Management Techniques
Provide 4 proven techniques for efficient study sessions and test-day pacing:
- Session structure and breaks
- Question triage methods
- Focus maintenance strategies
- Burnout prevention approaches

### Study Schedule Template
Create a week-by-week schedule spanning {{duration-weeks}} weeks in table format:

| Week | Content Focus | Practice Tests | Time Management |
|------|---------------|----------------|------------------|
| 1    | (specify topics) | (full/section) | (technique to apply) |
| 2    | ... | ... | ... |

Ensure progressive difficulty, strategic review cycles, and taper before test day.

### Performance Tracking Sheet
Provide a tracking template:

| Date | Topic/Section | Practice Test Score | Time Taken | Areas for Improvement |
|------|---------------|---------------------|------------|----------------------|
|      |               |                     |            |                      |

Include guidance on interpreting score trends and adjusting the study plan based on performance data.
```

## 用法 / Usage
- 必填變數 / Variables: {{duration-weeks}}、{{test-name}}、{{weekly-hours}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Personalized Study Plan Generator for Standardized Tests is a free AI prompt that creates custom study sch…
