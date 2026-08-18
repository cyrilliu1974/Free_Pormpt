# Weekly Stakeholder Report Template Generator

## 簡介

The Weekly Stakeholder Report Template Generator is a free AI prompt that transforms raw project updates into professional, executive-ready weekly task reports. This stakeholder report prompt for ChatGPT takes your project name, week dates, recipient list, and weekly updates - then outputs a complete email report organized into completed tasks, key achievements, issues with owners and ETAs, prioritized upcoming work, metrics, and additional notes. It runs on ChatGPT, Claude, Gemini, and Grok, delivering consistent formatting that busy stakeholders can scan in under two minutes. Teams use it to maintain weekly cadence with clients, executives, and cross-functional partners without spending an hour crafting each update from scratch. Reach for this prompt when you need to turn bullet-point status notes into a polished report that answers the four questions every stakeholder asks: What shipped? What's at risk? What's next? How are we tracking? ● Separates completed tasks, achievements, blockers, and priorities into labeled sections that executives can skim ● Formats issues with assigned owners and estimated resolution times so accountability is clear ● Includes a metrics section to surface KPIs and progress indicators when available ● Maintains a professional yet friendly tone appropriate for both internal leadership and external clients ## Prompt

```
## Role
You are a business communication expert specializing in stakeholder reports for busy executives.

## Task
Generate a concise weekly task report using the template below. Fill all sections with the information provided, keeping the tone professional and friendly, and the content scannable and actionable.

## Context
Project: {{project-name}}
Week of: {{week-start-date}}
Recipients: {{recipient-names}}
Sender: {{sender-name}}

Work completed, achievements, blockers, and priorities: {{weekly-update}}

## Output
Format the report as:

**Subject:** Weekly Task Report - {{project-name}} - Week of {{week-start-date}}

Hi {{recipient-names}},

Here is the weekly task report for {{project-name}} for the week of {{week-start-date}}:

**Completed Tasks:**
- [List completed tasks from the weekly update]

**Key Achievements:**
- [Extract significant accomplishments or milestones]

**Issues/Blockers:**
- [List problems with owner and estimated resolution time in format: Issue [Owner, ETA]]

**Priorities for Upcoming Week:**
1. [Top priority with owner]
2. [Second priority with owner]
3. [Third priority with owner]

**Metrics:**
- [Include relevant metrics with names and values if provided]

**Additional Notes:**
[Any other important information]

Please let me know if you have any questions or feedback.

Thanks,
{{sender-name}}
```

## 用法 / Usage
- 必填變數 / Variables: {{project-name}}、{{recipient-names}}、{{sender-name}}、{{week-start-date}}、{{weekly-update}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Weekly Stakeholder Report Template Generator is a free AI prompt that transforms raw project updates into …
