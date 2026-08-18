# Design System Style Guide Generator

## 簡介

The Design System Style Guide Generator is a free AI prompt that builds production-ready, interactive style guides for design and engineering teams. This design system prompt for ChatGPT generates a complete single-file React application with embedded Tailwind CSS that serves as living documentation for your brand. It produces an interactive style guide with copy-paste code snippets, live component playgrounds, downloadable design tokens in CSS/JavaScript/JSON formats, and comprehensive integration instructions. The prompt runs on ChatGPT, Claude, and Cursor, taking your brand context - industry, personality, existing assets, and team structure - and outputting a navigable artifact that includes color systems with usage guidelines, typography hierarchies, spacing scales, responsive grid layouts, and a full component library with buttons, inputs, cards, and modals in all interactive states. The generated guide features dark mode, keyboard shortcuts, and WCAG AA accessibility compliance, styled with the polish of professional documentation systems. Designers and developers use this prompt when launching new products, unifying fragmented design systems, or onboarding engineering teams to established brand guidelines. ● Outputs a complete brand foundation with color palettes, typography scales, and spacing systems with hex codes and usage rules ● Generates an interactive component library with live examples, hover states, and copy-paste React code for buttons, forms, and UI elements ● Includes responsive 12-column grid layouts, mobile-first breakpoints, and downloadable design tokens in multiple export formats ● Provides step-by-step integration guides for React, Next.js, and Vite projects with onboarding workflows and maintenance best practices ## Prompt

```
## Role

You are a design systems architect building production-ready style guides that bridge design and engineering with living documentation, interactive components, real code snippets, and clear integration guidance.

## Task

Build a comprehensive, interactive style guide as a single-file React artifact using Tailwind CSS. The guide serves as a single source of truth that eliminates design ambiguity and accelerates development.

## Context

{{brand-context}}

Include: industry/sector, brand personality (modern/classic/playful/professional), existing brand assets (logos, colors, design elements), primary products or applications where the style guide will be used, and team structure (design/development composition).

## Output

Deliver a production-ready, single-file React application with embedded Tailwind styles that includes:

**Brand Foundation**
- Complete color system: primary, secondary, neutral, and semantic colors with hex codes and usage guidelines
- Typography system: font families, sizes, weights, line heights, and usage rules for headers, body text, and UI elements
- Spacing scale: 4px base grid with 8px increments, margin and padding guidelines

**Component Library**

Interactive components with live examples and copy-paste code snippets:
- Buttons (primary/secondary/ghost variants in sm/md/lg sizes with all states: default, hover, active, disabled)
- Input fields, cards, badges, alerts, modals
- Each component shows usage guidelines and implementation code

**Layout Patterns**
- Responsive 12-column grid system
- Mobile/tablet/desktop breakpoints (mobile: 640px, tablet: 768px, desktop: 1024px)
- Common page templates (dashboard, content page, landing page)

**Design Tokens**

Generate downloadable tokens in multiple formats:
- CSS variables
- JavaScript objects
- JSON

**Interactive Features**
- Sidebar navigation structured: Foundation → Components → Patterns → Resources
- Search functionality
- Dark mode toggle
- Keyboard shortcuts (/ for search, Cmd+K for command palette)
- Color pickers and font size previews
- Component playgrounds for live experimentation

**Implementation Guide**

Comprehensive README section with:
- Step-by-step integration instructions for React/Next.js/Vite projects
- Best practices for adopting into existing codebases
- Developer onboarding guidance
- Version control and maintenance workflow

**Technical Requirements**
- Professional styling similar to Stripe documentation or shadcn/ui
- Semantic HTML and modern CSS practices
- Fully responsive design
- WCAG AA accessibility compliance minimum
- Single-file artifact with embedded styles
```

## 用法 / Usage
- 必填變數 / Variables: {{brand-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Design System Style Guide Generator is a free AI prompt that builds production-ready, interactive style gu…
