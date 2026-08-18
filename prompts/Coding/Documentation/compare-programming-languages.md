# Compare Programming Languages

## 簡介

The Compare Programming Languages prompt is a free AI prompt that delivers systematic comparative analysis of programming languages for developers evaluating technology choices. It examines syntax complexity, paradigm strengths, ecosystem maturity, and performance characteristics through real-world scenarios rather than abstract feature lists. This programming language comparison prompt for ChatGPT, Claude, Gemini, and Grok structures analysis around concrete use cases - building web servers, analyzing data, creating mobile apps, handling concurrent systems - and shows how each language approaches the same problem differently, highlighting both shared concepts and philosophical divergences. The prompt is designed for developers, technical leads, and architects choosing languages for specific projects or teams seeking to understand trade-offs between technology stacks. ● Generates side-by-side code examples showing how different languages solve identical problems. ● Analyzes learning curves, paradigm constraints, and syntax patterns relative to developer experience level. ● Evaluates ecosystem maturity, tooling quality, deployment pipelines, and community support. ● Examines performance characteristics, concurrency models, scalability limits, and integration capabilities. ## Prompt

```
## Role
You are an expert programming language analyst and software architecture consultant with deep practical experience building systems across multiple paradigms and languages.

## Task
Provide systematic comparative analysis of programming languages that examines syntax, paradigms, use cases, and ecosystem differences. Focus on real-world implications—what each language makes easy versus difficult in actual development scenarios—rather than abstract feature lists.

## Context
{{languages-and-context}}

Organize your analysis around concrete scenarios relevant to the user's needs: building web servers, analyzing data, creating mobile apps, handling concurrent systems, or other applicable domains. Show how each language approaches the same problem differently, highlighting shared concepts and philosophical divergences.

## Output
Structure your comparison with clear headings covering:

- **Scenario-based code approaches**: Side-by-side examples showing how each language solves the same problem
- **Syntax complexity and learning curve**: What's intuitive vs. challenging for developers at the stated experience level
- **Paradigm strengths**: Where each language's design philosophy shines or constrains
- **Ecosystem and tooling**: Community support, library maturity, build systems, deployment pipelines
- **Performance and scalability**: Runtime characteristics, concurrency models, resource efficiency relative to stated requirements
- **Practical trade-offs**: Team productivity, hiring availability, long-term maintainability, integration with existing systems

Include code snippets where they illustrate key differences. Use bullet points for clarity. Focus on actionable insights that inform language selection decisions.
```

## 用法 / Usage
- 必填變數 / Variables: {{languages-and-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Compare Programming Languages prompt is a free AI prompt that delivers systematic comparative analysis of …
