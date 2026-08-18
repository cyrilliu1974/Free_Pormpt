# Sticky Header Implementation Prompt for Front-End

## 簡介

The Sticky Header Implementation Prompt for Front-End is a free AI prompt that generates complete, production-ready sticky navigation code for web developers and UX engineers. This sticky header prompt for ChatGPT, Claude, Gemini, and Grok delivers mobile-first CSS using position: sticky, JavaScript enhancements for scroll detection and class toggling, and accessibility features including ARIA attributes and focus management. It prevents layout shifts, avoids content obstruction, and includes performance optimizations like CSS containment and will-change hints. Developers use it to build navigation systems that shrink on scroll, handle responsive breakpoints, and work across all devices without framework dependencies. Reach for this prompt when you need copy-paste ready code with inline explanations, customizable CSS properties for theming, and guidance on common pitfalls in sticky header implementations. ● Analyzes header structure requirements, scroll trigger points, and visual behavior like shrinking, color transitions, and shadow effects. ● Provides position: sticky CSS solutions with responsive breakpoints, smooth transitions, proper z-index layering, and mobile viewport optimization. ● Includes JavaScript for scroll detection with throttling, fallback support for older browsers, and class-based state management. ● Ensures accessibility with focus management, ARIA attributes, reduced-motion media queries, and keyboard navigation support. ## Prompt

```
## Role
You are an expert front-end developer and UX engineer specializing in navigation systems that balance accessibility, performance, and user experience using modern CSS and JavaScript techniques.

## Task
Create a complete sticky header implementation with step-by-step guidance, production-ready code examples, and best practices. The solution must prevent layout shifts, avoid content obstruction, work across devices, and maintain accessibility standards.

## Context
Website type: {{website-type}}
Header configuration: {{header-config}}

Deliver a mobile-first responsive solution that optimizes vertical space, uses position: sticky as the primary technique with JavaScript enhancement where needed, and incorporates smooth transitions, proper z-index layering, and performance optimization.

## Output
Structure your response with:

1. **Requirements Analysis** – confirm header structure, trigger point, and visual behavior (shrinking, color shifts, shadows)
2. **CSS Implementation** – complete position: sticky solution with responsive breakpoints and transition effects
3. **JavaScript Enhancement** – scroll detection, class toggling, and fallback support with performance throttling
4. **Accessibility** – focus management, ARIA attributes, reduced-motion preferences
5. **Mobile Optimization** – vertical space efficiency, touch interaction, viewport considerations
6. **Performance** – CSS containment, will-change hints, layout shift prevention

Provide copy-paste ready code blocks with inline comments explaining each technique. Include HTML structure, complete CSS with custom properties for easy theming, and vanilla JavaScript (no framework dependencies). Show before/after behavior and common pitfalls to avoid.
```

## 用法 / Usage
- 必填變數 / Variables: {{header-config}}、{{website-type}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Sticky Header Implementation Prompt for Front-End is a free AI prompt that generates complete, production-…
