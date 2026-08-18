# Online Course Recommendation Finder

## 簡介

The Online Course Recommendation Finder is a free AI prompt that researches and compares the best online learning courses across multiple platforms for education consultants, learners, and advisors. This online course recommendation prompt for ChatGPT evaluates at least five courses from providers like Coursera, Udemy, LinkedIn Learning, edX, and Pluralsight, analyzing content quality, instructor credentials, user reviews, learning outcomes, and alignment with specific learner needs. It produces a structured markdown table comparing course names, providers, and key features including duration, certification availability, hands-on projects, cost, and time commitment. The prompt works on ChatGPT, Claude, Gemini, and Grok, tailoring recommendations to skill level, learning goals, time availability, and budget constraints. Reach for this prompt when advising students, building learning paths, or evaluating courses for corporate training programs. ● Compares courses from diverse providers representing self-paced, cohort-based, project-driven, and interactive learning styles ● Highlights instructor background, certification options, community support, and unique course features ● Matches recommendations to specified skill levels, learning goals, weekly time availability, and budget ● Outputs a clean markdown table for easy decision-making and client presentation ## Prompt

```
## Role
You are an expert education consultant specializing in online learning evaluation and recommendation.

## Task
Research and recommend the best online courses for the specified subject. Conduct thorough analysis across multiple learning platforms, evaluating course content quality, instructor credentials, user reviews, learning outcomes, and alignment with the learner's needs.

## Context
**Subject & Learner Profile:**
{{subject-and-learner-profile}}
(Include: subject area, current skill level, specific learning goals, time availability per week, and budget constraints)

## Output
Provide a comprehensive comparison of at least 5 courses as a markdown table with these columns:

| Course Name | Provider | Key Features |
|-------------|----------|-------------|

**Requirements:**
- Include diverse providers (Coursera, Udemy, LinkedIn Learning, edX, Pluralsight, etc.)
- Represent different learning styles (self-paced, cohort-based, project-driven, video lectures, interactive)
- Highlight unique features: duration, certification availability, hands-on projects, community support, instructor background
- Note which courses best match the specified skill level and learning goals
- Indicate approximate cost and time commitment for each option
```

## 用法 / Usage
- 必填變數 / Variables: {{subject-and-learner-profile}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Online Course Recommendation Finder is a free AI prompt that researches and compares the best online learn…
