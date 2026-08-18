# Notion Widget Builder Prompt for ChatGPT and Claude

## 簡介

The Notion Widget Builder is a free AI prompt that generates complete, production-ready Notion widgets with full-stack code for developers building embedded tools. This Notion widget prompt for ChatGPT, Claude, and Cursor takes your widget specification and produces React 18+ components with TypeScript, Tailwind CSS, iframe integration logic, and deployment configurations that work immediately when embedded in Notion pages. It handles responsive scaling across 1-3 column layouts, light/dark mode theming with Notion's color palette, localStorage persistence, and cross-origin messaging constraints. Reach for this prompt when you need to build custom Notion widgets - timers, calculators, dashboards, habit trackers, or any interactive tool - and want architecture guidance, complete source code, and embedding instructions in one response. ● Outputs complete React/TypeScript components with Tailwind CSS, keeping bundle size under 100KB and render time under 500ms for fast loading inside Notion iframes. ● Includes iframe communication patterns, responsive design for desktop and mobile Notion layouts, and WCAG accessibility compliance with error handling. ● Generates package.json, Tailwind config, build scripts, and deployment instructions for Vercel, Netlify, or your preferred hosting platform. ● Provides testing checklists covering cross-browser compatibility, light/dark mode validation, and multi-device responsiveness to ensure widgets work reliably in production. ## Prompt

```
## Role

You are an expert full-stack developer specializing in Notion-embedded widgets with deep knowledge of iframe constraints, cross-origin messaging, responsive scaling, and performance optimization.

## Task

Create a complete, production-ready Notion widget that integrates seamlessly into Notion's ecosystem and works immediately when deployed and embedded.

## Context

{{widget-specification}}

Include: widget purpose and functionality, target users and needs, must-have vs. nice-to-have features, technical stack preferences or constraints, and preferred hosting platform (Vercel, Netlify, etc.).

## Technical Requirements

- React 18+ with TypeScript and Tailwind CSS
- Bundle size under 100KB with sub-500ms render time
- Notion color palette integration with light/dark mode support
- Responsive design optimized for 1-3 column Notion layouts
- LocalStorage persistence with export/import functionality
- Production-ready error handling and WCAG accessibility standards

## Output

Deliver a structured response with these sections:

### Requirements Analysis & Architecture Plan
Break down the specifications and propose the technical architecture.

### Component Structure & UI Design System
Define component hierarchy and design tokens aligned with Notion's visual language.

### Core Functionality Implementation
Provide complete React/TypeScript components with full logic.

### Notion Integration & Performance Optimization
Implement iframe communication, responsive behavior, and performance patterns.

### Complete Code Artifacts
Include all files: components, Tailwind config, package.json, and build configuration.

### Testing & Cross-Environment Validation
Provide testing checklist covering desktop/mobile, light/dark modes, and cross-browser compatibility.

### Deployment Guide & Notion Embedding Instructions
Step-by-step deployment process and embedding instructions with iframe configuration.

### Documentation & Enhancement Recommendations
Usage documentation, maintenance notes, and suggested future enhancements.
```

## 用法 / Usage
- 必填變數 / Variables: {{widget-specification}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Skill_Prompt_Spec_Extractor
- 適用 / Use when: The Notion Widget Builder is a free AI prompt that generates complete, production-ready Notion widgets with fu…
