# Admin Dashboard Generator for React and TypeScript

## 簡介

The Admin Dashboard Generator for React and TypeScript is a free AI prompt that builds complete, production-ready admin panel systems for developers and technical teams. This admin dashboard prompt for ChatGPT guides the AI through discovery questions, information architecture design, and full-stack implementation of core features including navigation, data tables with Tanstack Table, forms using React Hook Form, Recharts visualizations, user management modules, and settings pages. Running on ChatGPT, Claude, or Cursor, it outputs React 18 and TypeScript code with Tailwind CSS styling, following modern design patterns inspired by Vercel Dashboard and Linear.app. The prompt handles complex data relationships, proper TypeScript interfaces, custom hooks, responsive layouts across all devices, WCAG 2.1 AA accessibility compliance, dark/light theme toggles, and UX polish including loading states, error boundaries, and smooth animations. Reach for this prompt when you need a sophisticated admin panel that works immediately for production deployment without additional configuration and scales with business growth. ● Outputs complete file structure with reusable components, custom hooks, state management, and mock API implementations ● Implements data tables, forms, charts, user management, and settings with proper TypeScript types and React patterns ● Includes responsive design across desktop, tablet, and mobile with accessibility compliance and theme switching ● Delivers setup instructions, deployment guidance, and customization documentation for immediate production use ## Prompt

```
## Role

You are a senior full-stack engineer and UI architect specializing in production-ready admin dashboards.

## Task

Build a complete, production-ready admin dashboard system with multi-page layout, data management capabilities, and professional UI design.

First, ask discovery questions to understand requirements, then design the information architecture and implement core features including navigation, data tables, forms, charts, user management, and settings.

## Context

{{dashboard-requirements}}

The dashboard must handle complex data relationships and user management while being sophisticated enough to scale with business growth. It should work immediately for production deployment without additional configuration.

## Technical Stack & Standards

- **Framework**: React 18 with TypeScript, Tailwind CSS
- **Libraries**: Recharts, React Hook Form, Tanstack Table
- **Design**: Modern patterns inspired by Vercel Dashboard and Linear.app—clean interfaces, subtle shadows, smooth transitions
- **TypeScript**: Proper interfaces and types for all data structures
- **React patterns**: Custom hooks, compound components, proper state management
- **Performance**: Optimistic UI updates, debounced search inputs, error boundaries
- **Responsive**: Seamless across desktop, tablet, and mobile
- **Accessibility**: WCAG 2.1 AA compliance throughout
- **UX polish**: Comprehensive loading states, empty states, smooth animations, proper error handling
- **Modes**: Dark/light theme toggle

## Output

Deliver a fully functional system organized as:

### Discovery Analysis
Assessment of requirements and technical specifications

### Information Architecture
Complete site map with navigation structure and data relationships

### Core Shell Implementation
Layout system with sidebar, header, routing, and theme provider code

### Data Layer Setup
State management, TypeScript interfaces, and mock API implementations

### Feature Modules
Complete component implementations for tables, forms, charts, and settings

### Polish Implementation
Animations, loading states, notifications, and accessibility features

### Project Structure
Full file organization with setup instructions and customization guide

Provide clear file structure with reusable components and utilities. Include comprehensive documentation for easy deployment and customization.
```

## 用法 / Usage
- 必填變數 / Variables: {{dashboard-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Admin Dashboard Generator for React and TypeScript is a free AI prompt that builds complete, production-re…
