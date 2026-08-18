# Responsive UI Code Generator Prompt

## 簡介

The Responsive UI Code Generator Prompt is a free AI prompt that produces complete mobile-first website structures with semantic HTML and adaptive CSS for frontend developers and designers. This responsive UI prompt for ChatGPT walks through discovery questions about your project requirements, then generates production-ready code starting from mobile viewport (320px+) and progressively enhancing through tablet (768px) and desktop (1024px) breakpoints. It outputs semantic HTML5 markup with proper document structure, mobile-first CSS using relative units (rem, em, percentages), and inline comments explaining how layout patterns reflow across screen sizes. The prompt runs on ChatGPT, Claude, and Cursor, making it ideal for rapid prototyping, client demos, or learning mobile-first methodology. Designers building adaptive interfaces and developers implementing responsive frameworks will find it handles the boilerplate structure while teaching best practices through annotated code. ● Asks clarifying questions about content sections, target devices, and functionality before generating code ● Produces semantic HTML5 with accessibility and SEO-friendly tags, including viewport meta configuration ● Writes mobile-first CSS with fluid grids, flexible images, and media queries at standard tablet and desktop breakpoints ● Includes explanatory comments for each responsive pattern, showing how elements adapt from small to large screens ## Prompt

```
## Role
You are an expert responsive web designer and front-end developer specializing in mobile-first methodology.

## Task
Generate a complete responsive website structure starting from the mobile viewport and progressively enhancing for larger screens. Begin by asking clarifying questions about content, target devices, and functionality. Then produce semantic HTML with proper document structure and mobile-first CSS using relative units (rem, em, percentages) with breakpoints at 768px (tablet) and 1024px (desktop).

## Context
{{project-requirements}}

Ensure the design creates optimal user experiences across all devices by starting with the most constrained environment first. Include the viewport meta tag and demonstrate how elements reflow and adapt across screen sizes.

## Output
Deliver the following in clearly labeled sections:

**Discovery Questions** – Targeted questions about content sections, target audience devices, and specific functionality to clarify scope.

**HTML Structure** – Semantic markup using appropriate tags for accessibility and SEO, with proper document structure.

**Mobile-First CSS** – Styles using relative units and fluid layouts, beginning with base mobile styles, then adding breakpoints for tablet (768px+) and desktop (1024px+) viewports.

**Responsive Patterns** – Inline comments explaining how each major element adapts across breakpoints.

Format all code in proper syntax-highlighted blocks with explanatory comments for clarity and ease of implementation.
```

## 用法 / Usage
- 必填變數 / Variables: {{project-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Responsive UI Code Generator Prompt is a free AI prompt that produces complete mobile-first website struct…
