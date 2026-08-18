# Task Priority Ranker Builder

## 簡介

The Task Priority Ranker Builder is a free AI prompt that generates a production-ready task management application for developers and product teams who need intelligent priority scoring systems. This task priority ranker prompt for ChatGPT produces a complete single-file React TypeScript component with a weighted scoring engine that calculates task priority using impact, urgency, effort, and dependency factors. The generated application includes color-coded priority displays, auto-sorting with smooth animations, visual task groupings ("Do Now," "Do Today," "Schedule Later"), and customizable weight sliders with preset modes like "Deadline Driven" and "Quick Wins." It runs on ChatGPT, Claude, and Cursor, delivering code styled with Tailwind CSS and Framer Motion that works immediately in any React environment. Use it when building productivity tools, prototyping task management features, or creating decision-support interfaces that help users cut through competing priorities. ● Implements a weighted scoring formula combining impact ratings, deadline urgency multipliers, effort costs, and dependency bonuses for objective task ranking ● Includes customizable weight sliders, three preset prioritization modes, and real-time recalculation as users adjust parameters ● Generates keyboard shortcuts, swipe-to-complete mobile gestures, one-click task completion, and LocalStorage persistence ● Delivers production-ready code with inline comments explaining the scoring algorithm and interaction patterns, requiring zero additional configuration ## Prompt

```
## Role

You are an expert product engineer specializing in intelligent productivity systems.

## Task

Build a complete, production-ready Task Priority Ranker application as a single-file React TypeScript artifact.

## Requirements

**Core Functionality**
- Task input with name, deadline, impact (1-10 slider), effort (1-10 slider), and dependency tags
- Intelligent scoring engine using: `(Impact × Urgency Weight) - (Effort × 0.3) + Dependency Bonus`
- Urgency weights: Due today = 10×, This week = 5×, This month = 2×, Later = 1×
- Auto-sorted display with color-coded priorities (red/orange/yellow/green) and smooth reorder animations
- Visual groupings: "Do Now" (top 3), "Do Today" (next 5), "Schedule Later" (rest)
- Customization panel with adjustable weight sliders and preset modes ("Deadline Driven", "Impact Focused", "Quick Wins")

**User Experience Features**
- {{ux-features}}
- One-click task completion
- Keyboard shortcuts (n = new task, 1-9 = quick actions, x = complete)
- Swipe-to-complete on mobile
- LocalStorage persistence
- Mobile responsive design

**Technical Stack**
- React 18+ with TypeScript
- Tailwind CSS for styling
- Framer Motion for animations
- Zero configuration required—immediately functional

## Output

Provide clean, well-commented code as a complete single-file React component. Include inline explanations for the scoring algorithm and key interaction patterns. The application must work immediately when copied into a React environment.
```

## 用法 / Usage
- 必填變數 / Variables: {{ux-features}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Task Priority Ranker Builder is a free AI prompt that generates a production-ready task management applica…
