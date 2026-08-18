# Troubleshooting Workflow Generator for Support Teams

## 簡介

The Troubleshooting Workflow Generator for Support Teams is a free AI prompt that creates systematic problem-resolution procedures for technical support specialists, IT teams, and customer service professionals. This troubleshooting workflow prompt for ChatGPT builds logical decision trees that guide users from symptom identification through root cause analysis to final resolution. It structures each workflow with diagnostic steps that include clear branching logic ("If yes, proceed to step X; if no, go to step Y"), specific resolution procedures for each identified cause, verification steps to confirm the problem is solved, and escalation criteria for when additional support is needed. The prompt adapts language complexity to match your target audience's technical expertise, whether you're writing for end users, junior technicians, or experienced engineers. It runs on ChatGPT, Claude, Gemini, and Grok to produce professional troubleshooting guides for software systems, hardware components, business processes, or customer service scenarios. Reach for this prompt when you need to document consistent problem-resolution procedures, train support staff, reduce resolution time, or create knowledge base articles that help users self-serve common issues. ● Builds numbered diagnostic sequences with clear decision points and branching logic for systematic problem identification ● Generates specific resolution procedures for each identified root cause, not vague advice ● Includes verification steps to confirm issues are fully resolved before closing tickets ● Provides escalation criteria so users know when to seek additional technical support ## Prompt

```
## Role
You are an expert troubleshooting specialist who designs comprehensive, efficient problem-resolution workflows.

## Task
Create step-by-step troubleshooting procedures that systematically identify and resolve issues. Build logical decision trees that guide users from symptom identification through root cause analysis to resolution. Include verification steps to confirm problems are solved.

## Context
System/process details: {{system-description}}

Common issues to address: {{known-issues}}

Target user technical level: {{technical-expertise}}

## Output
Deliver a structured troubleshooting guide with:

- **Overview**: Problem scope and prerequisites
- **Diagnostic Steps**: Numbered sequence with clear decision points ("If yes, proceed to step X; if no, go to step Y")
- **Resolution Procedures**: Specific actions for each identified cause
- **Verification**: How to confirm the issue is resolved
- **Escalation Criteria**: When to seek additional support

Format each workflow with clear headings, subheadings, and numbered steps. Adapt language complexity to match the specified technical expertise level.
```

## 用法 / Usage
- 必填變數 / Variables: {{known-issues}}、{{system-description}}、{{technical-expertise}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Troubleshooting Workflow Generator for Support Teams is a free AI prompt that creates systematic problem-r…
