# Recommend Codebase Naming Conventions

## 簡介

The Recommend Codebase Naming Conventions prompt is a free AI prompt that analyzes your existing code and delivers structured naming guidelines to improve readability and eliminate technical debt for software teams. This codebase naming conventions prompt for ChatGPT takes a code context variable and produces intent-revealing naming rules for variables, functions, classes, and tests, complete with before-and-after examples extracted from your actual code. It applies Robert C. Martin's Clean Code principles - pronounceability, searchability, and the elimination of mental mapping - while respecting language-specific case conventions (camelCase for JavaScript, snake_case for Python, PascalCase for classes). Use it when onboarding new developers, refactoring legacy systems, or establishing team coding standards. It runs on ChatGPT, Claude, Gemini, and Grok. ● Analyzes your provided code context and surfaces problematic patterns that require mental translation. ● Delivers verb-noun function patterns, boolean naming rules (is/has/should/can), and noun-based class names that reveal responsibility. ● Provides language-specific case conventions and decision frameworks for choosing between naming alternatives. ● Includes structured sections for variables, functions, classes, tests, and common scenarios like data pipelines and event handlers. ## Prompt

```
## Role

You are an expert software architect specializing in clean code principles and intent-revealing naming conventions across enterprise codebases.

## Task

Analyze the provided code and recommend comprehensive naming conventions that reveal intent, ensure pronounceability and searchability, and eliminate mental mapping. Deliver structured guidelines with before/after examples and implementation rules.

## Context

{{code-context}}

Poor naming creates technical debt. Every identifier should communicate purpose without comments. Establish consistent patterns for variables, functions, classes, and tests that avoid abbreviations (except universally understood terms like URL, API, HTTP), reveal intent, and indicate behavior clearly.

Address case conventions (camelCase vs snake_case vs PascalCase) based on language standards. Cover edge cases and provide decision frameworks for choosing between naming alternatives.

## Output

Structure your response with these sections:

### Variables
- Intent-revealing patterns
- Avoiding abbreviations and single letters
- Before/after examples from the provided code

### Functions
- Verb-noun patterns that describe behavior
- Boolean function naming (is/has/should/can)
- Before/after examples from the provided code

### Classes
- Noun-based naming that reveals responsibility
- Avoiding generic suffixes (Manager, Helper, Processor)
- Before/after examples from the provided code

### Tests
- Readable test names that describe scenarios
- Given-When-Then or should_do_something patterns
- Before/after examples from the provided code

### Case Conventions
- Language-specific standards (JavaScript/Java use camelCase, Python/Ruby use snake_case, classes use PascalCase)
- Consistency rules within the codebase

### Common Scenarios
- Data processing pipelines
- User interaction handlers
- Business logic implementation

For each section, identify problematic patterns that require mental translation and provide specific transformation rules with concrete examples extracted from the code context.
```

## 用法 / Usage
- 必填變數 / Variables: {{code-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Recommend Codebase Naming Conventions prompt is a free AI prompt that analyzes your existing code and deli…
