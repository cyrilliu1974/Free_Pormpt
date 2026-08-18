# CSS Gradient Maker Builder Prompt

## 簡介

The CSS Gradient Maker Builder Prompt is a free AI prompt that generates step-by-step technical guidance for developers building a professional React application to create and export CSS gradients. This CSS gradient maker prompt for ChatGPT, Claude, and Cursor walks you through architecture, state management, interactive UI components, and performance optimization to create a tool with live preview, drag-and-drop color stops, angle controls, and multi-format export (CSS, Tailwind, SVG, PNG). It covers React + TypeScript + Tailwind CSS + Framer Motion setup, custom hooks for gradient state (linear, radial, conic), color picker integration, preset libraries, undo/redo, and 60fps animation techniques. Use it when you need to ship a polished gradient design tool that rivals commercial products. ● Provides complete project architecture: tech stack, folder structure, TypeScript interfaces, and dependency configuration. ● Includes working code for interactive UI components: live canvas preview, draggable color stops, color pickers, and angle/direction controls. ● Covers advanced features like CSS/Tailwind code generation, preset gradient libraries, multi-format export, and undo/redo. ● Delivers React performance patterns (memoization, debouncing, efficient re-renders) to maintain smooth 60fps interactions and canvas rendering. ## Prompt

```
## Role

You are an expert front-end architect and UI/UX specialist building production-ready React applications with modern web technologies.

## Task

Provide comprehensive technical guidance to build a professional-grade CSS Gradient Maker using React and TypeScript. The tool should rival premium design products like Linear.app and Figma with polished UX, real-time preview, smooth animations, and enterprise-level functionality.

## Context

{{developer-context}}

## Output

Structure your response with these sections:

### Project Architecture and Setup
Complete tech stack configuration, folder structure, and dependency setup for React + TypeScript + Tailwind CSS + Framer Motion.

### Core State Management
TypeScript interfaces, custom hooks, and gradient state logic that handles multiple color stops, angle/direction, and gradient types (linear, radial, conic).

### Interactive UI Components
Implementation details for:
● Live gradient canvas with real-time preview
● Color stop controls with drag-and-drop positioning
● Color picker integration
● Angle/direction controls
● Smooth animations and transitions

### Advanced Features
● CSS/Tailwind/inline style code generation
● Preset gradient library
● Export functionality (CSS, SVG, PNG)
● Undo/redo capability

### Performance Optimization
React optimization techniques to maintain 60fps interactions: memoization, debouncing, efficient re-renders, and canvas rendering strategies.

### Polish and UX Details
Micro-interactions, keyboard shortcuts, accessibility (WCAG compliance), responsive design, and premium visual refinements.

### Complete Code Implementation
Full working application with commented code examples for each major component and feature.

Provide detailed code snippets with implementation guidance for each section. Use bullet points (●) to organize subsections and key implementation steps.
```

## 用法 / Usage
- 必填變數 / Variables: {{developer-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The CSS Gradient Maker Builder Prompt is a free AI prompt that generates step-by-step technical guidance for d…
