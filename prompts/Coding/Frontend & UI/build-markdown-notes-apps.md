# Build Markdown Notes App Prompt for ChatGPT

## 簡介

The Build Markdown Notes App Prompt is a free AI prompt that generates a full implementation guide for developers creating a production-ready, browser-based markdown notes application without any backend dependencies. This markdown notes app prompt for ChatGPT produces a twelve-section architecture and code guide covering HTML5 structure, CSS3 theming, modular JavaScript, extended markdown parsing (tables, code blocks, LaTeX equations), hierarchical organization with tags and categories, search indexing, multi-format export (PDF, HTML, markdown), keyboard shortcuts, auto-save with version history, and localStorage persistence. It runs on ChatGPT, Claude, Gemini, and Grok, tailoring code complexity to your JavaScript skill level and applying your chosen design aesthetic. Reach for this prompt when you need to build a knowledge-management tool that competes with Obsidian or Notion, entirely in vanilla JavaScript with no framework overhead. ● Outputs complete code for split-screen live preview, syntax highlighting, and extended markdown support including tables, code fences, and mathematical equations. ● Provides hierarchical organization with categories, tags, favorites, full-text search, and filtering so users can manage hundreds of notes efficiently. ● Includes auto-save, version history, data recovery, and localStorage implementation with import/export backup to prevent data loss. ● Delivers keyboard shortcuts, dark/light themes, responsive design for desktop and tablet, and multi-format export (PDF, HTML, markdown files) for professional-grade user experience. ## Prompt

```
## Role

You are an expert full-stack web developer and UI/UX architect building production-ready web applications.

## Task

Create a comprehensive implementation guide for a professional-grade markdown notes application that runs entirely in the browser without backend dependencies. This is a complete knowledge management system competing with Obsidian and Notion, featuring real-time rendering, persistent storage, advanced organization, and export capabilities.

## Context

The application must handle complex markdown syntax (tables, code blocks, mathematical equations) while maintaining performance. Users expect desktop-application quality with intuitive workflows, keyboard-driven efficiency, and zero data loss. Balance feature richness with clean, maintainable code architecture.

**Technical specifications:**
- Stack: HTML5, CSS3, vanilla JavaScript with modular ES6 modules and clear separation of concerns
- Target: Modern evergreen browsers (Chrome, Firefox, Safari, Edge) on desktop and tablet
- Delivery: Single-developer build shipped incrementally in working milestones
- User proficiency: {{javascript-skill-level}}
- Design aesthetic: {{design-style}}

## Output

Structure your implementation guide with these sections, providing complete code examples and clear implementation instructions for each:

1. **Application Architecture and File Structure** — overall project organization and module dependencies
2. **HTML5 Semantic Structure with Split-Screen Layout** — document structure and responsive layout foundation
3. **CSS3 Styling System** — dark/light themes, responsive design, syntax highlighting
4. **Core JavaScript Modules** — editor controller, preview renderer, storage manager
5. **Markdown Parser Integration** — extended syntax support for tables, code blocks, math equations
6. **Hierarchical Organization System** — categories, tags, favorites, navigation
7. **Search and Filtering Engine** — content indexing and query implementation
8. **Export Functionality** — PDF, HTML, and markdown file generation
9. **Keyboard Shortcuts and Productivity Features** — efficiency improvements and shortcuts
10. **Auto-Save, Version History, and Data Recovery** — persistence and recovery mechanisms
11. **LocalStorage Implementation** — data storage with import/export backup capability
12. **Performance Optimization and Best Practices** — rendering efficiency, memory management, extensibility

For each section, provide working code examples with implementation instructions in bullet points and plain explanations of how components work together.
```

## 用法 / Usage
- 必填變數 / Variables: {{design-style}}、{{javascript-skill-level}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Build Markdown Notes App Prompt is a free AI prompt that generates a full implementation guide for develop…
