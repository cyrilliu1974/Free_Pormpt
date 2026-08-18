# Analyze Memory Leaks in JavaScript Applications

## 簡介

The Analyze Memory Leaks in JavaScript Applications prompt is a free AI prompt that systematically identifies and resolves memory leaks in JavaScript code for developers facing performance degradation in long-running sessions. This memory leak analysis prompt for ChatGPT examines your application code, memory symptoms, and runtime environment to detect JavaScript-specific patterns that prevent garbage collection - including detached DOM nodes, closure references capturing large scopes, event listener accumulation, circular references, persistent timers, and global variable pollution. It produces a structured report with annotated code snippets showing the problematic patterns, explanations of why the garbage collector fails, fixed implementations, and prioritized remediation steps. The prompt runs on ChatGPT, Claude, Gemini, and Grok, making it accessible across text-generation platforms. Reach for this prompt when you observe escalating memory usage, browser slowdowns, or crashes during extended user sessions and need expert forensic analysis of your JavaScript codebase. ● Detects detached DOM nodes, closure traps, event listener leaks, circular references, and timer accumulation that compound over time. ● Explains garbage collection failures for each identified pattern so you understand the root cause. ● Provides fixed code snippets with lifecycle hooks, WeakMap/WeakSet usage, and scope minimization techniques. ● Prioritizes fixes by severity and implementation ease to guide your remediation roadmap. ## Prompt

```
## Role
You are a memory forensics specialist analyzing JavaScript applications for memory leaks that prevent garbage collection.

## Task
Analyze the provided code to identify memory leaks that compound over time in long-running sessions. For each leak, explain why the garbage collector cannot reclaim memory and provide concrete disposal patterns.

## Context
{{application-code}}

{{memory-symptoms}}

{{runtime-environment}}

Systematically examine the code for these JavaScript-specific leak patterns:

- **Detached DOM nodes** that persist after removal
- **Closure references** that inadvertently capture large scopes
- **Event listener accumulation** without corresponding cleanup
- **Circular references** between objects preventing garbage collection
- **Timer/interval references** that persist indefinitely
- **Global variable pollution** creating permanent references

## Output
Deliver your findings in this structure:

**Memory Leak Analysis Report**

**Critical Findings:**
- Bullet points of most severe memory leaks discovered

**Detailed Analysis:**
For each leak pattern found:
```javascript
// Problematic Code
[code snippet]

// Why This Leaks:
[explanation of garbage collection failure]

// Fixed Code:
[solution snippet]
```

**Recommended Disposal Patterns:**
1. Lifecycle hooks for proper cleanup
2. WeakMap/WeakSet usage for appropriate references
3. Event listener management strategies
4. Closure scope minimization techniques

**Implementation Priority:**
Ordered list from highest to lowest impact, considering severity and ease of implementation.
```

## 用法 / Usage
- 必填變數 / Variables: {{application-code}}、{{memory-symptoms}}、{{runtime-environment}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Analyze Memory Leaks in JavaScript Applications prompt is a free AI prompt that systematically identifies …
