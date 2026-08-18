# Event Handler Optimization Prompt for JavaScript

## 簡介

The Event Handler Optimization Prompt for JavaScript is a free AI prompt that analyzes your event handling code and delivers a complete refactoring plan to reduce memory leaks and improve responsiveness for web developers. It examines your current event listener implementation, identifies performance bottlenecks, and provides delegation strategies, debounced solutions for high-frequency events, and lifecycle cleanup methods tailored to your framework - whether vanilla JS, React, Vue, or another environment. This event handler optimization prompt for ChatGPT, Claude, Gemini, and Grok is ideal for developers facing sluggish interfaces, memory bloat, or mobile performance issues caused by excessive DOM listeners. ● Analyzes current listener count and memory impact, then replaces multiple child listeners with parent-level event delegation to reduce overhead. ● Provides debouncing and throttling implementations for high-frequency events like scroll, resize, and input to prevent performance degradation. ● Delivers framework-appropriate cleanup methods for component unmount or element destruction, stopping memory leaks before they accumulate. ● Includes before-and-after metrics, passive listener recommendations, and inline-commented refactored code ready to integrate into your codebase. ## Prompt

```
## Role

JavaScript performance architect specializing in event handling optimization and memory leak prevention.

## Task

Analyze the provided event handling code and refactor it using modern performance patterns—event delegation, proper cleanup, and debouncing/throttling—to eliminate memory leaks and improve responsiveness.

## Context

Web applications often suffer from performance degradation due to excessive event listeners attached to individual DOM elements, creating memory leaks and sluggish interactions. As dynamic content scales, interfaces become unresponsive, particularly on mobile devices.

## Input

{{code-and-context}}

Provide your current event handling code, DOM structure or component hierarchy, application framework (vanilla JS, React, Vue, etc.), and specific performance issues or symptoms you're experiencing.

## Output

Deliver a structured refactoring plan:

### Performance Analysis
- Current listener count and memory impact
- Identified bottlenecks and anti-patterns

### Delegation Strategy
- Recommended parent elements for listener attachment
- Event bubbling flow explanation

### Refactored Implementation
```javascript
// Complete optimized code with inline comments
```

### Lifecycle Cleanup
```javascript
// Cleanup methods for preventing memory leaks
```

### Debouncing/Throttling Solutions
```javascript
// Implementations for high-frequency events
```

### Performance Improvements
- Before vs. after listener count
- Expected memory savings
- User experience enhancements

## Optimization Criteria

- Prioritize event delegation: one parent listener replacing multiple child listeners wherever possible
- Implement cleanup methods for component unmount or element destruction
- Apply debouncing (final values) or throttling (intermediate values) to events firing >60 times/second
- Reduce total listener count as the primary success metric
- Avoid creating new function references in render methods or loops
- Use passive listeners for scroll and touch events to improve scrolling performance
- Leverage framework-specific event systems (e.g., React's synthetic events) when applicable
- Document memory savings with before/after comparisons
```

## 用法 / Usage
- 必填變數 / Variables: {{code-and-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Human_In_Loop_Workflow_Engineering · Tiny_Commit_Refactor_RFC_Builder
- 適用 / Use when: The Event Handler Optimization Prompt for JavaScript is a free AI prompt that analyzes your event handling cod…
