# Testing Dashboard Builder for Multi-Framework Integration

## 簡介

The Testing Dashboard Builder for Multi-Framework Integration is a free AI prompt that generates a complete technical implementation plan for building a production-grade testing dashboard for development teams. This testing dashboard prompt for ChatGPT, Claude, Gemini, and Grok produces a detailed architecture covering framework adapters (Jest, Vitest, Pytest, RSpec), WebSocket-based real-time streaming, analytics engines, React component hierarchies with TypeScript interfaces, filtering systems with URL state management, and a complete visual design system with dark-theme specifications. The output includes concrete architectural decisions, technology choices, code patterns, and a seven-phase implementation roadmap with technical milestones. Use it when you need to consolidate test results from multiple frameworks into a unified, real-time dashboard with coverage heatmaps, flaky test detection, and trend analysis. ● Framework adapter layer design that unifies data from Jest, Vitest, Pytest, RSpec, and other testing tools into a single format. ● Real-time WebSocket streaming implementation for live test event updates during continuous integration runs. ● Analytics engine with metrics calculation, data persistence strategy, coverage heatmaps, and flaky test detection. ● Complete UI component structure with React/TypeScript interfaces, advanced filtering, keyboard shortcuts, virtualization, and responsive dark-theme design specs including color codes and animations. ## Prompt

```
## Role

You are a senior full-stack engineer and UX architect specializing in developer tooling and testing infrastructure.

## Task

Design a production-ready Testing Dashboard that integrates multiple testing frameworks and provides real-time test insights. Deliver a comprehensive technical implementation plan.

## Context

{{testing-infrastructure-context}}

## Output

Structure your response with these sections:

**Framework Architecture**: Multi-framework adapter layer design and unified data format

**Real-Time Streaming Setup**: WebSocket implementation for live test event streaming

**Analytics Engine Design**: Metrics calculation system and data persistence strategy

**UI Component Structure**: React component hierarchy with TypeScript interfaces and styling specs

**Filtering and Navigation**: Advanced filtering with URL state management and keyboard shortcuts

**Visual Design System**: Complete specifications including color codes, typography, animations, and responsive behavior for dark theme UI

**Performance Optimization**: Virtualization, lazy loading, and strategies for handling large test suites

**Implementation Roadmap**: Seven-phase development plan with deliverables and technical milestones

Provide specific architectural decisions, technology choices, and concrete code patterns. Focus on scalability, maintainability, and developer experience. Include coverage heatmaps, flaky test detection, trend analysis features, accessibility features, and performance benchmarks where relevant.
```

## 用法 / Usage
- 必填變數 / Variables: {{testing-infrastructure-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Testing Dashboard Builder for Multi-Framework Integration is a free AI prompt that generates a complete te…
