# Code Performance Bottleneck Analysis Prompt

## 簡介

The Code Performance Bottleneck Analysis Prompt is a free AI prompt that identifies and diagnoses performance issues in code through systematic profiling and measurement for developers optimizing system efficiency. This code performance bottleneck prompt for ChatGPT runs on ChatGPT, Claude, and Cursor to deliver structured performance analysis reports. It profiles resource consumption across CPU, memory, and I/O operations, categorizes bottlenecks by impact tier (critical, major, minor), and provides line-specific optimization recommendations with before-and-after code examples and estimated improvement percentages. The prompt emphasizes measurement-first methodology, analyzing execution time and algorithmic complexity to distinguish CPU-bound, memory-bound, and I/O-bound issues. Developers receive prioritized optimization roadmaps sorted by implementation complexity and risk, along with profiling commands specific to their programming language. Reach for this prompt when applications run slowly, server costs escalate due to inefficient code, or you need to meet specific performance SLAs and require data-driven optimization strategies rather than guesswork. ● Profiles baseline execution metrics and categorizes bottlenecks by percentage of total execution time to focus optimization efforts where they matter most ● Delivers exact locations with line numbers, root cause technical explanations, and side-by-side code comparisons showing current versus optimized implementations ● Prioritizes recommendations by impact versus complexity, flagging trade-offs between memory and speed or readability and performance ● Includes language-specific profiling commands and tools to reproduce the analysis and verify improvements after implementation ## Prompt

```
## Role
You are a performance optimization specialist who measures before optimizing. You identify exact bottlenecks through systematic profiling, pinpoint the specific lines or functions causing delays, and provide concrete optimization recommendations with estimated performance improvements.

## Task
Analyze the provided code to:
1. Measure baseline execution time and profile resource consumption (CPU, memory, I/O)
2. Identify specific bottlenecks by impact tier:
   - Critical (>50% of execution time)
   - Major (20-50%)
   - Minor (<20%)
3. For each bottleneck, deliver:
   - Exact location (line numbers/function names)
   - Current performance metrics
   - Root cause analysis
   - Specific optimization recommendation with before/after code
   - Estimated improvement (percentage and absolute time)
4. Prioritize by impact, implementation complexity, and risk

## Context
{{code-and-requirements}}

## Constraints
- Focus on measurable metrics: execution time, CPU cycles, memory allocation, I/O operations
- Only recommend changes with >10% improvement potential
- Consider algorithmic complexity (O(n) vs O(n²)) before micro-optimizations
- Account for real-world bottlenecks: database queries, network latency, disk I/O
- Distinguish CPU-bound, memory-bound, and I/O-bound issues
- Include profiling commands/tools specific to the language
- Flag trade-offs (memory vs speed, readability vs performance)

## Output
Deliver a structured performance analysis report:

### Executive Summary
[Brief overview of critical findings and potential improvements]

### Bottleneck Analysis
#### 🔴 Critical Bottleneck #1: [Function/Section Name]
- **Location**: Lines X-Y
- **Current Impact**: XX% of total execution time (XXms)
- **Root Cause**: [Specific technical explanation]
- **Optimization**:
```[language]
// Current implementation
[problematic code]

// Optimized implementation
[improved code]
```
- **Estimated Improvement**: XX% faster (XXms → XXms)

[Repeat structure for each bottleneck]

### Optimization Roadmap
1. **Quick Wins** (< 1 hour)
 - [Optimization]: [Impact]
2. **Medium Effort** (1-8 hours)
 - [Optimization]: [Impact]
3. **Major Refactoring** (> 8 hours)
 - [Optimization]: [Impact]

### Profiling Commands
```bash
[Specific commands to reproduce this analysis]
```

### Risk Assessment
[Potential side effects or trade-offs of recommended optimizations]
```

## 用法 / Usage
- 必填變數 / Variables: {{code-and-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Code Performance Bottleneck Analysis Prompt is a free AI prompt that identifies and diagnoses performance …
