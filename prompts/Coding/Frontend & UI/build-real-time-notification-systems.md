# Real-Time Notification System Builder

## 簡介

The Real-Time Notification System Builder is a free AI prompt that generates complete, production-grade notification infrastructure with UI components, real-time transport, and smart prioritization logic for developers building modern web applications. This notification system prompt for ChatGPT, Claude, and Cursor produces a full-stack solution built with React, TypeScript, Tailwind CSS, and Framer Motion, including a notification bell with badge animations, dropdown panel with intelligent grouping, toast system with auto-dismiss, and a filterable notification center. It solves the dual challenge of preventing user fatigue from excessive alerts while ensuring critical messages are never missed, using priority-based visual hierarchy, rate limiting, and Do Not Disturb scheduling. The prompt delivers working code for real-time connection layers with reconnection logic, offline queueing, state management with optimistic updates, and performance optimizations like virtualized lists and lazy loading. Reach for this prompt when you need to implement notification features that handle high traffic, support keyboard navigation and screen readers, and maintain sub-100ms response times with smooth 60fps animations. ● Produces a complete notification schema, connection layer with WebSocket or Server-Sent Events, state management store, and all UI components organized for immediate deployment. ● Implements intelligent grouping algorithms, priority levels, bulk operations, snooze functionality, and rate limiting to prevent notification storms. ● Includes virtualized lists for performance at scale, full accessibility support with keyboard navigation and screen readers, and offline queueing with reconnection logic. ● Delivers integration guides, file structure, utility functions, and usage examples following clean design principles inspired by Linear.app and Vercel. ## Prompt

```
## Role

You are a senior full-stack developer and UX architect specializing in production-grade notification infrastructure.

## Task

Build a complete, production-ready notification system including UI components, real-time infrastructure, and intelligent prioritization logic. Deliver working code that can be deployed immediately.

## Context

{{business-context}}

The notification system must solve the dual problem of preventing both user fatigue from over-notification and missed critical alerts from under-notification. Focus on cohesive systems thinking rather than isolated components.

## Requirements

**Technical Stack:**
- React + TypeScript
- Tailwind CSS
- Framer Motion for animations
- {{real-time-transport}} (WebSockets or Server-Sent Events)

**Core Components:**
- Notification bell with animated badge
- Dropdown panel with smart grouping
- Toast system with auto-dismiss logic
- Notification center with filtering and search

**Infrastructure:**
- Real-time connection layer with reconnection logic and offline queueing
- Comprehensive state management with optimistic updates
- Intelligent grouping and priority-based visual hierarchy
- Notification schema with type, priority, timestamp, metadata, and actions

**Interaction Features:**
- Mark as read, dismiss, snooze, and inline actions
- Bulk management operations
- Do Not Disturb mode with scheduling
- Rate limiting to prevent notification storms

**Performance & Quality:**
- Virtualized lists for large notification volumes
- Lazy loading and code splitting
- Sub-100ms response times with 60fps animations
- Full keyboard navigation and screen reader support
- Proper error handling and offline support

**Design Aesthetic:**
Clean, modern interface inspired by Linear.app and Vercel—zero visual bloat, priority-driven hierarchy.

## Output

Provide complete working code organized by:

1. **Notification Schema** – Data structure definitions
2. **Connection Layer** – Real-time transport implementation
3. **State Management** – Store with grouping, sorting, optimistic updates
4. **UI Components** – All interface elements with animations
5. **Interaction Handlers** – User action logic
6. **Advanced Features** – Filtering, bulk operations, DND mode
7. **Performance Optimizations** – Virtualization, rate limiting
8. **Integration Guide** – Setup instructions, usage examples, deployment steps

Include file structure, complete component code, utility functions, and integration examples. Ensure enterprise-grade reliability suitable for immediate production deployment.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}}、{{real-time-transport}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Real-Time Notification System Builder is a free AI prompt that generates complete, production-grade notifi…
