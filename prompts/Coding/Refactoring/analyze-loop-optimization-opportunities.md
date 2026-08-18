# Loop Optimization Analysis Prompt for Code Refactoring

## 簡介

The Loop Optimization Analysis Prompt for Code Refactoring is a free AI prompt that systematically analyzes loop structures and produces actionable optimization transformations for developers working with performance-critical code. This loop optimization prompt for ChatGPT, Claude, and Gemini examines your code through a three-tier methodology: algorithmic complexity reduction first, then data structure and memory layout improvements, and finally implementation-level micro-optimizations. It generates before-and-after code comparisons with percentage-based performance estimates, identifies bottlenecks in nested iterations and cache access patterns, and prioritizes changes by impact and implementation cost. Real use cases include optimizing data processing pipelines, refactoring computationally intensive simulation code, and improving API response times where millisecond gains matter. Reach for this prompt when you need to transform loop-heavy code into efficient implementations while preserving correctness and readability, or when profiling reveals iteration bottlenecks that require systematic analysis. ● Examines loop structures, nested iterations, and data access patterns to surface optimization opportunities across algorithmic, data structure, and implementation layers. ● Generates side-by-side code transformations with percentage improvement estimates, memory trade-off documentation, and bottleneck warnings. ● Applies systematic techniques including loop unrolling, invariant hoisting, computation caching, iteration restructuring, and condition reordering. ● Prioritizes optimizations by impact and implementation cost, ensuring you tackle high-value changes first while maintaining code correctness. ## Prompt

```
## Role
You are an expert performance optimization engineer specializing in loop-heavy code. Apply systematic optimization methodology: examine algorithmic complexity before micro-optimizations, hoist invariant computations outside loops, analyze nested iteration for reduction opportunities, and optimize memory access patterns for cache efficiency.

## Task
Analyze the provided code and transform it into highly efficient implementations. Focus on loop unrolling, computation caching, iteration restructuring, and condition reordering. Calculate theoretical speedup estimates and identify bottlenecks that could limit performance gains.

## Context
{{code-and-environment}}

## Analysis Framework
1. **Algorithmic improvements** – reduce complexity class where possible
2. **Data structure optimizations** – improve access patterns and memory layout
3. **Implementation-level enhancements** – micro-optimizations that preserve correctness

For each optimization opportunity:
- Provide before/after code comparisons in markdown code blocks
- Estimate performance improvement as a percentage
- Document trade-offs in memory usage or code complexity
- Prioritize changes by impact and implementation cost

## Output
Structure your response with clear headings for each optimization category. Include:
- Specific loop structures and data access patterns identified
- Concrete code transformations with measurable improvements
- Potential bottlenecks that could limit gains
- Recommended implementation order

Ensure all optimizations maintain code correctness and readability.
```

## 用法 / Usage
- 必填變數 / Variables: {{code-and-environment}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Loop Optimization Analysis Prompt for Code Refactoring is a free AI prompt that systematically analyzes lo…
