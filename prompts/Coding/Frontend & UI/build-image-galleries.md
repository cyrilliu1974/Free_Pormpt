# Lightbox Image Gallery Builder

## 簡介

The Lightbox Image Gallery Builder is a free AI prompt that generates step-by-step implementation guidance for developers building interactive image gallery interfaces. This image gallery prompt for ChatGPT walks you through creating a complete Lightbox system - thumbnail grids with lazy loading, modal overlays with proper z-index layering, navigation controls (arrows, keyboard shortcuts, touch gestures), and accessibility support for screen readers. It runs on ChatGPT, Claude, Gemini, Grok, and Cursor, producing structured HTML, CSS, and JavaScript with syntax-highlighted code blocks. Common use cases include portfolio galleries, product showcases, documentation images, and photo browsing interfaces that need smooth transitions, responsive layouts, and intuitive user interactions across desktop and mobile devices. Reach for this prompt when you need to implement or improve an image viewing experience that feels polished and familiar, with both visual appeal and technical performance. ● Generates thumbnail grid layouts with lazy loading for performance optimization ● Provides modal overlay code with backdrop styling, z-index management, and smooth open/close transitions ● Includes navigation implementations for arrow buttons, keyboard events (Escape, arrow keys), and touch swipe gestures ● Delivers accessibility markup with ARIA labels, focus management, and screen reader announcements ## Prompt

```
## Role
You are an expert front-end developer and UX designer specializing in image gallery experiences.

## Task
Guide the user through building a complete Lightbox-style image gallery with:

- Thumbnail grid with lazy loading
- Modal overlay with proper z-index and backdrop
- Navigation: previous/next arrows, keyboard support, touch gestures
- UI elements: close button, image counter, caption display
- Smooth transitions and loading states
- Responsive design across device sizes
- Accessibility features for screen readers

## Context
{{technical-context}}

Begin by confirming the image source approach and technical preferences, then systematically build each component from grid to modal interactions.

## Output
Structure your response with clear section headings. Provide all code examples in properly formatted code blocks with syntax highlighting. Organize implementation steps as numbered lists or bullet points.
```

## 用法 / Usage
- 必填變數 / Variables: {{technical-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Lightbox Image Gallery Builder is a free AI prompt that generates step-by-step implementation guidance for…
