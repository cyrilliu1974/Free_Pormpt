# Meeting Management Platform Builder

## 簡介

The Meeting Management Platform Builder is a free AI prompt that generates complete development plans for collaboration platforms covering scheduling, real-time meetings, and post-meeting workflows for full-stack engineers and product teams. This meeting management platform prompt for ChatGPT produces a step-by-step technical blueprint including project architecture, data models, calendar integration, live collaboration features, and analytics dashboards. Running on ChatGPT, Claude, or Cursor, it accepts your technical stack and project context as inputs, then outputs a structured development plan with TypeScript interfaces, state management patterns, API client implementations, and production-ready code examples. Teams use it to build platforms that manage the entire meeting lifecycle - from smart scheduling and agenda preparation through real-time note-taking, action item tracking, and post-meeting insights - without starting from scratch. Reach for this prompt when you need to architect a collaboration tool that balances intuitive user experience for non-technical teams with the customization depth that engineering organizations require. ● Outputs complete project architecture with folder structure, dependency manifests, and environment configuration for immediate development kickoff. ● Provides TypeScript interfaces, Zustand store patterns, and API client scaffolding for type-safe state management and data flow. ● Delivers calendar integration logic with smart scheduling algorithms, conflict detection, and time-zone handling for optimized meeting coordination. ● Includes real-time collaboration components, action item capture systems, decision logging, and post-meeting summary generation with analytics dashboards. ## Prompt

```
## Role

You are an expert full-stack engineer and product designer specializing in collaboration platforms.

## Task

Architect a production-ready meeting management platform covering the complete lifecycle from scheduling through follow-up. Build a comprehensive, step-by-step development plan based on:

{{technical-stack}}

{{project-context}}

## Context

The platform must be intuitive enough for non-technical teams yet powerful enough for customization, combining real-time collaboration with seamless user experience.

## Output

Structure your development plan with these sections:

● **Project Architecture and Setup**: Complete file structure, dependencies, and configuration
● **Core Data Models and State Management**: TypeScript interfaces, state stores, and API clients
● **Calendar and Scheduling Interface**: Smart scheduling with calendar integration and time optimization
● **Pre-Meeting Workspace**: Agenda builder, document management, and readiness tracking
● **Live Meeting Mode**: Real-time collaboration, action item capture, and decision logging
● **Post-Meeting Hub and Analytics**: Summary generation, action item dashboard, and meeting insights
● **Polish and Performance Optimization**: Command palette, keyboard shortcuts, and performance tuning

Present specific technical implementations, code examples, and production-ready best practices for each component in bullet point format using ●.
```

## 用法 / Usage
- 必填變數 / Variables: {{project-context}}、{{technical-stack}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Meeting Management Platform Builder is a free AI prompt that generates complete development plans for coll…
