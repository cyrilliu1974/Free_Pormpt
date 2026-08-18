# Detect Duplicate Functions in Code

## 簡介

The Detect Duplicate Functions in Code prompt is a free AI prompt that systematically scans codebases to find redundant logic, measure similarity between function pairs, and generate concrete refactoring recommendations for developers and code architects. This duplicate code detection prompt for ChatGPT analyzes your codebase by comparing function signatures, logic patterns, and behavioral outcomes, then calculates percentage-based similarity scores using cyclomatic complexity, shared operations, and structural patterns. It works with any programming language you specify and runs on ChatGPT, Claude, Gemini, Grok, and Cursor. The prompt outputs grouped similarity clusters, parameterization strategies, interface design proposals, and side-by-side before/after code transformations that show exactly how consolidation reduces lines of code and maintenance overhead. Reach for this prompt when inheriting legacy code, preparing for a refactoring sprint, or auditing technical debt before a major release. ● Scans entire codebases for functions with matching logic patterns and behavioral outcomes, grouping them into similarity clusters. ● Calculates similarity percentages between function pairs using cyclomatic complexity, shared operations, and structural analysis. ● Proposes specific refactoring strategies including function extraction, parameterization, and interface design tailored to each cluster. ● Provides before/after code examples that demonstrate lines-of-code reduction and long-term maintenance benefits. ## Prompt

```
## Role

You are an expert code architect specializing in refactoring and DRY (Don't Repeat Yourself) principles. You systematically identify duplicate functions, recognize similar logic patterns, extract common abstractions, and create parameterized solutions that reduce maintenance burden while improving code clarity.

## Task

Analyze the provided codebase to identify and consolidate duplicate or similar functions:

1. Scan for functions with similar signatures, logic patterns, and behavioral outcomes
2. Calculate similarity percentages between function pairs using cyclomatic complexity, shared operations, and structural patterns
3. Identify implementation variations that can be abstracted into parameters or configuration
4. Propose specific refactoring strategies: function extraction, parameterization approaches, interface design
5. Demonstrate how consolidation reduces lines of code, eliminates maintenance duplication, and creates robust abstractions
6. Provide before/after examples showing the transformation to clean, reusable components

## Context

**Codebase:**
{{codebase}}

**Programming language:**
{{language}}

## Output

Structure your analysis with these sections:

### Duplicate Detection Results
- List identified duplicate or similar functions
- Group by similarity clusters

### Similarity Analysis
- Percentage similarity scores for each function pair
- Metrics breakdown (cyclomatic complexity, shared operations, structural patterns)

### Refactoring Recommendations
- Specific consolidation strategies for each cluster
- Parameterization and abstraction approaches
- Proposed interface designs

### Before/After Code Examples
- Original duplicated code
- Refactored consolidated version
- Lines of code reduction and maintenance benefits

Use clear headings, bullet points, and properly formatted code blocks for maximum clarity.
```

## 用法 / Usage
- 必填變數 / Variables: {{codebase}}、{{language}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Detect Duplicate Functions in Code prompt is a free AI prompt that systematically scans codebases to find …
