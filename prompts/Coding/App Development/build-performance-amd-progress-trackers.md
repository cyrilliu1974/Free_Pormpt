# Build Performance and Progress Trackers

## 簡介

The Build Performance and Progress Trackers is a free AI prompt that generates a full-stack goal-tracking web application for developers building engagement-focused productivity tools. This performance tracker prompt for ChatGPT produces a React + TypeScript codebase with data visualization, milestone celebrations, and intelligent feedback loops that adapt to user momentum. It runs on ChatGPT, Claude, and Cursor, delivering organized component files ready for deployment with no backend required - all persistence uses window.localStorage and JSON export. Reach for this prompt when you need a complete tracking system that goes beyond static to-do lists, supporting multiple concurrent goals with pace projections and psychological engagement patterns baked into the UX. ● Produces ten organized components including goal setup forms with TypeScript interfaces, calculation engines for pace analysis and projections, dashboard layouts with Recharts visualizations, quick-update modals, and adaptive insight generators. ● Implements a Linear.app-inspired minimal design using Tailwind CSS with muted blue color schemes, smooth animations for progress updates, and mobile-first touch-optimized layouts. ● Includes detailed inline comments explaining UX decisions and logic patterns, example data for realistic testing, and complete localStorage integration with JSON export capabilities. ● Generates adaptive motivational messages from performance patterns, auto-celebrates milestones, and adjusts feedback tone based on user momentum and trend analysis. ## Prompt

```
## Role

You are an expert full-stack developer specializing in goal-tracking systems with data visualization and engagement-focused UI design.

## Task

Build a complete dynamic progress tracker as a React + TypeScript web app with localStorage persistence.

## Requirements

**Core Functionality:**
- Support multiple simultaneous goals through flexible data models
- Auto-generate dashboards showing current progress, milestones, trend analysis, and pace projections
- Real-time calculations and JSON data export
- Motivational elements that adapt to user momentum and performance patterns
- All persistence via window.localStorage (no backend)

**Technical Stack:**
- React + TypeScript with proper interfaces and type safety
- Tailwind CSS for Linear.app-inspired minimal design
- Recharts for data visualization with muted blue color schemes
- Mobile-responsive, touch-optimized layout
- Smooth animations for progress updates and milestone celebrations

**Code Quality:**
- Proper separation of concerns with reusable components
- Detailed inline comments explaining logic and UX decisions
- Performance optimization throughout
- Example data and realistic testing scenarios included

## Context

{{goal-configuration}}

## Output

Provide complete, production-ready code organized by component:

1. **Goal Setup Component** – Form with validation and TypeScript interfaces
2. **Calculation Engine** – Core logic for progress calculations, pace analysis, projection algorithms
3. **Dashboard Layout** – Main component with progress visualization and metric cards
4. **Quick Update Modal** – Rapid logging interface with timestamp tracking
5. **Insight Generator** – Algorithm producing adaptive motivational messages from performance patterns
6. **Data Visualization** – Recharts implementation for trend graphs and progress charts
7. **Styling System** – Tailwind classes and custom styles for minimal aesthetic
8. **localStorage Integration** – Complete persistence with JSON export functionality
9. **Responsive Design** – Mobile-first layout working perfectly across all devices
10. **Animation System** – Smooth transitions, milestone celebrations, loading states

Include step-by-step implementation guidance for each major feature.
```

## 用法 / Usage
- 必填變數 / Variables: {{goal-configuration}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Academic_Research_Synthesis_Pipeline · Anchor_Fading_Curriculum_Protocol
- 適用 / Use when: The Build Performance and Progress Trackers is a free AI prompt that generates a full-stack goal-tracking web …
