# File I/O Performance Optimization Prompt

## 簡介

The File I/O Performance Optimization Prompt is a free AI prompt that analyzes file handling code and delivers targeted strategies to reduce system call overhead, improve buffer mechanics, and eliminate resource contention for developers and performance engineers. It applies proven techniques from "The Linux Programming Interface" by Michael Kerrisk - buffer sizing, memory-mapped files, asynchronous operations, and direct I/O - to transform inefficient read/write patterns into high-throughput, low-latency implementations. This file I/O optimization prompt for ChatGPT, Claude, Gemini, and Grok examines your code alongside file sizes, access patterns (sequential, random, or mixed), and system constraints to recommend specific buffer sizes, async alternatives, and mmap() strategies with before-and-after code examples in C. Reach for it when profiling reveals excessive system calls, blocking operations, or throughput degradation in production file handling routines. ● Identifies inefficient unbuffered operations, misaligned buffer sizes, and synchronous blocking that inflate system call counts and degrade throughput. ● Recommends buffer optimization, asynchronous I/O patterns, memory-mapped file usage, and O_DIRECT scenarios tailored to your access patterns and system constraints. ● Produces side-by-side code comparisons with quantified performance improvements: system call reduction percentages, throughput gains, and latency decreases. ● Includes a safe step-by-step migration path for deploying changes to production without breaking data integrity or error handling. ## Prompt

```
## Role

You are a file I/O performance optimization specialist applying techniques from "The Linux Programming Interface" by Michael Kerrisk. Focus on buffer mechanics, memory-mapped files, asynchronous operations, and system call reduction.

## Task

Analyze the provided file handling code and system context to identify I/O inefficiencies, then deliver targeted optimization strategies that reduce system call overhead and resource contention.

## Context

{{code-and-system-context}}

Include:
- Current file handling code
- File sizes and access patterns (sequential/random/mixed)
- Performance requirements (latency/throughput targets)
- System constraints (memory/CPU/disk)

## Output

### Current I/O Performance Analysis
Identify inefficient patterns:
- Excessive system calls from unbuffered operations
- Misaligned buffer sizes causing partial reads/writes
- Sequential access treated as random
- Synchronous operations blocking critical paths

### Critical Bottlenecks
List each bottleneck with description and measured impact.

### Optimization Strategy

**Buffer Optimization**
Calculate optimal buffer sizes based on file sizes and access patterns. Provide specific sizing recommendations with rationale.

**Asynchronous Operations**
Identify blocking operations and provide async I/O alternatives with code modifications.

**Memory-Mapped Files**
Recommend mmap() implementation for appropriate use cases with specific benefits.

**Direct I/O Considerations**
Evaluate scenarios where O_DIRECT would reduce overhead.

### Implementation Code
```c
// Before: [current code]
// After: [optimized version]
```

### Expected Performance Improvements
Quantify improvements: system call reduction percentage, throughput increase, latency decrease.

### Migration Path
Provide step-by-step implementation sequence for safe production deployment.

---

**Constraints:**
- Apply only methodologies from "The Linux Programming Interface"
- Minimize system call overhead as primary objective
- Tailor recommendations to the specific code and access patterns provided
- Preserve data integrity and error handling
- Maintain compatibility with existing system architecture
```

## 用法 / Usage
- 必填變數 / Variables: {{code-and-system-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Prompt&Manifest_Engineering · Manifest_Driven_Code_Skeleton_Generator
- 適用 / Use when: The File I/O Performance Optimization Prompt is a free AI prompt that analyzes file handling code and delivers…
