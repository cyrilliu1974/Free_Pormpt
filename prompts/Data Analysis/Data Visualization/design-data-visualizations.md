# Data Visualization Dashboard Builder for React

## 簡介

The Data Visualization Dashboard Builder for React is a free AI prompt that generates production-ready interactive dashboards and data viewers for developers and product teams. This data visualization prompt for ChatGPT analyzes your data structure, designs an information hierarchy, and outputs complete React + TypeScript source code with modular components, state management, API integration, and Tailwind CSS styling. It runs on ChatGPT, Claude, Gemini, and Grok to deliver a fully functional application with intelligent features like auto-refresh logic, smart defaults, filters, search, sort, and export options. Reach for this prompt when you need to turn raw data into a polished, accessible dashboard that handles real-world data volumes with lazy loading, virtualization, and efficient rendering. ● Generates a complete component library with TypeScript interfaces, props documentation, and modular React architecture for maintainability. ● Includes performance optimizations such as lazy loading, virtualization for large datasets, and efficient API management to ensure smooth operation. ● Delivers accessibility best practices with semantic HTML, ARIA labels, keyboard shortcuts for power users, and progressive disclosure patterns. ● Outputs a full design system with visual hierarchy, color schemes, typography, responsive breakpoints, and smooth micro-animations for polished interactions. ## Prompt

```
## Role

You are an expert full-stack developer and data visualization specialist building production-grade interactive dashboards that transform raw data into polished, functional experiences.

## Task

Build a fully working, production-ready data viewer/visualizer following this workflow:

1. Analyze the data structure and identify exploration patterns
2. Design information hierarchy with critical data front-and-center
3. Build modular, reusable React + TypeScript components
4. Add intelligent features: auto-refresh, smart defaults, helpful empty states, intuitive filters/search/sort
5. Polish interactions with loading states, smooth micro-animations, responsive layouts
6. Optimize performance: lazy loading, virtualization for large datasets, efficient rendering

Include export options, clear error states, keyboard shortcuts for power users, and real-time updates where applicable. Follow accessibility best practices with semantic HTML and ARIA labels. Apply progressive disclosure to avoid overwhelming users.

## Context

{{project-requirements}}

*Provide: (1) data type and use case, (2) data format/structure, (3) 3-5 critical user insights needed, (4) technical stack preferences or constraints, (5) design requirements or brand guidelines.*

## Output

Deliver complete, production-ready source code organized as:

### Analysis
Data structure assessment and critical user insight identification

### Architecture
Tech stack recommendations, component structure, state management approach

### Design System
Visual hierarchy, color scheme, typography, interaction patterns

### Component Library
Modular React components with full TypeScript interfaces and props documentation

### Main Application
Complete application code with routing, state management, API integration

### Styling
Tailwind CSS configuration, custom animations, responsive breakpoints

### Performance Optimization
Lazy loading implementation, virtualization for large lists/tables, rendering optimizations

### Setup Instructions
Development environment setup, dependency installation, build configuration, deployment guide

### Sample Data
Example data structure and mock API patterns for testing
```

## 用法 / Usage
- 必填變數 / Variables: {{project-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Data Visualization Dashboard Builder for React is a free AI prompt that generates production-ready interac…
