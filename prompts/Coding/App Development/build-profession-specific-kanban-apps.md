# Profession-Specific Kanban App Builder

## 簡介

The Profession-Specific Kanban App Builder is a free AI prompt that generates a complete, deployable React Kanban application tailored to any profession's unique workflows, terminology, and data requirements for developers and technical teams. This profession-specific Kanban app prompt for ChatGPT, Claude, and Cursor produces a single-page React application with dynamic interface adaptation, custom field schemas, drag-and-drop card management, and local persistence. Instead of generic task boards, it creates Kanban systems that mirror how different professions actually work - whether tracking patient care in healthcare, managing legal cases, coordinating event planning, or handling real estate transactions. You provide profession requirements (terminology, workflows, custom fields, validation rules) and technical specifications (React version, TypeScript, state management approach, styling framework), and receive structured, production-ready code with extensible profession definitions, adaptive card components, smooth drag-and-drop integration, and complete data management. Reach for this prompt when you need to build or prototype a Kanban tool for a specific industry that requires more than off-the-shelf task management - where domain vocabulary, workflow stages, and data validation must align with professional practice. ● Produces complete TypeScript React code with profession configuration systems, dynamic card rendering, and adaptive validation logic ● Includes drag-and-drop integration with visual feedback, state management patterns, and local storage persistence across sessions ● Delivers extensible architecture with clear profession definition schemas and examples for switching between industry contexts ● Provides inline architectural comments, TypeScript types for all data structures, and keyboard shortcuts for power users ## Prompt

```
## Role

You are an expert React architect building production-grade Kanban applications.

## Task

Create a complete, single-page React Kanban board application that dynamically adapts its interface, terminology, workflows, and data fields based on the selected profession. The application should feel purpose-built for each profession's actual work reality, not generic task management.

## Context

Profession-specific requirements (include terminology, workflows, custom fields, validation rules, and any domain-specific constraints):
{{profession-config}}

Technical specifications (React version, state management approach, TypeScript usage, styling framework, drag-and-drop library preferences, persistence requirements):
{{tech-specs}}

## Output

Deliver a complete, production-ready React implementation structured as:

**Profession Configuration System**  
Extensible profession definitions with custom terminology, workflows, and field schemas

**Core Kanban Board Architecture**  
Main dashboard layout, column structure, and responsive board container

**Dynamic Card Components**  
Profession-aware card rendering with adaptive data display and validation

**Drag-and-Drop Integration**  
Smooth card movement with visual feedback and position persistence

**Data Management and Persistence**  
State management, local storage, and multi-board support

**Interactive Features**  
Card creation/editing modals, filtering, search, and keyboard shortcuts

**Visual Design and Micro-interactions**  
Professional styling with smooth animations and loading states

Provide:
- Complete React component code with inline architectural comments
- TypeScript types for all data structures
- Clear extension points for adding new professions
- Usage examples demonstrating profession switching

The code should be immediately deployable with all imports, state logic, and event handlers fully implemented.
```

## 用法 / Usage
- 必填變數 / Variables: {{profession-config}}、{{tech-specs}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Profession-Specific Kanban App Builder is a free AI prompt that generates a complete, deployable React Kan…
