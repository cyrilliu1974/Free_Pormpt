# WCAG-Compliant Dark Mode Implementation Prompt

## 簡介

The WCAG-Compliant Dark Mode Implementation Prompt is a free AI prompt that generates accessible dual-theme systems for frontend developers and UI engineers facing legal accessibility requirements. This dark mode prompt for ChatGPT, Claude, and Cursor produces production-ready CSS custom properties, theme toggle code, color adaptation strategies, and testing checklists that satisfy WCAG 2.1 AA contrast ratios. It adapts brand colors mathematically for dark backgrounds, implements localStorage persistence with system preference detection, and respects motion reduction settings. Real-world applications include SaaS dashboards requiring ADA compliance, e-commerce sites serving diverse user bases, and content platforms where readability across lighting conditions is critical. Reach for this prompt when retrofitting existing projects with compliant dark modes or architecting new theming systems that must pass accessibility audits and serve users with photosensitivity or visual impairments. ● Defines CSS custom property architectures with 4.5:1 contrast ratios for normal text and 3:1 for large text and interactive elements in both light and dark themes. ● Generates theme toggle code with localStorage persistence, prefers-color-scheme detection, and transitions that respect prefers-reduced-motion settings. ● Produces color mapping tables showing original brand colors, dark mode equivalents, calculated contrast ratios, and WCAG compliance status for every pairing. ● Includes testing checklists referencing axe DevTools and WAVE, troubleshooting guides for common failures like halation from pure black backgrounds, and focus state management patterns. ## Prompt

```
## Role
You are an accessibility-first frontend architect specializing in WCAG 2.1-compliant theming systems.

## Task
Design and implement a dual-theme (light/dark) system that meets WCAG 2.1 AA contrast requirements and respects user preferences. Provide production-ready code, testing protocols, and a color adaptation strategy.

## Context
The application currently lacks compliant dark mode support. Previous attempts caused accessibility violations and readability complaints. The solution must satisfy legal accessibility requirements and integrate with:

{{project-setup}}

*Include: brand color palette (hex/RGB), current CSS framework or styling approach, target browser support, user demographics and accessibility needs, and preference detection strategy (system automatic/manual toggle/both).*

## Implementation Requirements

### Contrast Standards
- Normal text: minimum 4.5:1 contrast ratio in both themes
- Large text (18pt+ or 14pt+ bold): minimum 3:1 contrast ratio
- Interactive elements: distinct focus states with 3:1 contrast against adjacent colors
- Non-text UI components: 3:1 minimum contrast

### Technical Constraints
- Use CSS custom properties for theming architecture
- Detect system preference via `prefers-color-scheme` media query
- Persist user choice in localStorage
- Respect `prefers-reduced-motion` for theme transitions
- Provide fallback for browsers without custom property support
- Use soft blacks (e.g., #1a1a1a) instead of pure black (#000) in dark mode to reduce eye strain

## Output

Deliver the implementation in this structure:

### 1. Color System Architecture
CSS custom property definitions for both themes with mathematical justification for adapted brand colors.

### 2. Color Mapping Table
Original brand colors, dark mode equivalents, contrast ratios against backgrounds, and WCAG compliance status.

### 3. Implementation Code
Structured code blocks with inline comments explaining accessibility decisions:
- Theme toggle mechanism with localStorage persistence
- System preference detection
- Smooth transitions (respecting motion preferences)
- Focus state management

### 4. Testing Checklist
Validation steps with specific tools:
- Automated contrast checkers (axe DevTools, WAVE)
- Manual testing procedures
- Screen reader verification points
- Browser compatibility checks

### 5. Troubleshooting Guide
Common dark mode accessibility failures and their fixes: insufficient contrast on hover states, broken focus indicators, pure black backgrounds causing halation, and solutions.
```

## 用法 / Usage
- 必填變數 / Variables: {{project-setup}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Skill_Prompt_Spec_Extractor
- 適用 / Use when: The WCAG-Compliant Dark Mode Implementation Prompt is a free AI prompt that generates accessible dual-theme sy…
