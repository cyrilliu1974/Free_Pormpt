# Testing Command Center Builder for React and TypeScript

## 簡介

The Testing Command Center Builder is a free AI prompt that generates a complete, production-ready testing framework application for QA engineers and development teams shipping critical software. This testing command center prompt for ChatGPT, Claude, and Cursor produces a full-stack React + TypeScript + Tailwind application that handles 1000+ tests without performance degradation. It generates smart test suite generators, live execution dashboards with real-time streaming, detailed failure visualization with stack traces and error categorization, interactive coverage metrics with trend analysis, performance profiling for memory and load bottlenecks, AI-powered suggestions for coverage gaps and vulnerability patterns, and flaky test detection with automatic retry logic. Teams use it to replace fragile testing setups that miss edge cases like race conditions, network timeouts, and memory leaks before they reach production. Reach for this prompt when you need a sophisticated testing infrastructure that simulates production chaos and provides actionable diagnostics to ship safely. ● Generates domain-specific test suites with organized categories, AAA pattern structure, and deterministic isolation ● Builds live execution dashboards with parallel test runners, real-time result streaming, and intelligent retry logic for flaky tests ● Creates detailed failure analysis with stack traces, error categorization, and actionable diagnostics to prevent production issues ● Implements performance profiling with load time monitoring, memory usage tracking, and bottleneck identification across the entire test suite ● Includes interactive coverage metrics with historical trend analysis, AI-powered gap detection, and vulnerability pattern recommendations ● Delivers complete React + TypeScript code with Recharts visualizations, Monaco Editor integration, keyboard shortcuts, and responsive design for 1280px+ screens ## Prompt

```
## Role

You are a senior QA architect and test automation specialist building resilient testing frameworks for production environments. You design systems that uncover real-world failure modes: network timeouts, race conditions, memory leaks, and edge cases that surface under load.

## Task

Build a complete, production-ready testing command center application that includes:

- Smart test generators that understand project context and generate domain-specific test suites
- Live execution dashboard with real-time test result streaming and parallel execution
- Detailed failure visualization with stack traces, error categorization, and actionable diagnostics
- Interactive coverage metrics with trend analysis and historical tracking
- Performance profiling (load time, memory usage, bottleneck identification)
- AI-powered suggestions for coverage gaps and common vulnerability patterns
- Test history tracking and flaky test detection with automatic retry logic

The system must handle 1000+ tests without performance degradation and provide actionable insights that prevent production failures.

## Context

The user needs a robust testing framework that simulates production chaos and provides confidence to ship safely. Previous testing approaches missed edge cases, performance bottlenecks, and real-world behavior patterns, resulting in critical production failures.

**Project details:**
{{project-context}}

## Technical Requirements

- React + TypeScript + Tailwind CSS
- Recharts for visualizations, Monaco Editor for code display
- Design aesthetic: slate grays, emerald (#10B981) for pass states, crimson (#EF4444) for failures (Linear.app meets Chrome DevTools)
- Implement keyboard shortcuts, export capabilities, responsive design (1280px+ screens)
- Follow AAA testing pattern (Arrange-Act-Assert) with deterministic, isolated test cases
- Minimize external dependencies for core testing logic
- Zero performance bottlenecks in test execution and UI rendering

## Workflow

1. **Project Assessment**: Analyze testing requirements based on project type, tech stack, and critical user flows
2. **Test Suite Architecture**: Design organized test categories with domain-specific templates and coverage strategies
3. **Execution Engine**: Build parallel test runner with real-time streaming and intelligent retry logic
4. **Dashboard Interface**: Create split-pane layout with navigation, live results, and detailed failure analysis
5. **Intelligence Layer**: Add AI-powered coverage gap analysis and edge case recommendations
6. **Performance Profiling**: Integrate monitoring for load times, memory usage, and bottleneck detection

## Output

Provide:

1. **Project Assessment**: Analysis of testing requirements and risk areas
2. **Test Suite Architecture**: Organized test categories and coverage strategies
3. **Execution Engine Design**: Parallel runner implementation with streaming and retry logic
4. **Dashboard Interface**: Complete UI layout with navigation and analysis panels
5. **Intelligence Layer**: AI-powered suggestions for missing coverage and vulnerabilities
6. **Performance Profiling**: Monitoring implementation for bottleneck identification
7. **Complete Application Code**: Full React + TypeScript implementation with all components
8. **Deployment Instructions**: Setup guide with configuration and optimization recommendations
```

## 用法 / Usage
- 必填變數 / Variables: {{project-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Testing Command Center Builder is a free AI prompt that generates a complete, production-ready testing fra…
