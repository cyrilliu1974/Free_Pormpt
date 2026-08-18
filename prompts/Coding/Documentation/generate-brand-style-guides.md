# Tailwind CSS Brand Style Guide Generator

## 簡介

The Tailwind CSS Brand Style Guide Generator is a free AI prompt that produces a complete, actionable style guide with utility classes, pixel values, and implementation patterns for developers working with Tailwind CSS. This brand style guide prompt for ChatGPT takes your project name, design direction, target audience, and existing brand assets and returns a structured document covering colors (hex values and Tailwind classes like bg-blue-600), typography scales, spacing systems, component patterns, shadows, animations, border radius, opacity, and a fully coded example component. It runs on ChatGPT, Claude, Gemini, and Grok, and is designed for teams that need a utility-first design system developers can follow without constant designer oversight. The prompt outputs specific class combinations, responsive patterns, and configuration recommendations that prevent implementation drift and miscommunication between design and engineering. Use this prompt when you need a Tailwind-specific style guide that bridges design intent and front-end code, especially for new developers onboarding to a project or teams maintaining visual consistency across multiple contributors. ● Outputs a complete color palette with hex values, Tailwind class names, and usage contexts for primary, secondary, neutral, semantic, and accent colors. ● Defines typography with font families, size scales, weights, line heights, and Tailwind classes for headings, body text, UI elements, and captions. ● Specifies spacing, shadows, border radius, opacity, and animation systems with exact pixel values and corresponding Tailwind utilities. ● Includes a fully implemented example component with complete class reference demonstrating how multiple style guide elements combine in real code. ## Prompt

```
## Role

You are a design systems architect who builds Tailwind CSS-based style guides that bridge the gap between design intent and developer implementation. Your documentation is specific, actionable, and maintained without constant designer oversight.

## Task

Generate a comprehensive style guide with concrete values, Tailwind CSS utility classes, and implementation patterns. Each section must include specific measurements, class names, and usage guidelines—no abstract descriptions. Provide a complete example component that demonstrates multiple style elements working together.

## Context

**Project:** {{project-name}}

**Design direction:** {{design-direction}}

**Target audience and platform:** {{target-audience-and-platform}}

**Existing brand assets:** {{existing-brand-assets}}

The guide must enable new developers to maintain visual consistency without direct designer supervision. Focus on utility-first patterns that prevent the miscommunication and implementation drift that plague traditional design systems.

## Output

Structure your style guide with these sections:

**Overview**
Brief philosophy and usage guidelines for the system.

**Color Palette**
Primary, secondary, neutral, semantic, and accent colors with hex values, Tailwind classes (e.g., `bg-blue-600`, `text-gray-800`), and usage contexts.

**Typography**
Font families, size scale, weight system, line heights, letter spacing, and Tailwind typography classes. Specify usage for headings (h1-h6), body text, UI elements, and captions.

**Spacing System**
Spacing scale with pixel values and Tailwind utilities (`m-4`, `p-6`, `gap-8`). Include margin, padding, and gap patterns.

**Component Styles**
Buttons, form elements, cards, and other common components with specific class combinations and variants (primary, secondary, disabled states).

**Shadows & Elevation**
Shadow system with Tailwind classes (`shadow-sm`, `shadow-lg`, `shadow-2xl`) and elevation hierarchy for layering.

**Animations & Transitions**
Transition timing, duration values, and Tailwind classes (`transition-all`, `duration-200`, `ease-in-out`) for hover states and micro-interactions.

**Border Radius**
Radius scale with pixel values and Tailwind utilities (`rounded`, `rounded-lg`, `rounded-full`) for different component types.

**Opacity & Transparency**
Opacity scale and Tailwind classes (`opacity-50`, `bg-opacity-80`) for layering, disabled states, and hierarchy.

**Tailwind Patterns**
Common utility combinations, responsive patterns, and configuration recommendations specific to this system.

**Example Component**
Complete implementation of one component (card, form, navigation item) with full Tailwind class reference demonstrating how multiple style guide elements combine.

---

Write concisely. Use simple words and short sentences (Gunning Fog index 8). Avoid adjectives and adverbs unless necessary. Do not include a closing paragraph. Provide specific values and code, not generic design advice.
```

## 用法 / Usage
- 必填變數 / Variables: {{design-direction}}、{{existing-brand-assets}}、{{project-name}}、{{target-audience-and-platform}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Tailwind CSS Brand Style Guide Generator is a free AI prompt that produces a complete, actionable style gu…
