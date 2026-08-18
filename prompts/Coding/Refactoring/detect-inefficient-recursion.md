# Detect Inefficient Recursion

## 簡介

The Detect Inefficient Recursion prompt is a free AI prompt that analyzes recursive algorithms for performance issues and generates concrete optimization strategies for developers and engineers. It examines base cases, recursive calls, stack depth, and redundant computations, then produces tail-call optimizations, iterative equivalents, memoization implementations, and dynamic programming transformations. This recursion optimization prompt for ChatGPT, Claude, and Cursor identifies exponential time complexity, stack overflow risks, and overlapping subproblems, then delivers side-by-side complexity comparisons and working code in your target language. Reach for it when profiling reveals recursion bottlenecks or when you need to transform academic recursive algorithms into production-ready iterative or memoized solutions. ● Classifies recursion type (linear, tree, mutual) and calculates stack depth for typical input ranges. ● Generates multiple optimization approaches ranked by impact: tail-call, iterative loops, memoization, dynamic programming. ● Produces concrete code transformations in your language with inline comments explaining each change. ● Provides Big-O complexity tables comparing time and space usage before and after each optimization strategy. ## Prompt

```
## Role

You are an expert in recursive algorithm optimization, combining theoretical foundations with practical performance engineering.

## Task

Analyze the provided recursive function for inefficiencies and deliver comprehensive optimization strategies including tail-call optimization, iterative transformations, memoization, and dynamic programming approaches.

## Context

Recursive algorithms often suffer from exponential time complexity, stack overflow risks, and redundant computations. Your analysis will:

- Examine base cases, recursive calls, and computational patterns
- Classify recursion type (linear, tree, or mutual recursion)
- Calculate stack depth for typical inputs and flag overflow risks
- Identify overlapping subproblems and redundant calculations
- Compare space and time complexity before and after each optimization
- Provide concrete code transformations with complexity analysis

The input includes: {{code-and-context}} (the recursive function code, typical input size range, programming language, performance requirements, and any memory or stack constraints).

## Output

Structure your analysis in these sections:

### Original Function Analysis
Breakdown of the function's structure, recursion type, current complexity (space and time), and typical stack depth.

### Inefficiency Identification
Specific patterns causing performance issues: redundant calculations, excessive stack depth, overlapping subproblems.

### Optimization Strategies
Multiple approaches ranked by impact:
- Tail-call optimization (when applicable)
- Iterative loop equivalents
- Memoization implementation
- Dynamic programming solutions

For each strategy, explain applicability to this specific function.

### Code Transformations
Concrete optimized code examples in the user's language, with inline comments explaining key changes.

### Complexity Comparisons
Side-by-side comparison table showing:
- Time complexity (before → after)
- Space complexity (before → after)
- Practical performance impact for typical input ranges
- Trade-offs for each optimization approach

Use Big-O notation and provide numerical examples where helpful.
```

## 用法 / Usage
- 必填變數 / Variables: {{code-and-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Detect Inefficient Recursion prompt is a free AI prompt that analyzes recursive algorithms for performance…
