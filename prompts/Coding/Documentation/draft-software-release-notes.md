# Software Release Notes Generator Prompt

## 簡介

The Software Release Notes Generator Prompt is a free AI prompt that creates professional, structured release documentation for software teams and product managers. This software release notes prompt for ChatGPT takes your version number, release date, target audience, and list of changes, then organizes them into a formatted document with clear sections for new features, improvements, bug fixes, known issues, system requirements, and upgrade instructions. It runs on ChatGPT, Claude, Gemini, and Grok, prioritizing the most impactful changes first while writing concise descriptions that balance technical accuracy with audience accessibility. Teams use it to communicate updates to end users, stakeholders, internal QA teams, and technical support staff. Reach for this prompt when you need to turn a raw list of code changes, tickets, or engineering notes into polished, audience-appropriate release documentation that helps users understand what changed and why it matters. ● Automatically categorizes changes into logical sections and prioritizes the most impactful updates first ● Writes concise, descriptive explanations that communicate user benefit alongside technical detail ● Includes system requirements, compatibility notes, and step-by-step upgrade instructions where applicable ● Adapts tone and depth to match your target audience, from technical developers to non-technical end users ## Prompt

```
## Role
You are an expert software release manager creating comprehensive release notes that communicate changes, improvements, and fixes to stakeholders.

## Task
Generate structured release notes for {{software-name}} version {{version-number}} (release date: {{release-date}}) tailored to {{target-audience}}.

## Context
Key changes to document:
{{changes-and-fixes}}

## Process
1. Categorize changes into logical sections: New Features, Improvements, Bug Fixes, Known Issues, and any other relevant groupings
2. Within each section, prioritize the most impactful items first
3. Write concise yet descriptive explanations for each item
4. Include necessary user instructions or upgrade steps where applicable
5. Note any relevant system requirements or compatibility information

## Output
Deliver release notes in this structure:

**[Software Name] v[Version] – [Release Date]**

### New Features
- [Feature]: [Description and user benefit]

### Improvements
- [Enhancement]: [What changed and why it matters]

### Bug Fixes
- [Fix]: [Issue resolved]

### Known Issues
- [Issue]: [Description and workaround if available]

### System Requirements
[Any updated requirements]

### Upgrade Instructions
[Steps users should take, if applicable]

Use consistent formatting, clear language, and bullet points throughout. Ensure technical accuracy while remaining accessible to your target audience.
```

## 用法 / Usage
- 必填變數 / Variables: {{changes-and-fixes}}、{{release-date}}、{{software-name}}、{{target-audience}}、{{version-number}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Software Release Notes Generator Prompt is a free AI prompt that creates professional, structured release …
