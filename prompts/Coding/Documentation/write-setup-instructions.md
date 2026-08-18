# Setup Instructions Writer for Software Documentation

## 簡介

The Setup Instructions Writer for Software Documentation is a free AI prompt that produces clear, unambiguous installation guides for software on any operating system. This setup instructions prompt for ChatGPT generates structured documentation with numbered steps, exact copy-paste commands, and built-in verification checkpoints that help users confirm they're on the right track. It runs on ChatGPT, Claude, Gemini, and Grok, producing guides organized into prerequisites checks, installation steps with explanations, verification procedures, and proactive troubleshooting sections. Technical writers use it to create first-attempt-success documentation that anticipates confusion before it happens, reducing support ticket volume and improving user onboarding experiences. ● Structures guides with prerequisite checks, installation steps, verification procedures, and troubleshooting in one organized document ● Includes exact commands in code blocks for copy-pasting and "What you should see" confirmation points after critical steps ● Anticipates common errors and pitfalls, addressing them proactively before users encounter frustration ● Uses visual hierarchy, bullet points, and clear section headings to make every instruction actionable and unambiguous ## Prompt

```
## Role
You are a technical documentation specialist writing installation guides that users complete successfully on the first attempt.

## Task
Create clear, step-by-step setup instructions for {{software-name}} on {{target-os}}. Every instruction should be unambiguous—users should never pause to wonder what to do next.

## Context
{{setup-context}}

Anticipate confusion before it happens. Guide users around pitfalls proactively. Include specific details about where to find interface elements, what success looks like at each stage, and alternative paths when things don't work as expected.

## Output
Structure your installation guide with:

**Numbered steps** with exact commands in code blocks for copy-pasting

**"What you should see"** confirmation points after critical steps so users know they're on track

**Clear section headings** organized as:
1. Prerequisites Check (with links to install missing dependencies)
2. Installation Steps (with explanations of what each step accomplishes)
3. Verification (how to confirm the installation succeeded)
4. Troubleshooting (addressing common errors before users encounter them)

Use bullet points and visual hierarchy for maximum readability. Make every instruction unambiguous and actionable.
```

## 用法 / Usage
- 必填變數 / Variables: {{setup-context}}、{{software-name}}、{{target-os}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Setup Instructions Writer for Software Documentation is a free AI prompt that produces clear, unambiguous …
