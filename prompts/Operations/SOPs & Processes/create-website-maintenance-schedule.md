# Website Maintenance Schedule Generator

## 簡介

The Website Maintenance Schedule Generator is a free AI prompt that creates platform-specific maintenance schedules covering CMS updates, plugin compatibility, security scans, backups, and performance optimization for website managers and developers. This website maintenance schedule prompt for ChatGPT analyzes your CMS platform and produces a structured maintenance plan with task frequencies, security best practices, backup strategies, and performance tips. It runs on ChatGPT, Claude, Gemini, and Grok, delivering actionable schedules in table format with 8-10 essential tasks, 5-7 security practices, backup retention policies, and optimization recommendations. Web agencies use it to standardize client site maintenance; in-house teams rely on it to prevent downtime and security incidents. Reach for this prompt when onboarding a new website, auditing current maintenance practices, or training technical staff on proper upkeep routines. ● Produces task schedules with frequencies and descriptions tailored to your CMS platform (WordPress, Drupal, Joomla, custom builds) ● Includes authentication, access control, monitoring, and vulnerability management best practices ● Defines full, incremental, and database backup strategies with retention policies ● Recommends caching, asset optimization, database maintenance, and speed improvement techniques ## Prompt

```
## Role

You are an experienced website maintenance expert with deep knowledge of CMS systems, plugins, themes, and security best practices.

## Task

Create a comprehensive website maintenance schedule tailored to the user's platform and site. Cover CMS updates, plugin compatibility, theme updates, security scans, backups, security best practices, backup strategy, and performance optimization.

## Context

- Website URL: {{website-url}}
- CMS platform: {{cms-platform}}

## Output

Provide your response in the following structure:

**Maintenance Schedule**

| Task | Frequency | Description |
|------|-----------|-------------|
| [List 8-10 essential maintenance tasks with appropriate frequencies and clear descriptions] | | |

**Security Best Practices**

1. [List 5-7 comprehensive security practices covering authentication, access control, monitoring, patching, and vulnerability management]

**Backup Strategy**

- [Backup type]: [Frequency and retention policy]
- [Include full, incremental, and database backups with appropriate schedules]

**Performance Optimization Tips**

- [List 5-7 actionable tips for improving site speed, caching, asset optimization, database maintenance, and user experience]

Ensure all recommendations are specific to the CMS platform provided and reflect current best practices for website maintenance and security.
```

## 用法 / Usage
- 必填變數 / Variables: {{cms-platform}}、{{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Website Maintenance Schedule Generator is a free AI prompt that creates platform-specific maintenance sche…
