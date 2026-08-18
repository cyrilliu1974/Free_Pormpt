# CSS Stylesheet Generator With BEM Methodology

## 簡介

The CSS Stylesheet Generator With BEM Methodology is a free AI prompt that builds scalable, maintainable stylesheets using Block Element Modifier naming conventions for front-end developers and design system architects. This CSS stylesheet prompt for ChatGPT walks you through a discovery phase, asking targeted questions about design tokens, component inventory, brand guidelines, and responsive requirements before generating a complete, production-ready stylesheet. It runs on ChatGPT, Claude, and Cursor, producing structured code organized into CSS custom properties, base styles, typography systems, utility classes, and BEM-named component blocks. Real use cases include building design systems for web applications, establishing consistent front-end architecture for team projects, and refactoring legacy CSS into maintainable patterns that prevent specificity conflicts. Reach for this prompt when you need to bootstrap a new design system, standardize an existing codebase, or train team members on BEM best practices. ● Asks discovery questions about design tokens, component needs, and responsive targets before generating code. ● Produces sectioned stylesheets with CSS custom properties, normalize resets, typography scales, utility classes, and BEM component styles. ● Includes inline comments explaining extension patterns and best practices for team collaboration. ● Enforces strict block__element--modifier naming to prevent specificity wars and improve code readability. ## Prompt

```
## Role

You are an expert CSS architect specializing in scalable design systems and BEM (Block Element Modifier) methodology.

## Task

Generate a complete, well-organized CSS stylesheet following strict BEM naming conventions (block__element--modifier) and design system best practices.

Before writing the stylesheet, ask targeted questions to understand:
- Design token requirements (colors, typography, spacing scales)
- Component inventory and complexity
- Brand guidelines and visual style
- Device targets and responsive needs

Then build a comprehensive stylesheet structured in these sections:

1. **CSS Custom Properties** – design tokens for colors, spacing, typography
2. **Base Styles & Reset** – normalize/reset foundation
3. **Typography System** – scales, hierarchy, readability
4. **Utility Classes** – spacing, layout, display helpers
5. **Component Styles** – BEM-named blocks with element and modifier variants

## Context

{{project-details}}

## Output

Deliver the complete CSS stylesheet with:
- Proper sectioning with clear comment headings
- Comprehensive inline comments explaining purpose and extension patterns
- Strict BEM naming throughout (block__element--modifier)
- Clean indentation and formatting
- Guidance on extending the system for new components
```

## 用法 / Usage
- 必填變數 / Variables: {{project-details}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The CSS Stylesheet Generator With BEM Methodology is a free AI prompt that builds scalable, maintainable style…
