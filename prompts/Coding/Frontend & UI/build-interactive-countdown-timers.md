# Interactive Countdown Timer Builder

## 簡介

The Interactive Countdown Timer Builder is a free AI prompt that generates production-ready countdown timer web applications with polished UI, smooth animations, and celebration effects for developers and designers. This countdown timer prompt for ChatGPT, Claude, and Cursor produces complete, commented code organized into modular components including live-updating timer cards, input forms, confetti celebrations, and state persistence via LocalStorage. It handles your chosen tech stack (React, TypeScript, Framer Motion, or alternatives), applies your design aesthetic (color schemes, animation styles, visual preferences), and tailors functionality to your specific countdown use cases - whether product launches, event countdowns, or task deadlines. Reach for this prompt when you need a share-worthy timer application that goes beyond utilitarian clocks, delivering mobile-first responsive design with touch-friendly interactions and accessibility built in. ● Outputs modular components for timer display, user input forms, and celebration animations with entrance and exit transitions. ● Includes state management and LocalStorage integration so timers persist across browser sessions. ● Provides mobile-first responsive layouts with ARIA labels, keyboard navigation, and cross-browser compatibility. ● Delivers a complete deployment package with setup instructions, dependency lists, and feature documentation. ## Prompt

```
## Role
You are an expert full-stack developer and product designer specializing in consumer-grade web applications with polished UI, smooth animations, and responsive design.

## Task
Build a production-ready countdown timer web application with delightful animations, celebration effects, and a shareable interface that stands out from generic utilitarian timers.

## Context
Create a solution distinguished by playful aesthetics, buttery-smooth animations, interactive micro-interactions for emotional engagement, mobile-first responsive design, state persistence, and accessibility.

**Requirements to incorporate:**
{{tech-stack}} — frameworks, libraries, and styling approach
{{design-aesthetic}} — color schemes, animation style, and visual preferences
{{countdown-use-cases}} — event types and timer scenarios to support

## Output
Deliver complete, production-ready code organized into:

**Project Architecture & Setup**
- File structure with dependencies and configuration
- Single HTML file or multi-file project as appropriate for the chosen tech stack

**Core Components**
- TimerCard: displays individual countdown with live updates
- CreateTimerForm: user input for new timers
- ConfettiEffect: celebration animation when countdown reaches zero

**Animation & Interaction Systems**
- Smooth transitions and micro-interactions
- Entrance/exit animations for timer cards

**State Management & Data Persistence**
- State handling appropriate to the chosen framework
- LocalStorage integration for timer persistence

**Responsive Design & Styling**
- Mobile-first layout approach
- Touch-friendly interactions

**Performance & Accessibility**
- Cross-browser compatibility
- ARIA labels and keyboard navigation
- Error handling

**Deployment Package**
- Setup instructions
- Feature overview README

Provide complete, commented code blocks for each component. Ensure all code is copy-paste ready for immediate deployment.
```

## 用法 / Usage
- 必填變數 / Variables: {{countdown-use-cases}}、{{design-aesthetic}}、{{tech-stack}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Agent_Runtime_Charter_Design
- 適用 / Use when: The Interactive Countdown Timer Builder is a free AI prompt that generates production-ready countdown timer we…
