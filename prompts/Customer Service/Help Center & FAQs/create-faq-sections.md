# Accessible FAQ Section Builder for WCAG Compliance

## 簡介

The Accessible FAQ Section Builder for WCAG Compliance is a free AI prompt that creates fully accessible accordion components for developers and designers who need to balance cognitive load with inclusive design. This accessible FAQ prompt for ChatGPT analyzes your questions, groups them semantically, and outputs production-ready HTML5 and CSS with complete keyboard navigation and screen reader support. Unlike JavaScript-heavy solutions that often break accessibility requirements, it delivers semantic markup using either `<details>`/`<summary>` elements or proper ARIA accordion patterns that function without JavaScript. The prompt works on ChatGPT, Claude, Gemini, and Grok, making it ideal for front-end developers, UX designers, and accessibility specialists building help centers, support pages, or documentation sites that must meet WCAG AA standards. ● Outputs semantic HTML5 with proper heading hierarchy, ARIA labels, and collapsed-by-default sections that reduce information overload ● Includes embedded CSS with visible focus indicators, smooth transitions, and `prefers-reduced-motion` support for vestibular sensitivity ● Provides full keyboard navigation patterns (Tab, Enter, Space, Arrow keys) and screen reader state announcements ● Delivers an implementation guide with testing checklists for keyboard-only users, screen readers, and touch-target sizing ## Prompt

```
## Role
You are an accessibility-focused UI architect specializing in WCAG-compliant progressive disclosure patterns. Your expertise combines cognitive load management with inclusive design, creating interfaces that reduce information overload while remaining fully accessible to screen reader and keyboard users.

## Task
Create a complete, accessible FAQ accordion component that implements progressive disclosure without sacrificing accessibility. Analyze the provided questions to identify natural groupings, then deliver production-ready HTML and CSS with full keyboard navigation and screen reader support.

## Context
The FAQ must solve the dual challenge of preventing cognitive overload (by collapsing content by default) and maintaining WCAG compliance (through semantic markup and robust keyboard/screen reader support). Standard JavaScript-heavy solutions often fail accessibility requirements; pure disclosure widgets or semantic HTML with progressive enhancement are preferred.

## Input
**FAQ content:**
{{faq-content}}

**Interaction mode:**
{{interaction-mode}}

## Requirements

### Structure
- Use semantic HTML5 (`<details>`/`<summary>` or proper ARIA accordion pattern)
- Implement proper heading hierarchy (h2/h3) for questions
- Group into categories using `<nav>` with ARIA labels if more than 10 questions
- All sections collapsed by default

### Accessibility
- Full keyboard navigation: Tab, Enter, Space, Arrow keys
- Screen reader state announcements (expanded/collapsed)
- Focus management with visible focus indicators meeting WCAG AA contrast
- Touch targets minimum 44×44px
- Respect `prefers-reduced-motion` for transitions
- Must function without JavaScript (graceful degradation)

### Visual Design
- Clear state indicators (plus/minus icons) with text alternatives
- Smooth CSS transitions for expand/collapse
- WCAG AA color contrast on all interactive elements
- Calm, non-overwhelming aesthetic

## Output
Provide:

**1. Complete HTML structure**
- Semantic markup with inline code comments explaining accessibility decisions

**2. Embedded CSS**
- Styles for accordion states, transitions, focus indicators, reduced-motion support

**3. Implementation guide**
- Keyboard navigation patterns
- Screen reader behavior
- Testing checklist

Format with clear section headers separating HTML, CSS, and implementation notes.
```

## 用法 / Usage
- 必填變數 / Variables: {{faq-content}}、{{interaction-mode}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Accessible FAQ Section Builder for WCAG Compliance is a free AI prompt that creates fully accessible accor…
