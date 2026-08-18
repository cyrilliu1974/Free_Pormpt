# Frontend Filtering System Code Generator

## 簡介

The Frontend Filtering System Code Generator is a free AI prompt that builds production-ready filtering interfaces for frontend developers working with large datasets. This filtering system prompt for ChatGPT generates complete code implementations including debounced search, multi-field filtering, sorting controls, and virtual rendering techniques that maintain sub-100ms response times and 60fps scrolling even with datasets exceeding 10,000 items. It runs on ChatGPT, Claude, and Cursor, tailoring architecture and state-management patterns to your specified tech stack - whether React, Vue, Svelte, or vanilla JavaScript. The prompt delivers component code, performance optimizations (memoization, debouncing configuration, rendering strategies), accessible keyboard navigation with ARIA labels, styling solutions for filter indicators, and testing strategies including performance benchmarks. Reach for it when building dashboards, product catalogs, admin panels, or any interface where users need to search, filter, and sort through hundreds or thousands of records without lag. ● Generates debounced search and multi-field filtering logic with state management patterns matched to your framework ● Includes virtual scrolling and memoization techniques to handle 10,000+ items without pagination or frame drops ● Provides accessibility features - keyboard navigation, screen reader support, focus management, and ARIA attributes ● Outputs performance monitoring setup and testing strategies for benchmarking filter response times and rendering speed ## Prompt

```
## Role
You are a frontend architect specializing in high-performance data interfaces. You build filtering systems that handle large datasets with instant responsiveness through debouncing, virtual rendering, memoization, and progressive enhancement.

## Task
Build a production-ready smart filtering system with debounced search, multi-field filtering, sorting, and visual filter management. Deliver complete code implementations optimized for large datasets with smooth interactions, proper state management, accessibility, and performance monitoring.

## Context
{{project-context}}

## Requirements
**Tech Stack**: {{tech-stack}}

**Performance Target**: Sub-100ms filter response, smooth scrolling at 60fps, handle 10,000+ items without pagination

## Output
Provide a comprehensive solution structured as:

### Architecture Overview
System design, component structure, and separation of concerns for the filtering solution.

### Core Components
Complete implementation of filter, search, and sort components using modern patterns (hooks, composition). Include debouncing strategies, memoization, and virtual scrolling where appropriate.

### State Management
Data flow architecture and state patterns for complex filtering scenarios, optimized for the specified tech stack.

### Performance Optimizations
Specific techniques applied: debouncing configuration, memoization strategy, rendering optimizations, edge case handling. Explain architectural decisions in code comments.

### Visual Interface
CSS/styling solutions for filter indicators, responsive design, and smooth interactions with visual feedback for active filters.

### Accessibility Features
Keyboard navigation, screen reader support, ARIA labels, and focus management.

### Testing Strategy
Unit tests, integration tests, and performance benchmarking approaches tailored to the implementation.

### Monitoring & Optimization
Recommended tools and techniques for ongoing performance monitoring and dataset scaling.

Use production-ready code with error handling. Tailor implementations to the specified tech stack and project requirements.
```

## 用法 / Usage
- 必填變數 / Variables: {{project-context}}、{{tech-stack}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Dual_Layer_Prompt_Diagnostic_Scan
- 適用 / Use when: The Frontend Filtering System Code Generator is a free AI prompt that builds production-ready filtering interf…
