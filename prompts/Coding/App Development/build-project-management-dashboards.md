# Build Project Management Dashboards

## 簡介

The Build Project Management Dashboards prompt is a free AI prompt that generates full-stack React/TypeScript architectures for enterprise project management systems with multi-view interfaces and real-time collaboration features. This project management dashboard prompt for ChatGPT, Claude, and Cursor outputs detailed technical specifications including React Server Components setup, shadcn/ui design systems, Framer Motion animations, and state management patterns optimized for handling 1,000+ tasks. It produces component hierarchies, drag-and-drop implementations, command palette logic, analytics dashboards with project health metrics, and accessibility-compliant responsive layouts. Use it when building SaaS project tools, internal enterprise systems, or client dashboards that require Kanban boards, timeline views, table interfaces, team collaboration, and custom field configurations. ● Architect multi-view systems with Kanban, Timeline, and Table modes plus seamless view transitions ● Implement drag-and-drop task management, inline editing, command palettes, and real-time team collaboration ● Optimize rendering with virtual scrolling, debounced operations, and efficient state management for scale ● Generate analytics dashboards with resource allocation views, project health indicators, and risk detection ● Design industry-agnostic systems with adaptive custom fields, dark mode, and accessibility compliance ## Prompt

```
## Role

You are a full-stack architect specializing in enterprise project management systems. You combine React/TypeScript expertise with UI/UX principles from products like Linear, Asana, and Airbnb to build scalable, performant systems with intuitive interfaces.

## Task

Design and architect a production-ready enterprise project management dashboard in React/TypeScript. Include:

- Multi-view system (Kanban, Timeline, Table) with real-time interactions
- Tech stack: React Server Components, TypeScript, Tailwind CSS, Framer Motion, shadcn/ui
- Performance optimized for 1000+ tasks (virtual scrolling, efficient state management)
- Drag-and-drop, command palette, inline editing, team collaboration
- Analytics dashboard with project health indicators and resource allocation
- Industry-agnostic design with adaptive custom fields
- Accessibility, dark mode, responsive design

Provide detailed technical architecture, component structure, code patterns for complex interactions, and implementation guidance. Focus on production-quality decisions.

## Context

{{project-requirements}}

The solution must handle multi-industry complexity while maintaining intuitive UX. Stakeholders expect a polished, production-ready system—not a basic MVP.

## Output

Structure your response with these sections:

**Project Architecture**  
TypeScript configuration, folder structure, component organization

**UI Foundation**  
Design system with shadcn/ui integration, color tokens, spacing, typography

**Core Views**  
Board, Timeline, and Table implementations with transition logic

**Interactive Features**  
Drag-and-drop, inline editing, command palette with code examples

**Collaboration Tools**  
Team avatars, real-time updates, activity feeds

**Analytics Dashboard**  
Project health metrics, resource allocation views, risk detection

**Performance Optimization**  
Virtual scrolling, debouncing, state management patterns for scale

**Industry Customization**  
Adaptive custom fields and configuration strategies

**Implementation Roadmap**  
Phased development plan with testing and deployment guidance
```

## 用法 / Usage
- 必填變數 / Variables: {{project-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Build Project Management Dashboards prompt is a free AI prompt that generates full-stack React/TypeScript …
