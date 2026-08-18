# Thread Pool Configuration Optimizer for Java

## 簡介

The Thread Pool Configuration Optimizer for Java is a free AI prompt that calculates optimal thread pool sizes and executor settings for high-throughput production systems. The prompt applies mathematical formulas - including Little's Law and the cores × (1 + wait-time/compute-time ratio) calculation - to analyze your concurrent architecture, identify thread starvation and context switching bottlenecks, then recommend specific ExecutorService configurations with detailed reasoning. This thread pool optimization prompt for ChatGPT, Claude, Gemini, and Grok walks through current state assessment, workload characterization (CPU-bound versus I/O-bound tasks), mathematical sizing calculations with stated assumptions, bottleneck identification, and concrete configuration parameters for core pool size, max pool size, keep-alive duration, queue selection, and rejection policies. Reach for it when tuning Java concurrency in production environments where thread misconfigurations cascade into performance degradation and failures. ● Performs current state analysis of threading model architecture, workload types, and resource utilization patterns. ● Calculates optimal pool sizes using Little's Law and wait-to-compute ratio formulas, showing all work and assumptions. ● Identifies thread starvation points, context switching overhead, and resource contention patterns. ● Delivers specific ExecutorService configurations with pool size parameters, queue selection, rejection policies, and Java code examples. ## Prompt

```
## Role
You are an expert Java concurrency architect specializing in thread pool optimization and performance tuning for high-throughput production systems.

## Task
Analyze the provided concurrent system and calculate optimal thread pool configurations using Little's Law and the formula `thread count = cores × (1 + wait-time/compute-time ratio)`. Identify bottlenecks including thread starvation and excessive context switching, then provide executor configuration recommendations with detailed reasoning.

## Context
{{system-details}}

The system operates in a production environment where thread misconfigurations cascade into failures and performance degradation.

## Output
Structure your analysis with these sections:

### Current State Analysis
- Threading model architecture assessment
- Workload characterization (CPU-bound vs I/O-bound task breakdown)
- Resource utilization patterns

### Mathematical Calculations
- Apply the cores × (1 + wait/compute ratio) formula
- Calculate optimal pool sizes for each workload type
- Show all calculations with assumptions stated

### Bottleneck Identification
- Thread starvation points
- Context switching overhead
- Resource contention patterns

### Optimal Configuration Recommendations
- Specific `ExecutorService` configurations
- Pool size parameters (core, max, keep-alive)
- Queue selection and sizing
- Rejection policies

### Implementation Guidelines
- Code examples for recommended configurations
- Monitoring and tuning checkpoints
- Rollback considerations

Provide detailed bullet points with concrete values and Java code snippets where applicable.
```

## 用法 / Usage
- 必填變數 / Variables: {{system-details}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Thread Pool Configuration Optimizer for Java is a free AI prompt that calculates optimal thread pool sizes…
