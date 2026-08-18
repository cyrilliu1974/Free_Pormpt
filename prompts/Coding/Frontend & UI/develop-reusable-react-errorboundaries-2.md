# React ErrorBoundary Component Generator

## 簡介

The React ErrorBoundary Component Generator is a free AI prompt that creates comprehensive error handling solutions for React developers building resilient frontend applications. This React error boundary prompt for ChatGPT produces a complete TypeScript-enabled ErrorBoundary component with configurable fallback UI, error logging service integration (Sentry, LogRocket, etc.), and intelligent reset mechanisms that prevent component failures from cascading through your application tree. It runs on ChatGPT, Claude, Cursor, and other code-generation models, delivering reusable components with proper typing, accessibility support, and implementation patterns for routes, forms, lazy-loaded sections, and data-fetching layers. The output includes fallback UI designs for different error contexts, retry logic for recoverable failures, testing strategies for both unit and integration scenarios, and handling for edge cases like async errors, event handler failures, and hydration mismatches. Reach for this prompt when you need fault-tolerant React architecture that gracefully degrades instead of crashing, whether you're building a B2B SaaS dashboard, e-commerce checkout flow, or any application where stability and user experience cannot be compromised. ● Produces a fully-typed ErrorBoundary component with hooks, functional patterns, and granular boundary placement strategies ● Includes error logging integration code that captures component stack traces, user context, and actionable metadata ● Provides fallback UI components with accessibility features, retry buttons, and state preservation logic ● Delivers testing approaches that simulate rendering errors, async failures, and boundary reset behavior ## Prompt

```
## Role
You are a senior React architect specializing in resilient frontend systems. You build production-grade error boundaries that prevent component failures from cascading through application trees, ensuring graceful degradation instead of total crashes.

## Task
Create a comprehensive, production-ready React error handling solution centered on a reusable ErrorBoundary component with TypeScript support, flexible fallback UI, error logging integration, and reset functionality.

## Context
Application: {{app-context}}
*Describe your application type, scale, and critical user flows (e.g., "B2B SaaS dashboard serving 50k daily users, checkout flow cannot fail")*

Technical stack: {{tech-stack}}
*Specify UI framework, error logging service, and TypeScript requirement (e.g., "Material-UI, Sentry integration, TypeScript required")*

Error recovery needs: {{recovery-requirements}}
*Describe your preferred reset strategy and any custom recovery logic (e.g., "automatic retry for API errors, manual reset for rendering errors, preserve form state")*

## Requirements
- Build a reusable ErrorBoundary component with configurable fallback UI and reset capabilities
- Integrate error logging with proper context and metadata capture
- Use modern React patterns: hooks, functional components where applicable, proper typing
- Provide fallback UI components for different error scenarios with accessibility support
- Include retry mechanisms, contextual error handling, and granular boundaries
- Demonstrate implementation patterns for different application sections: routes, forms, data fetching
- Supply testing strategies for error boundary behavior
- Handle edge cases: async errors, event handler failures, hydration mismatches

## Output
Deliver in this structure:

**ErrorBoundary Component**
Complete, production-ready implementation with all core features and configuration options

**Fallback UI Components**
Reusable fallback designs for different error types and contexts

**Error Logging Integration**
Service integration code with proper error enrichment and reporting

**Usage Examples**
Implementation patterns for routes, lazy-loaded components, forms, and critical sections

**Advanced Features**
Retry logic, error recovery strategies, contextual handling, and performance considerations

**Testing Strategy**
Unit and integration tests covering error boundary behavior and edge cases

**Implementation Guide**
Step-by-step integration instructions with architectural best practices
```

## 用法 / Usage
- 必填變數 / Variables: {{app-context}}、{{recovery-requirements}}、{{tech-stack}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Context_Audit&Triage
- 適用 / Use when: The React ErrorBoundary Component Generator is a free AI prompt that creates comprehensive error handling solu…
