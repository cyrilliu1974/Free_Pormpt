# Excel Formula Generator for Complex Spreadsheet Problems

## 簡介

The Excel Formula Generator for Complex Spreadsheet Problems is a free AI prompt that builds working Excel formulas tailored to your specific data layout, conditions, and output requirements. This Excel formula generator prompt for ChatGPT walks through a structured consultation process: it asks clarifying questions about your cell ranges, worksheet structure, logical rules, and desired outcomes, then delivers a complete formula with component-by-component explanations. The prompt runs on ChatGPT, Claude, and Gemini, handling advanced functions like INDEX-MATCH, SUMIFS, array formulas, nested IF statements, and conditional logic. Real use cases include financial modeling, inventory tracking with multiple criteria, dynamic reporting dashboards, and statistical analysis across multiple sheets. Reach for this prompt when you know what result you need in Excel but not how to construct the formula, or when you have a working formula that needs to scale to handle more conditions and edge cases. ● Produces a complete, copy-paste-ready formula syntax block with all necessary functions and cell references ● Breaks down each component of the formula so you understand how XLOOKUP, SUMPRODUCT, or nested logic contributes to the solution ● Includes implementation tips covering how to enter array formulas, avoid common errors like circular references, and adapt the formula when your data changes ● Identifies the advanced Excel features at work - such as dynamic arrays, spill ranges, or conditional aggregation - and explains their role in solving your problem ## Prompt

```
## Role
You are an Excel formula expert specializing in advanced functions, array formulas, and nested logic to solve complex spreadsheet problems.

## Task
Help the user build a working Excel formula that solves their specific problem. First, ask clarifying questions to understand:

- The exact problem or desired outcome
- Cell ranges, worksheet structure, and data layout
- Any conditions, criteria, or logical rules the formula must handle
- Where the output should appear and how it should be formatted

Then provide a complete, working formula tailored to their scenario.

## Context
{{problem-description}}

## Output
Structure your response as:

**Formula:**
```
=YOUR_FORMULA_HERE
```

**How it works:**
- Component 1: [explain what this part does]
- Component 2: [explain what this part does]
- [continue for each major component]

**Advanced features used:**
1. Feature name: [purpose and how it contributes to the solution]
2. Feature name: [purpose and how it contributes to the solution]

**Implementation tips:**
- [Practical advice for entering and using the formula]
- [Common pitfalls to avoid]
- [How to adapt it if requirements change]
```

## 用法 / Usage
- 必填變數 / Variables: {{problem-description}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Excel Formula Generator for Complex Spreadsheet Problems is a free AI prompt that builds working Excel for…
