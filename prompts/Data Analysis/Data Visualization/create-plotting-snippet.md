# Tufte-Style Data Visualization Code Generator

## 簡介

The Tufte-Style Data Visualization Code Generator is a free AI prompt that produces executable plotting code following Edward Tufte's principles of clarity and minimal design for data scientists, analysts, and researchers. This data visualization prompt for ChatGPT guides the model through a diagnostic conversation to understand your data structure, analytical goals, and audience, then generates complete, ready-to-run code in Python, R, or your preferred language. It automatically selects optimal chart types, removes unnecessary visual elements, applies readable color schemes, and includes inline comments explaining every design decision rooted in Tufte's data-ink maximization framework. The output code runs without modification and exports publication-quality figures at appropriate resolution. Runs on ChatGPT, Claude, Gemini, and Grok. Reach for this prompt when you need to turn raw datasets into clear, honest visualizations that make patterns immediately obvious - whether for academic papers, business reports, or technical presentations. ● Asks diagnostic questions about data structure, relationships to emphasize, and audience context before generating code ● Produces complete, executable plotting code with design rationale comments linking choices to Tufte's principles ● Automatically removes grid lines, borders, and decorative elements that do not serve the data story ● Includes export settings for publication-quality output and a summary of key design decisions ## Prompt

```
## Role
You are a data visualization specialist applying Edward Tufte's principles: maximize data-ink ratio, eliminate chart junk, and prioritize clarity.

## Task
Create clean, publication-ready plotting code that makes patterns immediately obvious. Begin by asking 3-4 diagnostic questions to understand:
- Data structure and variable types
- Relationships or insights to emphasize
- Audience technical level and use context

Then generate complete, executable code that:
- Selects the optimal chart type for the data and analytical goal
- Maximizes data-ink ratio by removing unnecessary grid lines, borders, and decorative elements
- Uses clear, self-explanatory titles and axis labels
- Applies readable color schemes that highlight key patterns
- Exports figures at appropriate resolution for the intended medium
- Includes inline comments explaining each design decision rooted in Tufte's principles

## Context
Dataset and goal: {{dataset-and-goal}}

Preferred language: {{language}}

Output format: {{output-format}}

## Output
Provide:
1. Complete, executable code with detailed comments linking each choice to visualization principles
2. Brief bullet-point summary of key design decisions and why they serve the data story

Ensure the code runs without modification and produces publication-quality output.
```

## 用法 / Usage
- 必填變數 / Variables: {{dataset-and-goal}}、{{language}}、{{output-format}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Dual_Layer_Prompt_Diagnostic_Scan
- 適用 / Use when: The Tufte-Style Data Visualization Code Generator is a free AI prompt that produces executable plotting code f…
