# Digital Note-Taking Tool Comparison Prompt

## 簡介

The Digital Note-Taking Tool Comparison Prompt is a free AI prompt that creates side-by-side evaluations of note-taking applications to help professionals and students choose the right productivity tools. This note-taking tool comparison prompt for ChatGPT analyzes your shortlisted apps - Notion, Obsidian, Evernote, Apple Notes, or others - and delivers a structured markdown table comparing sync capabilities, organization methods, search functionality, integrations, pricing, and security. You specify your device ecosystem (iOS, Android, Windows, cross-platform), collaboration needs (solo, team sharing, real-time editing), and security requirements, and the prompt tailors its analysis accordingly. The output is designed for anyone evaluating note-taking software, migrating between platforms, or optimizing their information management stack. ● Compares multiple note-taking tools in a three-column table (Features, Pros, Cons) for quick decision-making ● Evaluates sync performance, organization features, search power, third-party integrations, and pricing tiers ● Tailors recommendations to your device ecosystem, collaboration workflow, and data security standards ● Produces markdown-formatted output ready to paste into documentation or share with teams ## Prompt

```
## Role
You are an expert digital productivity specialist focused on optimizing note-taking processes.

## Task
Analyze the specified digital note-taking tools and create a comprehensive comparison to help select the most suitable option. Provide actionable insights on leveraging these tools to streamline workflows, improve information retention, and boost productivity.

## Context
**Tools under consideration:** {{preferred-tools}}

**Use case requirements:**
- Primary purpose: {{note-taking-purpose}}
- Device ecosystem: {{device-ecosystem}}
- Collaboration needs: {{collaboration-requirements}}
- Security requirements: {{security-requirements}}

## Output
Deliver your analysis as a markdown table with three columns: **Features**, **Pros**, and **Cons**. Cover all major aspects of each tool—sync capabilities, organization methods, search functionality, integrations, pricing, and any features relevant to the stated requirements. The table should enable an informed decision based on the specific context provided.
```

## 用法 / Usage
- 必填變數 / Variables: {{collaboration-requirements}}、{{device-ecosystem}}、{{note-taking-purpose}}、{{preferred-tools}}、{{security-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Context_Audit&Triage
- 適用 / Use when: The Digital Note-Taking Tool Comparison Prompt is a free AI prompt that creates side-by-side evaluations of no…
