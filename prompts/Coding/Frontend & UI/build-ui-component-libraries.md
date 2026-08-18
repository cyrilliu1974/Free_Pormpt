# UI Component Library Builder Prompt for ChatGPT

## 簡介

The UI Component Library Builder Prompt for ChatGPT is a free AI prompt that generates production-ready design systems with tokens, components, and documentation for frontend teams building scalable interfaces. This UI component library prompt for ChatGPT walks through your project requirements - CSS framework choice (Tailwind, ShadCN, custom), design style, use case, brand colors, and device priorities - then outputs a structured component library with foundational design tokens (color palettes, typography scales, spacing systems), component variations (buttons, inputs, checkboxes with state logic), and accessibility-compliant code snippets. It runs on ChatGPT, Claude, and Cursor, delivering organized CSS or framework code that developers can integrate directly into web apps, dashboards, marketing sites, or e-commerce platforms. Teams reach for it when they need a consistent design language across products without starting from scratch or accumulating technical debt. ● Outputs color palettes with semantic naming, typography scales, and spacing systems based on 4px or 8px grids. ● Generates button, input, checkbox, and radio components with hover, active, disabled, focus, error, and success states in three sizes. ● Includes WCAG 2.1 AA accessibility annotations (contrast ratios, focus indicators, semantic markup) and composability rules to prevent style conflicts. ● Provides setup steps, file structure recommendations, and framework integration guidance tailored to your specified CSS system. ## Prompt

```
## Role
You are a design systems architect who builds production-ready UI component libraries that scale across products and teams.

## Task
Generate a complete, systematic UI kit with design tokens, component library, and implementation guidelines.

## Context
{{project-requirements}}

Include:
- CSS framework (ShadCN, Tailwind, custom CSS, or other)
- Design style preference (modern, minimal, bold, classic, etc.)
- Primary use case (web app, marketing site, dashboard, e-commerce, etc.)
- Brand colors if specific (otherwise use a professional default palette)
- Target device priorities (desktop, mobile, tablet)

## Requirements
- Create foundational design tokens: color palettes with semantic naming, typography scales, spacing systems (4px or 8px base), sizing scales
- Build component variations: buttons (primary, secondary, ghost, danger) with hover/active/disabled states and three sizes; input fields (text, select, checkbox, radio) with focus/error/success states
- Use systematic naming conventions and hierarchical organization from tokens → components → patterns
- Ensure responsive behavior and WCAG 2.1 AA accessibility (contrast ratios, focus indicators, semantic markup)
- Emphasize composability: components should combine cleanly without conflicts
- Avoid over-engineering: favor simplicity and maintainability over exhaustive edge-case coverage

## Output
Structure your response with these sections:

### Design Tokens
Color system (primary, secondary, neutral, semantic), typography scale, spacing/sizing tokens

### Button Components
Variants, states, sizes with code snippets

### Typography System
Heading hierarchy (h1-h6), body text, utilities (lead, small, muted)

### Input Components
Text inputs, selects, checkboxes, radios with validation states and code examples

### Spacing Utilities
Margin, padding, gap tokens with consistent scale

### Component Documentation
Usage guidelines, do's and don'ts, accessibility notes

### Implementation Guide
Setup steps, integration with {{project-requirements}} framework, file structure recommendations
```

## 用法 / Usage
- 必填變數 / Variables: {{project-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Prompt&Manifest_Engineering · Manifest_Driven_Code_Skeleton_Generator
- 適用 / Use when: The UI Component Library Builder Prompt for ChatGPT is a free AI prompt that generates production-ready design…
