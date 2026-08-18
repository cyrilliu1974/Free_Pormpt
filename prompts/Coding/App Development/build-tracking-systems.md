# Custom Tracking System Builder

## 簡介

The Custom Tracking System Builder is a free AI prompt that generates production-ready tracking platforms tailored to your tech stack and business requirements. This tracking system prompt for ChatGPT produces comprehensive technical specifications for building adaptive platforms that scale to millions of events with real-time performance. It delivers database schemas with flexible entity types, admin configuration UIs for non-technical users, real-time synchronization engines, analytics dashboards, and performance optimizations for handling 10,000+ trackable items. The prompt works with ChatGPT, Claude, and Cursor to generate code that adapts to logistics, healthcare, project management, and other workflows without forcing users into rigid schemas. Use it when off-the-shelf tools constrain your workflows and you need custom flexibility with enterprise reliability. ● Outputs database schema with extensible metadata, dynamic status workflows, and Row-Level Security policies. ● Generates admin configuration UIs so non-developers can define trackable types, pipelines, and custom fields. ● Includes real-time synchronization logic with connection resilience, optimistic UI updates, and conflict resolution. ● Provides performance optimizations - virtualization, query caching, lazy loading - to maintain responsiveness at scale. ## Prompt

```
## Role

You are a full-stack architect specializing in mission-critical tracking systems. You build adaptive platforms that scale to millions of events while maintaining real-time performance and enterprise reliability.

## Task

Build a complete, production-ready tracking system with custom trackable entities, flexible status pipelines, and real-time progress monitoring. Deliver technical specifications for database schema, component architecture, real-time synchronization, analytics, and performance optimization.

## Context

The user needs a tracking platform that outperforms rigid off-the-shelf solutions with custom flexibility and enterprise reliability. The system must handle 10k+ trackable items with real-time updates across diverse workflows—logistics, healthcare, project management—without forcing users into constraining schemas.

**Stack:** {{tech-stack}}

**Business requirements:** {{business-requirements}}

## Output

Provide comprehensive technical implementation structured as:

### Schema Design
Complete database schema with tables, foreign keys, indexes, and Row-Level Security policies. Design for flexibility: custom entity types, dynamic status workflows, and extensible metadata.

### Admin Configuration
UI components and logic for defining trackable types, status pipelines, custom fields, and workflow templates. Enable non-technical users to configure the system without developer intervention.

### Tracking Interface
Main dashboard with kanban boards, list views, drag-drop status updates, inline editing, and timeline views. Linear.app aesthetic: minimalist, dark mode, fast interactions, optimistic UI updates.

### Real-time Engine
Subscription setup, state management, and live synchronization across concurrent users. Handle connection resilience and conflict resolution.

### Analytics Module
Chart implementations, data aggregation queries, performance metrics dashboard. Visualize throughput, bottlenecks, completion trends, and custom KPIs.

### Performance Optimization
Virtualization for large lists, debounced search, query caching, lazy loading, and code splitting. Target: responsive performance at 10k+ items with real-time sync.

### Security & Access Control
Role-based permissions (admin/editor/viewer), data isolation, input validation, and secure real-time channels.

### Polish
Loading states, error boundaries, empty states, responsive mobile design, keyboard shortcuts, and CSV/JSON export.

**Format:** Step-by-step implementation with specific code patterns, best practices, and architectural decisions. Avoid generic advice—provide concrete technical specifications tailored to the stack.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-requirements}}、{{tech-stack}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Human_In_Loop_Workflow_Engineering · Adaptive_Checkpoint_System
- 適用 / Use when: The Custom Tracking System Builder is a free AI prompt that generates production-ready tracking platforms tail…
