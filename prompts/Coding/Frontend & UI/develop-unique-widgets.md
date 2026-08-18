# React Widget Component Builder Prompt

## 簡介

The React Widget Component Builder Prompt is a free AI prompt that generates complete, production-ready React components with TypeScript, Tailwind CSS, and enterprise-grade architecture for developers and engineering teams. This React widget development prompt for ChatGPT, Claude, Gemini, and Grok transforms high-level requirements into fully functional, self-contained components with comprehensive state management, accessibility compliance, responsive design, and performance optimizations. Whether you need a data visualization dashboard, an interactive form, a real-time notification panel, or a custom UI control, the prompt delivers copy-paste-ready code with documentation, theming systems, and deployment guidance. It analyzes your widget requirements, establishes a design foundation with color schemes and typography, architects the component structure, and outputs complete TypeScript code with ARIA labels, keyboard navigation, dark mode support, smooth animations, and error handling. This prompt is for front-end developers, full-stack engineers, product teams, and startups who need to ship polished, accessible widgets quickly without compromising quality or maintainability. ● Outputs full React + TypeScript components with loading, error, empty, and success state handling built in. ● Includes ARIA labels, keyboard navigation, and screen reader support for WCAG accessibility compliance. ● Applies Tailwind CSS with responsive breakpoints, dark mode theming, and custom animations using CSS transitions. ● Provides usage documentation, implementation examples, customization instructions, and performance optimization strategies. ## Prompt

```
## Role

You are a senior full-stack architect specializing in production-grade React component systems.

## Task

Create a fully functional, production-ready React widget component using TypeScript and Tailwind CSS. The component must work immediately when integrated and rival the quality of products like Linear, Notion, and Stripe.

## Context

{{widget-requirements}}

*Include: purpose and goal, data source or API integration, essential features and functionality, visual style preferences (minimal/modern/colorful/etc.), and target platform (desktop/mobile/both).*

## Output

Deliver a complete, enterprise-grade component with:

**Requirements Analysis**  
Detailed breakdown of widget specifications and technical requirements

**Design Foundation**  
Color scheme, typography, spacing system, and visual hierarchy

**Component Architecture**  
State management strategy and data flow implementation plan

**Complete Component Code**  
Full React + TypeScript component implementing:
- Comprehensive state management (loading, error, empty, success states)
- Full accessibility (ARIA labels, keyboard navigation, screen reader support)
- Responsive design across all device sizes
- Smooth animations and micro-interactions using CSS transitions
- Customizable theming with dark mode support
- Performance optimizations (lazy loading, memoization, efficient re-rendering)
- Proper error handling and validation

**Styling System**  
Tailwind CSS classes and custom CSS for theming, animations, and responsive behavior

**Usage Documentation**  
Implementation guide with code examples, customization options, and setup instructions for any required packages

**Performance Optimizations**  
Production deployment best practices and optimization techniques

Build as a modular, self-contained component that minimizes external dependencies and works immediately when copy-pasted.
```

## 用法 / Usage
- 必填變數 / Variables: {{widget-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The React Widget Component Builder Prompt is a free AI prompt that generates complete, production-ready React …
