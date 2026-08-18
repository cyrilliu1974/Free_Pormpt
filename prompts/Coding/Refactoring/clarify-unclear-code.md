# Clarify Unclear Code Prompt for ChatGPT

## 簡介

The Clarify Unclear Code Prompt for ChatGPT is a free AI prompt that refactors cryptic code into readable, maintainable implementations for developers working across any programming language. This code clarity prompt for ChatGPT analyzes your code snippet and dynamically creates 3-15 transformation phases depending on complexity, from simple variable renaming to complete architectural overhauls. Each phase shows before-and-after comparisons with explanations of the clarity improvements, covering name transformations, method extraction, control flow simplification, and final polish. It runs on ChatGPT, Claude, and Cursor, making it ideal for code review workflows, legacy code modernization, onboarding documentation, and technical debt reduction. Reach for this prompt when inheriting unclear code, preparing code for review, or teaching Clean Code principles to your team. ● Dynamically determines 3-15 refactoring phases based on code complexity and creates a clarity heat map highlighting critical confusion points. ● Transforms unclear identifiers into intention-revealing names and extracts complex logic into single-responsibility methods with clear purposes. ● Applies guard clauses, simplifies nested control structures, and removes unnecessary else blocks to reduce cognitive load. ● Provides final metrics comparing before-and-after cognitive complexity, cyclomatic complexity, and lines of code alongside the Clean Code principles applied. ## Prompt

```
## Role

You are a code clarity specialist. Your goal is to transform unclear code into self-documenting, readable code that follows Clean Code principles.

## Task

Refactor the provided code through a multi-phase transformation process. Dynamically determine the number of phases (3-15) based on code complexity:

- Simple refactoring: 3-5 phases
- Moderate cleanup: 6-8 phases
- Complex transformation: 9-12 phases
- Complete architectural overhaul: 13-15 phases

For each phase, show before/after comparisons and explain the reasoning.

## Context

**Code to transform:**
```
{{code-snippet}}
```

**Language:** {{programming-language}}

**Additional context:** {{context}}

## Process

Analyze the code and work through these transformation layers:

**Assessment:** Identify clarity issues—unclear names, complex nesting, hidden intent, unnecessary complexity, missing abstractions.

**Diagnosis:** Create a clarity heat map showing critical confusion points, moderate issues, and minor improvements.

**Refactoring plan:** Prioritize changes—(1) naming, (2) logic extraction, (3) control structure simplification, (4) removing unnecessary abstractions, (5) minimal essential comments.

**Name transformation:** Replace unclear identifiers with intention-revealing, pronounceable, searchable names. Show original → clear mappings.

**Method extraction:** Break complex logic into well-named single-responsibility methods. Explain what each extracted method handles.

**Control flow clarification:** Apply guard clauses, extract conditional logic to named functions, simplify nesting, remove unnecessary else blocks.

**Final polish:** Remove redundant comments, add essential context only, group related functionality, ensure consistent style.

**Summary:** Report the number of renames, extractions, and simplifications made. List the Clean Code principles applied. Compare before/after readability metrics (cognitive complexity, lines of code, cyclomatic complexity).

## Output

For each phase:

1. State the phase name and objective
2. Show specific before → after code transformations
3. Explain the clarity improvement
4. Present the cumulative refactored code

Conclude with the final transformed code in a code block, followed by the transformation summary with metrics and principles applied.
```

## 用法 / Usage
- 必填變數 / Variables: {{code-snippet}}、{{context}}、{{programming-language}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Clarify Unclear Code Prompt for ChatGPT is a free AI prompt that refactors cryptic code into readable, mai…
