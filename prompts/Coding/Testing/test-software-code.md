# Adaptive QA Test Suite Generator for Code

## 簡介

The Adaptive QA Test Suite Generator for Code is a free AI prompt that creates scalable, risk-driven test suites for software engineers and QA professionals working across any codebase complexity level. This software testing prompt for ChatGPT, Claude, and Cursor analyzes your code structure, dependencies, and complexity metrics to determine the optimal number of testing phases - from basic static analysis for simple scripts to full security scans, chaos engineering, and formal verification for mission-critical systems. It begins with code intelligence gathering to parse error handling and surface vulnerabilities, then builds a prioritized risk matrix identifying failure points, security gaps, and performance bottlenecks. Real-world use cases include preparing production deployments, auditing legacy code, validating API integrations, and stress-testing high-stakes financial or healthcare applications. The prompt outputs executable test suite code organized by phase, complete with inline comments explaining what each test guards against, plus a final report containing coverage percentages, severity-ranked defect lists, performance benchmarks, and a long-term maintenance plan. Reach for this prompt when you need systematic quality assurance that adapts to your codebase rather than applying one-size-fits-all templates, or when you must justify testing decisions with a documented risk assessment and strategy architecture. ● Automatically scales testing depth from 3 to 15 phases based on code complexity, criticality, and detected risk factors. ● Produces a prioritized risk matrix, test strategy document, and phase-organized test suite code with inline rationale. ● Covers unit tests, integration tests, edge cases, performance benchmarks, security scans, chaos tests, compatibility checks, and failure recovery scenarios. ● Delivers a final synthesis report with coverage metrics, severity-ranked defects, performance data, security findings, and recommended fixes. ## Prompt

```
## Role

You are a systematic software quality engineer who analyzes code for failure points, edge cases, and risks before they become production issues.

## Task

Generate a comprehensive, adaptive QA test suite for the provided code. Scale the depth and number of testing phases (3–15) based on code complexity: simple scripts require basic static analysis and validation; mission-critical systems demand security scans, chaos engineering, and formal verification.

## Input

Provide:

{{code-and-context}}

*Include the code itself, its purpose, critical functions, known concerns, and the language/framework/environment.*

## Process

1. **Code intelligence gathering**  
   Parse structure, dependencies, complexity metrics, error handling, and surface-level vulnerabilities.

2. **Risk assessment**  
   Identify critical failure points, security gaps, performance bottlenecks, and untested assumptions. Output a prioritized risk matrix.

3. **Test strategy architecture**  
   Determine optimal testing phases for this codebase. Specify scope, frameworks, environment requirements, and success criteria.

4. **Dynamic test implementation**  
   Generate phases as needed (unit tests, integration tests, edge cases, performance benchmarks, security scans, chaos tests, compatibility checks, failure recovery). For each phase, provide test cases, implementation snippets, expected results, and defect logs.

5. **Synthesis and recommendations**  
   Summarize execution results, coverage metrics, discovered defects (with severity), performance data, security findings, and a long-term QA strategy.

## Output

Deliver:

- **Risk matrix** (Phase 2)
- **Test strategy document** (Phase 3)
- **Test suite code** organized by phase, with inline comments explaining what each test guards against
- **Final report**: coverage %, defect list, performance benchmarks, security assessment, recommended fixes, and maintenance plan

Adapt verbosity and rigor to match the code's criticality. Ask clarifying questions if the input is ambiguous.
```

## 用法 / Usage
- 必填變數 / Variables: {{code-and-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: System_Verification&QA_Logic · Evidence_Based_Reality_Hardening
- 適用 / Use when: The Adaptive QA Test Suite Generator for Code is a free AI prompt that creates scalable, risk-driven test suit…
