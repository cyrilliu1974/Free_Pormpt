# React Slideshow Component Builder

## 簡介

The React Slideshow Component Builder is a free AI prompt that generates complete, production-ready presentation systems for developers building investor pitches, product demos, educational content, or corporate decks. This slideshow component prompt for ChatGPT, Claude, and Cursor produces a single-file React component with full TypeScript type safety, Tailwind CSS theming, Framer Motion animations, and enterprise features like presenter mode with notes, keyboard shortcuts, touch gestures, localStorage persistence, and print-ready PDF export. The prompt structures output into eight organized sections: TypeScript interfaces, core component logic, 6-8 reusable slide templates (title, split, grid, full-bleed), animation systems, media pipelines with lazy loading, presenter controls, navigation with accessibility compliance, and export functionality. Real-world use cases include building pitch decks for startups, training modules for corporate teams, and portfolio showcases for agencies. Reach for this prompt when you need a maintainable, scalable slideshow system that works across desktop, tablet, and mobile without over-engineering. ● Outputs a complete React component with TypeScript interfaces, Tailwind CSS theming, dark mode, and responsive layouts for all screen sizes. ● Includes Framer Motion transitions, keyboard navigation, touch gestures, fullscreen mode, auto-advance, and ARIA labels for accessibility. ● Provides presenter mode with speaker notes, timer, progress tracking, and audience view toggle for professional delivery. ● Delivers 6-8 reusable slide templates with flexible content slots, media handling with lazy loading, and print styles for PDF export. ## Prompt

```
## Role
You are an expert React developer specialized in building production-grade presentation systems.

## Task
Build a complete, single-file React slideshow component that handles professional presentations across any use case—investor pitches, product demos, educational content, or corporate decks.

## Context
{{presentation-requirements}}

The system must deliver enterprise-grade polish: smooth performance on all devices, flawless navigation, accessibility compliance, and maintainable architecture. Prioritize clean code over complexity.

## Technical Requirements
- **TypeScript**: Full type safety with interfaces for slide data, configuration, and props
- **Styling**: Tailwind CSS with CSS variables for theming; dark mode default with high-contrast accessibility; print media queries for PDF export
- **Animations**: Framer Motion for transitions and interactive states with precise timing
- **Responsiveness**: Desktop, tablet, and mobile support with adaptive layouts
- **Navigation**: Keyboard shortcuts, touch gestures, progress indicators, fullscreen mode, auto-advance
- **Advanced Features**: Presenter mode with notes, timer, localStorage persistence, theme customization
- **Performance**: Lazy loading for media, error boundaries, loading states, optimized rendering

## Output
Deliver a production-ready React component organized into these sections:

### 1. TypeScript Interfaces
Define slide data structure, configuration options, component props, and theme schema

### 2. Core Slideshow Component
Main component with state management, navigation logic, and event handlers that accepts `slideData` prop

### 3. Template Library
6-8 reusable slide layouts (title, content, split, full-bleed, grid, etc.) with flexible content slots and responsive behavior

### 4. Animation System
Framer Motion transitions between slides, enter/exit animations, loading states, and gesture handlers

### 5. Media Pipeline
Image and video handling with lazy loading, fallbacks, aspect ratio preservation, and performance optimization

### 6. Presenter Controls
Presenter view mode, speaker notes display, timer/progress tracking, audience mode toggle

### 7. Navigation & Accessibility
Keyboard shortcuts (arrows, space, ESC), touch/swipe gestures, focus management, ARIA labels, progress indicators

### 8. Export & Persistence
LocalStorage for state persistence, theme switching, guidance for PDF export via print styles

Focus on Linear.app-style minimalism: clean composition, intentional whitespace, typography hierarchy, and professional polish. Avoid over-engineering—prioritize maintainability and reliability.
```

## 用法 / Usage
- 必填變數 / Variables: {{presentation-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The React Slideshow Component Builder is a free AI prompt that generates complete, production-ready presentati…
