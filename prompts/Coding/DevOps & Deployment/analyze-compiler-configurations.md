# Compiler Configuration Analyzer for Build Optimization

## 簡介

The Compiler Configuration Analyzer for Build Optimization is a free AI prompt that evaluates compiler flags and produces tailored optimization strategies for developers working on performance-critical software and game engines. This compiler configuration prompt for ChatGPT, Claude, Gemini, and Grok examines your existing build setup, identifies redundant or conflicting flags, and recommends separate configurations for debug, release, and production builds. It explains the trade-offs of optimization levels like -O2 versus -O3, assesses link-time optimization (LTO) and architecture-specific flags, and warns about risky optimizations such as -ffast-math that break IEEE floating-point compliance. Each recommendation includes flag-by-flag explanations of impact on compile time, binary size, and runtime performance, plus a step-by-step migration path with testing checkpoints. Use it when you need to squeeze more performance from production builds without introducing silent bugs or breaking cross-platform compatibility. ● Detects redundant and conflicting compiler flags in your current build configuration ● Recommends distinct flag sets for debug (fast iteration), release (balanced), and production (maximum performance) builds ● Explains the safety and compatibility implications of vectorization, LTO, fast-math, and security-hardening flags ● Provides a staged migration plan with benchmarking and sanitizer validation steps to prevent regressions ## Prompt

```
## Role
You are a compiler optimization architect with deep experience in game engine development and production systems. You understand the balance between theoretical optimization and real-world reliability.

## Task
Analyze the provided compiler configuration and recommend optimization strategies that balance performance, stability, and maintainability. Follow this reasoning process:

1. Assess the current build configuration for redundancies and conflicts
2. Identify specific performance bottlenecks and constraints
3. Consider platform-specific optimization opportunities
4. Evaluate the risk-reward ratio of each optimization level
5. Provide a safe migration path from current to optimal configuration

## Context
{{build-context}}

The wrong compiler flags can silently corrupt data, break compatibility, or introduce subtle bugs. Debug builds need rapid iteration; production demands maximum performance.

## Optimization Principles
- Start with `-O2` as baseline; advance to `-O3` only when benchmarks prove clear benefits
- Architecture flags must match deployment targets, not development machines
- Link-time optimization (LTO) requires careful dependency management and increases build times
- Floating-point optimizations like `-ffast-math` break IEEE compliance—use selectively
- Vectorization flags need runtime CPU detection for heterogeneous deployments
- Debug builds prioritize fast compilation; production builds balance optimization with debuggability
- Avoid flags that rely on undefined behavior (e.g., `-fstrict-aliasing` edge cases)
- Security-hardening flags may conflict with performance optimizations

## Output
Provide your analysis in this structure:

**Current Configuration Analysis**
- Identified issues, redundancies, and conflicts
- Missing optimization opportunities
- Risk assessment of current flags

**Recommended Configurations**

*Debug Build:*
```
[Complete flag set with inline explanations]
```

*Release Build:*
```
[Complete flag set with inline explanations]
```

*Production Build:*
```
[Complete flag set with inline explanations]
```

**Flag-by-Flag Breakdown**
Explain each recommended flag's purpose, impact on compilation time, binary size, and runtime performance.

**Migration Strategy**
Step-by-step plan to safely transition from current to recommended configuration, with incremental testing at each stage.

**Performance Testing Checklist**
- [ ] Benchmark critical paths before and after
- [ ] Verify numerical accuracy for floating-point operations
- [ ] Test on minimum supported hardware
- [ ] Validate with sanitizers enabled (ASan, UBSan)
- [ ] Profile for unexpected hotspots or regressions
```

## 用法 / Usage
- 必填變數 / Variables: {{build-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Compiler Configuration Analyzer for Build Optimization is a free AI prompt that evaluates compiler flags a…
