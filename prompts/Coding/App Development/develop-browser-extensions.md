# Browser Extension Development Prompt

## 簡介

The Browser Extension Development Prompt is a free AI prompt that generates complete, working browser extensions tailored to a specific browser platform and user need. It produces all necessary files - manifest.json, background scripts, content scripts, popup interfaces, and supporting code - optimized for the target browser's native APIs and design language. This browser extension development prompt for ChatGPT, Claude, and Cursor walks through technical architecture, platform-specific API recommendations, permissions justification, UI design that matches the browser's aesthetics, performance optimization, error handling, and a step-by-step installation guide. Use it when you need a focused, single-purpose extension built for Chrome, Firefox, Edge, or Safari that solves a real problem for a defined audience. ● Delivers a complete file tree, manifest configuration, and working JavaScript for background workers, content scripts, and popup UI. ● Tailors API usage and permissions to the specified browser, avoiding generic cross-platform shortcuts that compromise performance. ● Includes error handling for permission denials, network failures, cross-origin restrictions, and edge cases. ● Provides installation steps, a testing checklist, and debugging tips matched to the user's technical level. ## Prompt

```
## Role

You are an expert browser extension architect specializing in production-ready, platform-native extensions.

## Task

Create a complete, working browser extension optimized for {{target-browser}} that solves this problem: {{extension-concept}}.

Deliver all necessary files including manifest.json, background scripts, content scripts, popup interface, and supporting code.

## Context

The target users are {{target-users}} with {{technical-level}} technical expertise.

Build a focused, single-purpose extension that feels native to the browser. Prioritize platform-specific APIs over generic cross-platform compromises. Match the complexity and documentation depth to the stated technical level.

## Output

Structure your response with these sections:

### Extension Scope and Browser-Specific Strategy
- Problem framing and core functionality boundaries
- Platform-specific API recommendations for {{target-browser}}
- Permissions required and their justifications

### Technical Architecture and File Structure
- Complete file tree and organization
- manifest.json configuration with version-specific syntax
- Module relationships and communication flow

### Core Functionality Implementation
- Background/service worker code with inline comments
- Content script implementation
- Message passing and state management
- Actual working code blocks, not pseudocode

### Native UI Design and User Experience
- Popup interface HTML/CSS/JS that matches {{target-browser}} design language
- Options page if needed
- Icon and visual asset specifications
- Keyboard shortcuts and accessibility considerations

### Performance Optimization and Best Practices
- Memory management and efficient DOM operations
- Event listener lifecycle management
- Storage strategy (local, sync, session)

### Edge Case Handling and Error Management
- Permission denial scenarios
- Network failures and timeout handling
- Cross-origin restrictions
- User-facing error messages

### Installation and Testing Guide
- Step-by-step local installation for {{target-browser}}
- Testing checklist for core functionality
- Debugging tips for common issues

Present all code with syntax highlighting markers. Explain architectural decisions specific to {{target-browser}} capabilities.
```

## 用法 / Usage
- 必填變數 / Variables: {{extension-concept}}、{{target-browser}}、{{target-users}}、{{technical-level}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Browser Extension Development Prompt is a free AI prompt that generates complete, working browser extensio…
