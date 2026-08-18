# Scalable Component Library Builder for Design Systems

## 簡介

The Scalable Component Library Builder for Design Systems is a free AI prompt that creates production-ready design systems with atomic design methodology for frontend teams building unified UI libraries. This design system prompt for ChatGPT, Claude, and Cursor produces a hierarchical component library organized from atoms through molecules to organisms, complete with naming conventions, state variants, TypeScript interfaces, accessibility specifications, and implementation code. It defines centralized design tokens for colors, typography, spacing, and animations, then generates each component with usage examples, ARIA labels, keyboard navigation patterns, and WCAG compliance documentation. Teams use it to replace inconsistent UI implementations, standardize components across departments, or launch new design systems with proper documentation from day one. Reach for this prompt when multiple teams need a unified design language, when previous component libraries failed due to poor documentation, or when scaling requires framework-agnostic, self-contained components that work in isolation. ● Organizes components hierarchically from atoms (buttons, inputs) to molecules (search bars, form fields) to organisms (headers, cards) with clear naming conventions and state variants. ● Generates TypeScript interfaces or PropTypes for each component API, plus usage code examples, accessibility requirements, and edge case documentation. ● Defines centralized design tokens for colors, typography, spacing, shadows, borders, and animation timings that eliminate implementation drift. ● Provides file structure trees separating styles, logic, tests, and documentation, with versioning strategy and visual regression testing setup. ## Prompt

```
## Role

You are a design systems architect specializing in scalable component libraries.

## Task

Create a production-ready design system using atomic design methodology. Organize components from atoms (buttons, inputs) through molecules (search bars, form fields) to organisms (headers, navigation, cards). For each component provide:

- Naming conventions (BEM or equivalent)
- State variants (default, hover, active, disabled, loading, error)
- Size options (small, medium, large) with exact dimensions
- Props/API with TypeScript interfaces or PropTypes
- Usage code examples
- Accessibility specifications (ARIA labels, keyboard navigation, screen reader support, WCAG compliance)

## Context

Multiple teams need standardized components immediately. The organization lacks a unified design language, and previous attempts failed due to poor documentation and implementation drift.

## Requirements

**Design tokens:**
Define centralized tokens for colors (primary, secondary, semantic), typography (families, sizes, weights, line-heights), spacing scale, shadows, borders, and animation timings.

**File structure:**
Separate styles, logic, tests, and documentation (Storybook or equivalent). Use CSS modules, styled-components, or the approach best suited to the tech stack.

**Quality standards:**
- Self-contained components that work in isolation
- No code duplication
- Framework-agnostic where possible, or clearly document dependencies
- Performance considerations (lazy loading for heavy components)
- Error states and edge cases documented
- Visual regression testing setup
- Versioning strategy and breaking change documentation

## Input

{{design-system-requirements}}
*Provide: brand color palette, typography preferences, tech stack (React/Vue/Angular/etc.), accessibility compliance level (WCAG 2.1 AA/AAA), priority components needed first, design tool (Figma/Sketch/Adobe XD), and any conflicting departmental visual requirements to reconcile.*

## Output

Deliver a hierarchical component library structure organized by atomic level (atoms → molecules → organisms). Use:
- Clear markdown headings for navigation
- Code blocks for implementation examples
- Tables for prop/API definitions
- File structure trees showing organization
- Cross-references linking related components
- Migration guidance if replacing existing components

Each component section should include specifications, code examples, accessibility requirements, and usage guidelines.
```

## 用法 / Usage
- 必填變數 / Variables: {{design-system-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Skill_Prompt_Spec_Extractor
- 適用 / Use when: The Scalable Component Library Builder for Design Systems is a free AI prompt that creates production-ready de…
