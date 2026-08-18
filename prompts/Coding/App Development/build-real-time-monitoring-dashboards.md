# Real-Time Monitoring Dashboard Builder Prompt

## 簡介

The Real-Time Monitoring Dashboard Builder Prompt is a free AI prompt that generates enterprise-grade observability dashboards with React, TypeScript, and Tailwind CSS for teams building mission-critical monitoring systems. This monitoring dashboard prompt for ChatGPT produces a complete application structure including reusable components (MetricCard, TimeSeriesChart, AlertBanner, StatusIndicator), simulated WebSocket data streams with realistic metric patterns, state management via Zustand or Context API, and performance optimizations that maintain 60fps even with 50+ simultaneous alerts. It runs on ChatGPT, Claude, and Cursor, delivering full file organization, TypeScript interfaces, error boundaries, responsive grid layouts, and accessibility features. Use it when you need a production-ready observability interface that handles high-volume events while maintaining visual clarity during critical incidents. This prompt is for full-stack engineers, DevOps teams, and platform developers building system monitoring tools for production environments where downtime translates to revenue loss. ● Outputs complete project structure with /components, /hooks, /utils, /types directories and full implementation files. ● Includes simulated WebSocket data streams with threshold breaches, realistic metric patterns, and event log generation. ● Implements state management for real-time updates, alert handling, threshold configuration UI, and time range selectors. ● Provides performance strategies including React.memo, useMemo, graceful degradation for network failures, and scalability from mobile to ultrawide displays. ## Prompt

```
## Role

You are a senior full-stack engineer specializing in enterprise-grade observability dashboards. You build real-time monitoring systems that handle high-volume events while maintaining clarity and responsiveness during critical incidents.

## Task

Build a production-ready real-time monitoring dashboard as a React + TypeScript application with Tailwind CSS.

Implement:

- **Reusable components**: MetricCard, TimeSeriesChart, AlertBanner, StatusIndicator with smooth animations
- **Simulated WebSocket data streams** with realistic metric patterns and threshold breaches
- **Information hierarchy**: status overview cards, main visualization area, event logs sidebar
- **Responsive grid layouts** optimized from mobile incident response to ultrawide monitoring walls
- **State management** (Zustand or Context API) for real-time updates and alert handling
- **Performance optimizations** (React.memo, useMemo) maintaining 60fps with 50+ simultaneous alerts
- **Controls**: threshold configuration UI, time range selectors, keyboard shortcuts, export capabilities
- **TypeScript typing**, inline documentation, and accessibility features

## Context

{{monitoring-requirements}}

The dashboard must provide instant visual feedback during high-stress scenarios, using semantic color coding and animation patterns that enhance critical information. Design for production environments where system failures translate to business losses—monitoring that prevents disasters rather than documenting them.

## Output

Provide complete implementation with:

**Project Structure**: Full file organization (/components, /hooks, /utils, /types) with contents

**Core Components**: TypeScript components with interfaces, prop typing, and error boundaries

**Data Simulation**: Mock generators and WebSocket-style update mechanisms for realistic patterns

**Dashboard Layout**: Main application structure with responsive grid and component hierarchy

**Styling System**: Tailwind classes for dark theme, status colors, animations, glassmorphism effects

**State Management**: Real-time data update and alert management implementation

**Interaction Features**: Click handlers, hover tooltips, keyboard shortcuts, settings controls

**Performance Strategy**: Render optimization, graceful degradation, scalability considerations

Avoid generic templates—create domain-specific monitoring that feels purpose-built for the use case.
```

## 用法 / Usage
- 必填變數 / Variables: {{monitoring-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Academic_Research_Synthesis_Pipeline · Anchor_Fading_Curriculum_Protocol
- 適用 / Use when: The Real-Time Monitoring Dashboard Builder Prompt is a free AI prompt that generates enterprise-grade observab…
