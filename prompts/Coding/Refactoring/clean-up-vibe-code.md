# Code Quality Audit and Refactoring Recommendations

## 簡介

The Code Quality Audit and Refactoring Recommendations prompt is a free AI prompt that performs structured code reviews and delivers actionable refactoring strategies for engineering teams maintaining production systems. This code quality audit prompt for ChatGPT guides the AI to analyze your codebase across five critical dimensions: clarity and code smells, hardcoded configurations and secrets, dependency security and licensing, automated quality gates, and documentation gaps. It runs on ChatGPT, Claude, Gemini, and Grok, accepting your technical stack and specific quality concerns as inputs, then returning prioritized recommendations with concrete code examples, configuration snippets, and command-line instructions. Use it when inheriting legacy code, preparing for a production launch, onboarding new engineers, or reducing technical debt before it compounds. ● Identifies code smells, duplication, and complexity hotspots with structural improvement suggestions tailored to your stack. ● Flags hardcoded credentials, environment-specific logic, and configuration that should be externalized. ● Assesses dependencies for security vulnerabilities, licensing conflicts, version mismatches, and performance bottlenecks. ● Recommends linting rules, pre-commit hooks, CI pipeline checks, and test coverage thresholds to prevent future issues. ● Provides templates for README files, API contracts, architecture decision records, and onboarding documentation. ## Prompt

```
## Role
You are a senior software engineer specializing in code quality audits, refactoring strategy, and technical debt prevention across production systems.

## Task
Perform a comprehensive code quality audit and deliver actionable refactoring recommendations organized into five analysis areas:

1. **Refactoring for Clarity** – identify code smells, duplication, complexity hotspots, and structural improvements
2. **Configuration & Secrets** – flag hardcoded values, credentials, and environment-specific logic that should be externalized
3. **Dependency Review** – assess libraries for security vulnerabilities, licensing issues, version conflicts, and performance impact
4. **Automated Quality Gates** – recommend linting rules, pre-commit hooks, CI pipeline checks, and coverage thresholds
5. **Documentation** – provide templates for README, API contracts, architecture decision records, and onboarding guides

## Context
{{technical-stack}}

{{quality-concerns}}

## Output
For each of the five sections:

- State the specific issue or gap found
- Explain the impact on maintainability, security, or performance
- Provide concrete code examples, configuration snippets, or command-line instructions that can be implemented immediately
- Prioritize recommendations by risk and effort

Avoid generic advice; tailor every suggestion to the stack and concerns provided. Use inline code blocks for snippets and file examples for larger configuration samples.
```

## 用法 / Usage
- 必填變數 / Variables: {{quality-concerns}}、{{technical-stack}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Code Quality Audit and Refactoring Recommendations prompt is a free AI prompt that performs structured cod…
