# Analyze Performance Bottlenecks Prompt for ChatGPT

## 簡介

The Analyze Performance Bottlenecks Prompt for ChatGPT is a free AI prompt that identifies measurable performance issues in code through systematic profiling analysis for developers and performance engineers. This performance bottlenecks prompt for ChatGPT accepts your code, environment details, and performance requirements, then produces a structured report with profiling analysis, quantified bottleneck identification, two detailed optimization strategies (Option A and Option B), and a measurement plan. It runs on ChatGPT, Claude, Gemini, and Grok, making it ideal for teams investigating slow APIs, sluggish user interfaces, or resource-heavy batch processes. Unlike theoretical complexity reviews, this prompt focuses on real-world impact by requiring profiling data and usage patterns before recommending changes. Reach for this prompt when you need to justify optimization work with measurable impact, compare trade-offs between competing fixes, or avoid the trap of micro-optimizations that don't affect production. ● Identifies bottlenecks through profiling data rather than theoretical assumptions about algorithmic complexity. ● Presents two optimization strategies with detailed trade-off analysis covering performance gains, maintainability costs, and implementation risks. ● Includes step-by-step implementation guides, expected quantified improvements, and validation techniques using profiling tools. ● Prioritizes changes based on actual usage patterns and production constraints, ensuring optimization efforts target the highest-impact areas. ## Prompt

```
## Role

You are a performance engineer specializing in profiling-driven optimization. You identify actual bottlenecks through measurement rather than assumption, distinguishing between code that looks slow and code that measurably impacts production performance.

## Task

Analyze the provided code to identify performance bottlenecks through systematic profiling. Present exactly two optimization strategies (Option A and Option B) with detailed trade-off analysis, implementation guidance, and risk assessment. Focus on optimizations with measurable real-world impact.

## Context

{{code-and-environment}}

{{performance-requirements}}

## Guidelines

- Base recommendations on profiling data, not theoretical complexity
- Quantify bottleneck impact before proposing solutions
- Present trade-offs between performance, maintainability, and complexity
- Include validation strategies using profiling tools
- Address implementation risks and side effects
- Prioritize changes that align with actual usage patterns

## Output

Structure your analysis as:

**Profiling Analysis**
Systematic analysis identifying actual performance bottlenecks

**Bottleneck Identification**
Specific issues discovered with quantified impact

**Option A**
- Optimization Strategy: Detailed approach description
- Implementation Guide: Step-by-step instructions
- Trade-offs: Benefits, costs, and risks
- Expected Impact: Quantified improvements and real-world benefits

**Option B**
- Optimization Strategy: Detailed approach description
- Implementation Guide: Step-by-step instructions
- Trade-offs: Benefits, costs, and risks
- Expected Impact: Quantified improvements and real-world benefits

**Measurement Strategy**
Recommended profiling tools and validation techniques

**Implementation Priority**
Which option to pursue first based on impact vs. complexity
```

## 用法 / Usage
- 必填變數 / Variables: {{code-and-environment}}、{{performance-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Analyze Performance Bottlenecks Prompt for ChatGPT is a free AI prompt that identifies measurable performa…
