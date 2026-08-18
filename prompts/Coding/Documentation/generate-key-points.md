# Technical Writing Best Practices Guide Generator

## 簡介

The Technical Writing Best Practices Guide Generator is a free AI prompt that creates customized technical writing guides tailored to your experience level, document type, and target audience. This technical writing prompt for ChatGPT produces a four-section guide covering core principles with priority rankings, style guidelines with examples and common pitfalls, a document structure table, and an actionable quality checklist. You provide your writer profile - experience level, primary document types (API docs, user manuals, tutorials), and audience technical background - and the prompt generates specific, actionable best practices rather than generic advice. It runs on ChatGPT, Claude, and Gemini, making it ideal for technical writers, documentation teams, software developers writing docs, and product managers creating user guides. ● Adapts recommendations based on your experience level, from beginner to advanced technical writers ● Prioritizes principles by impact, helping you focus on what matters most for documentation quality ● Includes real examples and common pitfalls for each style guideline ● Delivers an actionable quality checklist with specific dos and don'ts for review ## Prompt

```
## Role
You are a technical writing expert skilled at creating clear, concise, and user-friendly documentation.

## Task
Create a comprehensive guide on essential principles and best practices for effective technical writing, tailored to the user's experience level, document type, and audience.

## Context
{{writer-profile}}
Include: your technical writing experience level (beginner/intermediate/advanced), the primary type of documents you create (product manuals, API docs, user guides, tutorials, etc.), and your target audience's technical background (non-technical users, moderately technical, or expert-level).

## Requirements
1. Focus on essential principles and best practices that have the most impact on documentation quality and usability
2. Provide clear examples to illustrate guidelines and concrete action items
3. Avoid overly general advice; prioritize specific, applicable tips
4. Highlight the most critical principles through priority ranking

## Output
Structure the guide into four sections using this format:

📝 **Core Principles**
- Principle: [principle_name]
  Description: [principle_description]
  Priority: [1-5]

✍️ **Writing Style Guidelines**
- Guideline: [guideline]
  Example: [example]
  Pitfall: [pitfall]

🔧 **Document Structure**
| Element | Purpose | Best Practices |
|---------|---------|----------------|
| [element] | [purpose] | [best_practices] |

🎯 **Quality Checklist**
✅ Do:
- [do_item]

❌ Avoid:
- [avoid_item]
```

## 用法 / Usage
- 必填變數 / Variables: {{writer-profile}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Skill_Prompt_Spec_Extractor
- 適用 / Use when: The Technical Writing Best Practices Guide Generator is a free AI prompt that creates customized technical wri…
