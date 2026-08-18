# Bug Report Template Generator for QA Teams

## 簡介

The Bug Report Template Generator for QA Teams is a free AI prompt that creates standardized bug reporting structures for development teams struggling with vague, incomplete issue reports. This bug report template prompt for ChatGPT, Claude, Gemini, and Grok produces a markdown-formatted template following Ron Patton's Software Testing methodology. It generates identification sections with severity dropdowns, reproduction steps, environment fields, evidence guidelines, and side-by-side examples showing the difference between vague reports ("Login doesn't work sometimes") and actionable ones with specific steps and error messages. Real use cases include software teams onboarding non-technical testers, product managers building internal QA processes, and open-source projects needing contributor-friendly bug submission forms. Reach for this prompt when your team wastes time deciphering incomplete bug reports or when you need a template that balances technical detail with accessibility for all skill levels. ● Creates identification sections with severity dropdowns (Critical/High/Medium/Low) and clear definitions for each level. ● Generates reproduction sections with numbered steps, preconditions, and frequency fields to eliminate ambiguity. ● Includes environment fields for software version, OS, browser/device, and configurations that affect debugging. ● Provides 2-3 complete example bug reports across severity levels, demonstrating proper usage for payment failures, UI issues, and cosmetic problems. ## Prompt

```
## Role
You are a quality assurance architect specializing in bug reporting systems that work for both technical and non-technical users.

## Task
Create a comprehensive bug report template following Ron Patton's "Software Testing" methodology. The template must capture all essential debugging information while remaining accessible to reporters of all skill levels.

## Context
Development teams waste significant time deciphering vague bug reports with missing reproduction steps, unclear severity assessments, and incomplete environment details. This template will standardize bug reporting for {{software-context}} to accelerate debugging and prevent miscommunication.

## Output
Deliver a structured bug report template in markdown format with:

### Template Structure
- **Identification Section**: Title field and severity dropdown (Critical/High/Medium/Low) with clear definitions for each level
- **Reproduction Section**: Numbered steps to reproduce, preconditions, and frequency of occurrence
- **Behavior Section**: Expected result versus actual result fields
- **Environment Section**: Software version, operating system, browser/device, and relevant configurations
- **Evidence Section**: Screenshots, error logs, console output, and video recordings
- **Priority Assessment**: Priority level dropdown with business impact criteria

### Field Design Requirements
- Self-explanatory labels requiring no technical expertise
- Dropdown menus with standardized values where applicable
- Inline guidance text for complex fields
- Mandatory versus optional field indicators

### Example Entries
Provide side-by-side comparisons showing:
- **Vague**: "Login doesn't work sometimes"
- **Actionable**: Specific steps, error messages, and environment details that enable immediate reproduction

Include 2-3 complete example bug reports demonstrating proper usage across different severity levels (e.g., a critical payment processing failure, a medium UI alignment issue, and a low cosmetic typo).

### Design Principles
Ensure the template:
- Prevents common mistakes like missing reproduction steps
- Balances comprehensiveness with usability (avoid field overload)
- Focuses on information that directly accelerates debugging
- Works for both technical QA testers and non-technical end users
```

## 用法 / Usage
- 必填變數 / Variables: {{software-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Bug Report Template Generator for QA Teams is a free AI prompt that creates standardized bug reporting str…
