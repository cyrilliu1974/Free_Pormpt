# Vocabulary Learning App Builder

## 簡介

The Vocabulary Learning App Builder is a free AI prompt that generates a complete, deployable vocabulary learning web application for developers and educational technologists. This vocabulary learning app prompt for ChatGPT, Claude, and Cursor produces a full React TypeScript codebase implementing the Leitner spaced repetition system, Zustand state management with persistence, Tailwind CSS responsive design, and Framer Motion animations. The prompt delivers integrated components including learning interfaces, review cards, progress dashboards, audio pronunciation support, and PWA configuration. Real use cases include building language learning platforms, creating custom study tools for schools, or launching SaaS vocabulary applications with production-grade architecture. Reach for this prompt when you need a complete, working vocabulary app rather than starting from scratch - it handles the cognitive science, state logic, accessibility, and deployment setup in a single generation. ● Implements the Leitner spaced repetition algorithm with mathematically sound interval calculations for effective vocabulary retention ● Generates Zustand state stores with local persistence, vocabulary management functions, and progress tracking logic ● Includes 50+ sample vocabulary entries with translations, pronunciation guides, and example sentences to demonstrate the data model ● Outputs WCAG 2.1 AA compliant components with keyboard navigation, screen reader support, and audio pronunciation features ## Prompt

```
## Role
You are an expert full-stack developer and educational technology architect specializing in production-ready web applications.

## Task
Build a complete, deployable vocabulary learning web application with spaced repetition (Leitner system), sophisticated state management, and premium UI/UX. Deliver production-ready code with all components integrated and fully functional.

## Context
{{app-requirements}}

Include: target languages to support, design aesthetic preferences (default to Linear.app/Readwise-inspired minimalism if unspecified), deployment platform (Vercel, Netlify, etc.), feature priorities, and target user skill level.

## Technical Stack
- React with TypeScript
- Zustand for state management with persistence
- Tailwind CSS for responsive design
- Framer Motion for animations
- WCAG 2.1 AA compliant accessibility
- Audio integration for pronunciation
- Full PWA configuration
- Code splitting, lazy loading, error boundaries

## Output
Deliver the complete application with:

1. **Project Architecture & TypeScript Interfaces**  
   Type definitions for vocabulary items, user progress, and state

2. **Core Components**  
   Learning interface, review cards, progress dashboard, statistics views

3. **State Management Layer**  
   Zustand stores with persistence, vocabulary management, progress tracking

4. **Spaced Repetition Engine**  
   Leitner algorithm implementation with mathematically sound interval calculations

5. **Sample Data**  
   50+ vocabulary entries with translations, pronunciation guides, and example sentences

6. **Styling & Animation**  
   Responsive layouts, micro-interactions, loading states

7. **Audio & Accessibility**  
   Pronunciation support, keyboard navigation, screen reader optimization

8. **Error Handling & Optimization**  
   Error boundary components, performance monitoring, bundle optimization

9. **Deployment Configuration**  
   Build scripts, environment setup, PWA manifest

Provide fully integrated, production-ready code with comprehensive comments explaining architecture decisions and implementation details.
```

## 用法 / Usage
- 必填變數 / Variables: {{app-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Vocabulary Learning App Builder is a free AI prompt that generates a complete, deployable vocabulary learn…
