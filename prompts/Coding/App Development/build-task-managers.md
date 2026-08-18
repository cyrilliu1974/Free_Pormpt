# Build Task Manager App – React TypeScript Prompt

## 簡介

The Build Task Manager App – React TypeScript Prompt is a free AI prompt that generates a complete development guide for creating adaptive task management applications tailored to specific industries and workflows. This task manager app prompt for ChatGPT, Claude, and Cursor produces a full-stack development blueprint including component architecture, industry-specific templates, drag-and-drop kanban boards, state management patterns, and UI implementation using React, TypeScript, Tailwind CSS, shadcn/ui, and Framer Motion with LocalStorage persistence. The prompt adapts to your industry workflow, technical experience level, and feature priorities - delivering step-by-step implementation guidance for building a Linear.app-style interface with Notion-like functionality that handles 500+ tasks with optimized performance. It covers responsive mobile-first design, WCAG accessibility standards, natural language task input, comprehensive search and filtering, and production deployment strategies. Reach for this prompt when you need to build a production-grade task management system that feels native to specific user workflows, whether for software teams, creative agencies, healthcare operations, or any domain requiring adaptive productivity tools. ● Industry template system that auto-generates workflow columns, task fields, and presets customized to the user's domain and mental model. ● Complete technical stack guidance including React hooks and context for state management, code splitting and virtualization for performance, and component composition patterns. ● Mobile-first responsive design with touch-optimized drag-and-drop interactions, keyboard navigation, ARIA labels, and progressive enhancement. ● Production-ready implementation covering kanban and list views, priority color coding, natural language quick-add, comprehensive search, and deployment configuration. ## Prompt

```
## Role
Expert full-stack developer specializing in React, TypeScript, and adaptive productivity applications.

## Task
Build a fully adaptive task management application using React, TypeScript, Tailwind CSS, shadcn/ui, and Framer Motion with LocalStorage persistence.

## Context
**Core functionality:**
- Industry-specific templates that auto-generate workflow columns, task fields, and presets
- Drag-and-drop kanban board with toggleable list view
- Priority color coding and natural language quick-add
- Comprehensive search and filtering
- Performance optimized for 500+ tasks

**Design requirements:**
- Linear.app aesthetics meets Notion functionality: clean typography, generous whitespace, subtle shadows, smooth transitions
- Mobile-first responsive design with touch-optimized interactions
- WCAG accessibility standards

**Technical architecture:**
- Component composition with clear separation of concerns
- Efficient state management using React hooks and context
- Code splitting and virtualization for performance
- Responsive breakpoints and progressive enhancement

Customize based on:
- {{industry-workflow}}: the primary industry/use case, target users, and key workflow patterns
- {{technical-context}}: React/TypeScript experience level, development timeline, and deployment constraints
- {{feature-priorities}}: UI/UX preferences, brand requirements, and ranked feature importance

## Output
Provide a complete development guide with:

**Architecture Overview**
Technical stack decisions, folder structure, and component hierarchy

**Industry Template System**
Implementation of smart templates that customize the workspace based on user selection

**Core Features Development**
Step-by-step implementation of kanban board, task CRUD operations, drag-and-drop, quick-add, and search

**UI Component Library**
shadcn/ui integration with custom components for consistent design system

**State Management**
React patterns for managing tasks, filters, views, and user preferences

**Responsive & Accessibility**
Mobile-first design, touch interactions, keyboard navigation, and ARIA labels

**Performance Optimization**
Virtualization for large lists, memoization strategies, and bundle optimization

**Deployment Guide**
Production build configuration and recommended hosting solutions

Include specific code examples, handle edge cases, and explain architectural decisions throughout.
```

## 用法 / Usage
- 必填變數 / Variables: {{feature-priorities}}、{{industry-workflow}}、{{technical-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Prompt&Manifest_Engineering · Manifest_Driven_Code_Skeleton_Generator
- 適用 / Use when: The Build Task Manager App – React TypeScript Prompt is a free AI prompt that generates a complete development…
