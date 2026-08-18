# UI Modernization Prompt for Dashboard Refactoring

## 簡介

The UI Modernization Prompt for Dashboard Refactoring is a free AI prompt that transforms outdated dashboard code into polished, production-ready React components with modern design systems, accessibility standards, and performance optimizations for developers and UI/UX engineers. This dashboard modernization prompt for ChatGPT, Claude, and Cursor takes your existing dashboard specification and refactors it into a complete implementation using React 18+ hooks, Tailwind CSS utilities, and current best practices. It delivers structured output including an analysis summary, a cohesive design system foundation (color palette, typography scale, spacing system), fully commented component code, performance enhancements like lazy loading and memoization, WCAG 2.1 AA accessibility compliance with ARIA labels and keyboard navigation, and detailed micro-interactions including loading states, transitions, and user feedback mechanisms. Real use cases include modernizing internal admin panels, updating SaaS product dashboards, and refreshing client-facing analytics interfaces without breaking existing functionality. Reach for this prompt when you need to upgrade a legacy dashboard UI but must preserve every feature while improving visual hierarchy, reducing cognitive load, and meeting modern accessibility and performance standards. ● Applies a cohesive design system with defined color palettes, typography scales, spacing systems, and visual hierarchy principles tailored to your dashboard. ● Outputs complete React component code with Tailwind CSS utilities, inline comments explaining improvements, and modern patterns like hooks and responsive design. ● Implements WCAG 2.1 AA accessibility standards including ARIA labels, keyboard navigation, focus management, and screen reader support. ● Documents performance optimizations such as code splitting, memoization, efficient re-renders, and lazy loading strategies with technical explanations. ## Prompt

```
## Role

You are a senior UI/UX engineer specializing in transforming legacy interfaces into modern, high-performing products.

## Task

Refactor the provided dashboard code into a polished, production-ready implementation that:

- Applies a cohesive design system (color, typography, spacing, visual hierarchy)
- Reduces cognitive load through improved information architecture
- Implements micro-interactions, loading states, and interaction feedback
- Meets WCAG 2.1 AA accessibility standards
- Optimizes performance (lazy loading, memoization, efficient re-renders)
- Uses modern patterns (React 18+ hooks, Tailwind CSS utilities, responsive design)
- Maintains 100% feature parity with the original

## Context

{{dashboard-specification}}

Include: complete component code or file contents, current tech stack and libraries, specific UX/design pain points to resolve, brand colors (or indicate if a modern palette is needed), and critical features that must be preserved.

## Output

Provide a structured transformation with:

**Analysis Summary**  
Map current functionality and list planned improvements.

**Design System Foundation**  
Define color palette, typography scale, spacing system, and visual hierarchy principles.

**Enhanced Component Code**  
Complete, production-ready React components with Tailwind CSS. Include inline comments explaining key improvements.

**Performance & Accessibility**  
Document technical optimizations (code splitting, memoization) and accessibility enhancements (ARIA labels, keyboard navigation, focus management).

**Micro-Interactions & Modern Patterns**  
Describe animations, transitions, loading states, empty states, and user feedback mechanisms implemented.

**Implementation Notes**  
Explain design decisions, assumptions, mobile responsiveness strategy, and any trade-offs made.

Deliver complete, working code ready for immediate implementation with zero functionality loss.
```

## 用法 / Usage
- 必填變數 / Variables: {{dashboard-specification}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The UI Modernization Prompt for Dashboard Refactoring is a free AI prompt that transforms outdated dashboard c…
