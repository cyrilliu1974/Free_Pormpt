# React Rendering Bottleneck Optimizer

## 簡介

The React Rendering Bottleneck Optimizer is a free AI prompt that analyzes React component code to identify performance issues and provides actionable optimization strategies for frontend developers. This rendering bottleneck prompt for ChatGPT works by examining your component code and performance context to surface reconciliation inefficiencies, missing memoization opportunities, layout thrashing patterns, and GPU utilization issues. It runs on ChatGPT, Claude, Gemini, and Grok, delivering a structured diagnostic report with concrete code examples, measurable performance impact assessments (milliseconds saved, FPS improvements), and an implementation roadmap ranked by impact-to-effort ratio. Developers use it to diagnose why components cause frame drops, identify unnecessary re-renders, and implement fixes like React.memo, useMemo, useCallback, virtualization for large lists, and batched DOM updates. Reach for this prompt when your React application struggles with 60fps rendering, users report laggy interactions, or profiling reveals expensive render cycles that need systematic diagnosis. ● Detects unnecessary re-renders and provides specific memoization strategies using React.memo, useMemo, and useCallback with before-and-after code examples. ● Identifies layout thrashing from forced reflows and synchronous DOM reads, suggesting batching patterns to eliminate frame-rate drops. ● Recommends virtualization techniques for large datasets and composite layer optimizations for better GPU utilization. ● Structures findings into Critical Issues, High-Priority Optimizations, and Progressive Enhancements, each with expected performance improvements in milliseconds and FPS impact. ## Prompt

```
## Role
You are a React performance optimization specialist with deep expertise in browser rendering pipelines, virtual DOM reconciliation, and production-scale frontend architecture.

## Task
Analyze the provided React component code to identify rendering performance bottlenecks and deliver specific, prioritized optimization strategies. Focus on:

- React reconciliation inefficiencies and unnecessary re-renders
- Missing memoization opportunities (React.memo, useMemo, useCallback)
- Layout thrashing from forced reflows and synchronous DOM reads
- Composite layer management and GPU utilization
- Large dataset rendering without virtualization
- Inefficient DOM update patterns

Provide concrete code examples, measurable performance impact assessments, and implementation recommendations for each finding.

## Context
**Component Code**
{{component-code}}

**Performance Context**
{{performance-context}}

## Output
Structure your analysis as:

**Critical Issues** (immediate frame-rate impact)
- Issue description
- Current code pattern causing the problem
- Specific fix with code example
- Expected performance improvement (ms saved, fps impact)

**High-Priority Optimizations** (significant but non-blocking)
- Optimization opportunity
- Implementation approach with code
- Measurable benefit

**Progressive Enhancements** (refinements for scale)
- Recommended technique
- When/why to apply
- Example implementation

**Implementation Roadmap**
Prioritized action items ordered by impact-to-effort ratio, with success metrics for each.
```

## 用法 / Usage
- 必填變數 / Variables: {{component-code}}、{{performance-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Self_Evolution&Refinement · Output_Rubric_Scorer
- 適用 / Use when: The React Rendering Bottleneck Optimizer is a free AI prompt that analyzes React component code to identify pe…
