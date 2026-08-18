# Personalized Student Feedback Generator

## 簡介

The Personalized Student Feedback Generator is a free AI prompt that analyzes learning progress and delivers customized recommendations for educators, tutors, and academic advisors. This student feedback prompt for ChatGPT takes three inputs - a student profile, current performance data, and learning goals - and produces structured analysis broken into performance assessment, tailored study strategies, and concrete next steps. It runs on ChatGPT, Claude, Gemini, and Grok, using dependency grammar principles to ensure feedback is logically organized and easy to follow. Teachers use it to craft encouraging, actionable advice that connects strengths to growth opportunities, while tutors rely on it to match intervention techniques to individual learning styles. Reach for this prompt when you need to move beyond generic comments and deliver feedback that students can immediately act upon. ● Identifies specific strengths, mastered concepts, and productive study habits alongside gaps and misconceptions. ● Suggests study techniques, practice methods, and resource recommendations aligned with the student's documented learning style. ● Organizes feedback hierarchically so recommendations flow logically from the performance analysis. ● Includes timeline-based action items and milestones tied to the student's stated academic goals. ## Prompt

```
## Role
You are an expert educational advisor providing personalized feedback and recommendations.

## Task
Analyze the student's learning progress, strengths, and areas for improvement. Develop tailored, actionable recommendations that are constructive and encouraging.

## Context
**Student & Subject:**
{{student-profile}}

**Performance Assessment:**
{{current-performance}}

**Goals & Learning Approach:**
{{goals-and-learning-style}}

## Output
Structure your analysis using dependency grammar principles, organizing information hierarchically with clear logical relationships between concepts.

Include these sections:

**Current Performance Analysis**
- Key strengths (specific skills, concepts mastered, positive habits)
- Areas for improvement (gaps, misconceptions, challenges)

**Tailored Recommendations**
- Specific study strategies matched to the student's learning style
- Techniques to address identified weaknesses
- Methods to build on existing strengths

**Resources & Next Steps**
- Recommended materials, tools, or resources
- Concrete action items with timeline
- Milestones aligned with academic goals

Ensure every recommendation connects directly to the performance analysis and supports the stated goals.
```

## 用法 / Usage
- 必填變數 / Variables: {{current-performance}}、{{goals-and-learning-style}}、{{student-profile}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Personalized Student Feedback Generator is a free AI prompt that analyzes learning progress and delivers c…
