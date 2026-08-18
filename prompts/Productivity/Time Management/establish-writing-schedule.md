# Writing Schedule Builder for Book Projects

## 簡介

The Writing Schedule Builder for Book Projects is a free AI prompt that creates structured, week-by-week writing schedules for authors working to complete a book manuscript without burnout. This writing schedule prompt for ChatGPT calculates required daily and weekly word counts based on your target completion date, available writing days, and personal writing speed, then delivers a markdown table mapping out at least four weeks of sustainable goals. It factors in buffer time for revisions, assesses feasibility against your stated productivity rate, and flags potential bottlenecks like holidays or high-intensity periods. Authors use it to turn vague book deadlines into actionable day-by-day plans that prevent overwhelm while maintaining steady momentum. The prompt runs on ChatGPT, Claude, Gemini, and Grok, and accepts details like book title, available days per week, target word count, desired timeframe, and average writing speed. This prompt is for novelists, non-fiction authors, thesis writers, and content creators who need a realistic timeline that respects their capacity while ensuring consistent progress. ● Calculates daily and weekly word-count targets based on timeline, availability, and personal writing speed ● Delivers a multi-week markdown table showing exactly which days to write and how many words to produce ● Builds in 80-85% capacity planning to accommodate revisions, off-days, and unexpected interruptions ● Includes usage instructions, adjustment triggers, and recalibration advice for handling missed days ## Prompt

```
## Role
You are an expert writing coach specializing in sustainable authorship schedules.

## Task
Create a structured weekly writing schedule in table format that balances consistent progress with realistic workload to complete a book on time without burnout.

## Context
Book project details:
{{book-project-details}}

Include in your project details: book title, available writing days per week, target word count, desired completion timeframe in weeks, and average writing speed in words per hour.

## Process
1. Calculate the required weekly and daily word counts based on the timeline and availability
2. Assess the feasibility against the stated writing speed
3. Identify potential bottlenecks (holidays, high-intensity periods)
4. Build in buffer time for revisions and off-days (aim for 80-85% capacity)
5. Distribute word count goals across available days to maintain steady momentum

## Output
Provide a brief introduction (3-4 sentences) explaining how to use the schedule, when to adjust targets, and how to handle missed days.

Then present a markdown table with two columns:
- **Writing Days** (e.g., Monday, Wednesday, Friday or Week 1 Day 1, Week 1 Day 2)
- **Word Count Goals** (daily target with weekly cumulative total)

Include at least 4 weeks of the schedule to establish the pattern. Add a closing note on monitoring progress and recalibrating as needed.
```

## 用法 / Usage
- 必填變數 / Variables: {{book-project-details}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Context_Audit&Triage
- 適用 / Use when: The Writing Schedule Builder for Book Projects is a free AI prompt that creates structured, week-by-week writi…
