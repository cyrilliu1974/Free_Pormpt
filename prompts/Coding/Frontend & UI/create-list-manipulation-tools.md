# List Manipulation Tool Component Builder

## 簡介

The List Manipulation Tool Component Builder is a free AI prompt that generates a complete React TypeScript component with advanced list editing features for frontend developers and full-stack engineers. This list manipulation prompt for ChatGPT produces a single, zero-placeholder component that parses text input, shuffles items using the Fisher-Yates algorithm with staggered animations, enables drag-and-drop reordering via Framer Motion, and provides copy-to-clipboard actions - all wrapped in a glassmorphic design with backdrop blur and micro-interactions. It runs on ChatGPT, Claude, and Cursor, delivering code that includes all imports, types, utility functions, and inline TypeScript comments explaining the implementation. Real use cases include building task organizers, randomizer tools, priority lists, and any interface where users need to reorder, shuffle, or manage collections of items with smooth animations and instant feedback. Reach for this prompt when you need a polished, accessible list component that maintains 60fps performance even with hundreds of items and supports keyboard navigation, ARIA labels, and screen reader compatibility out of the box. ● Centered three-zone layout with debounced input parsing, live item count, and a draggable output area ● True randomization using the Fisher-Yates shuffle enhanced by staggered flutter animations for visual delight ● Framer Motion integration for smooth drag-and-drop reordering with position transitions and visual feedback ● Glassmorphic styling with backdrop blur, responsive breakpoints, and micro-animations that maintain 60fps ## Prompt

```
## Role

You are an expert full-stack developer and UX architect building production-ready web applications with modern React, TypeScript, and animation libraries.

## Task

Create a complete, polished list manipulation tool as a single React component that handles:

- Smart text input parsing with debounced updates and item count display
- Fisher-Yates shuffle algorithm with staggered animations
- Drag-and-drop reordering using Framer Motion with smooth transitions
- Copy to clipboard and clear actions with user feedback
- Glassmorphic UI with backdrop blur, micro-animations, and responsive layout
- Full accessibility: keyboard navigation, ARIA labels, screen reader support
- 60fps performance for lists with hundreds of items

## Context

{{project-requirements}}

## Output

Deliver a complete, zero-placeholder React TypeScript component with:

- Centered layout: input zone, action bar, draggable output zone
- Inline TypeScript comments explaining key logic
- All imports, types, and utility functions included
- Production-ready code that runs flawlessly on first deployment

Provide the full code artifact ready to copy and use.
```

## 用法 / Usage
- 必填變數 / Variables: {{project-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The List Manipulation Tool Component Builder is a free AI prompt that generates a complete React TypeScript co…
