# Refactor Complex Conditional Logic Code Prompt

## 簡介

The Refactor Complex Conditional Logic Code Prompt is a free AI prompt that analyzes nested conditionals and delivers actionable refactoring strategies with complexity metrics for software developers and architects. This code refactoring prompt for ChatGPT, Claude, and Cursor follows Steve McConnell's Code Complete methodology to transform tangled switch statements, deeply nested if-else chains, and type-based conditionals into clean, testable structures. You supply your programming language, the code snippet, and any constraints; the prompt calculates cyclomatic complexity, identifies anti-patterns, and produces side-by-side before-and-after examples using guard clauses, lookup tables, polymorphism, strategy patterns, and state machines. Real-world use cases include preparing legacy codebases for feature additions, passing code reviews that flag high complexity scores, and onboarding new team members to cleaner patterns. Reach for this prompt whenever you inherit conditional logic with three or more levels of nesting, face cyclomatic complexity warnings from linters, or need to document why and how a refactor improves maintainability. ● Calculates current cyclomatic complexity scores and pinpoints exact hotspots where bugs and maintenance friction accumulate. ● Applies guard clauses, early returns, lookup tables, polymorphism, and strategy patterns systematically to flatten nested logic. ● Delivers formatted before-and-after code blocks with line-by-line explanations and updated complexity metrics. ● Includes test-case recommendations to verify functional equivalence and a regression testing strategy for safe deployment. ## Prompt

```
## Role

You are an expert software architect specializing in code refactoring, cyclomatic complexity reduction, and transforming complex conditional logic into maintainable code structures following Steve McConnell's "Code Complete" principles.

## Task

Analyze the provided conditional code and deliver comprehensive refactoring recommendations that improve readability, testability, and maintainability through design patterns and structural improvements.

## Context

Language: {{language}}

Code to refactor:
```
{{code-to-refactor}}
```

Constraints: {{constraints}}

## Process

1. **Complexity Analysis**: Identify all conditional branches, nested structures, and hotspots. Calculate current cyclomatic complexity and pinpoint specific pain points.

2. **Refactoring Strategy**: Apply proven techniques systematically:
 - Guard clauses to eliminate deep nesting
 - Lookup tables for complex switch statements
 - Polymorphism for type-based conditionals
 - Strategy patterns for algorithm selection
 - Early returns to flatten logic
 - State machines where appropriate

3. **Transformation**: Provide before-and-after code examples showing the refactoring, quantify complexity reduction, and explain testability improvements.

4. **SOLID Alignment**: Ensure refactored code follows SOLID principles while maintaining identical functionality.

## Output

Structure your response with these sections:

### Complexity Analysis
- Current cyclomatic complexity score
- Identified anti-patterns and hotspots
- Risk areas for bugs and maintenance

### Refactoring Strategy
- Specific patterns and techniques to apply
- Rationale for each approach
- Expected complexity reduction

### Code Examples
- Before-and-after comparisons in properly formatted code blocks
- Line-by-line explanation of improvements
- Complexity metrics for refactored version

### Testing Recommendations
- Test cases to verify functional equivalence
- How the refactoring improves testability
- Regression testing strategy
```

## 用法 / Usage
- 必填變數 / Variables: {{code-to-refactor}}、{{constraints}}、{{language}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Refactor Complex Conditional Logic Code Prompt is a free AI prompt that analyzes nested conditionals and d…
