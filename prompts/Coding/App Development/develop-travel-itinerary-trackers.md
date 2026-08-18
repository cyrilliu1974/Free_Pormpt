# Travel Itinerary Tracker App Development Prompt

## 簡介

The Travel Itinerary Tracker App Development Prompt is a free AI prompt that delivers a full-stack React + TypeScript travel itinerary application with complete code, architecture design, and deployment strategy for developers building travel management tools. This travel app development prompt for ChatGPT, Claude, and Cursor produces a comprehensive development plan covering TypeScript interfaces, state management, offline functionality with service workers, and real-time progress tracking. You receive copy-paste-ready code examples for components, API layers, IndexedDB persistence, and testing strategies using Vitest and Playwright. The output includes UI framework integration with shadcn/ui and Tailwind CSS, accessibility patterns, and performance optimization techniques like code splitting and lazy loading. Real-world deployment considerations cover CI/CD pipelines, hosting options, and online-offline sync mechanisms tailored to traveler behavior. This prompt is for full-stack developers and technical teams building travel management applications who need production-ready code with modern web architecture, not just theoretical guidance. ● Delivers complete TypeScript interfaces, component hierarchies, and state management patterns with Context API, Zustand, or Redux options ● Provides service worker implementation with Workbox for offline functionality and IndexedDB strategies for complex data persistence ● Includes testing setup across unit (Vitest), integration (React Testing Library), and end-to-end (Playwright) layers with example test cases ● Supplies performance optimization techniques, build pipelines with Vite, and deployment configurations for production environments ## Prompt

```
## Role
You are an expert full-stack developer and travel app architect.

## Task
Create a complete React + TypeScript travel itinerary tracking application with enterprise-grade UI, offline functionality, and intelligent progress tracking. Deliver a comprehensive, step-by-step development plan with complete code examples, file structures, and implementation details covering the full application lifecycle.

## Context
The application must handle:
- Modern web architecture with TypeScript interfaces
- User experience informed by traveler psychology
- Code quality and performance optimization
- Real-world deployment considerations

{{project-requirements}}

## Output
Structure your development plan with these sections:

### Architecture and Data Structure Design
- TypeScript interfaces and data models
- State management approach (Context API, Zustand, or Redux)
- API and service layer design

### Core Component Development Strategy
- Component hierarchy and organization
- Reusable component library
- Props and typing patterns

### User Interface and Experience Implementation
- UI framework integration (shadcn/ui + Tailwind CSS)
- Responsive design patterns
- Accessibility considerations (ARIA labels, keyboard navigation)

### Smart Features and Real-time Tracking
- Progress tracking logic and status management
- Real-time updates and notifications
- Adaptive features based on traveler behavior

### Offline Functionality and Data Persistence
- Service worker implementation with Workbox
- Local storage strategy (IndexedDB for complex data, localStorage for settings)
- Sync mechanisms for online/offline transitions

### Testing, Optimization, and Deployment
- Testing strategy: Vitest for unit tests, React Testing Library for integration, Playwright for e2e
- Performance optimization: code splitting, lazy loading, bundle analysis
- Build and deployment pipeline (Vite build, CI/CD setup, hosting options)

Provide complete, copy-paste-ready code examples for each section with explanatory comments.
```

## 用法 / Usage
- 必填變數 / Variables: {{project-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Skill_Prompt_Spec_Extractor
- 適用 / Use when: The Travel Itinerary Tracker App Development Prompt is a free AI prompt that delivers a full-stack React + Typ…
