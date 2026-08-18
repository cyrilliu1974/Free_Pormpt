# Color Picker Tool Builder Prompt

## 簡介

The Color Picker Tool Builder Prompt is a free AI prompt that generates fully functional color picker web applications for designers and developers who need professional-grade color tooling without external dependencies. This color picker tool builder prompt for ChatGPT produces complete HTML5, CSS3, and vanilla JavaScript code organized into modular sections: a multi-input color selection interface (eyedropper API, color wheel, RGB/HSL sliders), bidirectional format conversion between RGB, RGBA, HSL, HSLA, HEX, and CMYK, algorithm-based palette generators for complementary, analogous, triadic, tetradic, and monochromatic schemes, a visual gradient editor with linear, radial, and conic outputs, WCAG contrast ratio calculator, colorblindness simulation for protanopia, deuteranopia, and tritanopia, and export functionality for Adobe ASE, JSON, CSS variables, and SCSS formats. The prompt runs on ChatGPT, Claude, Gemini, and Grok and delivers production-ready code with responsive layouts, keyboard navigation, screen reader support, and local storage for saved color collections. Use it when building design systems, creating accessibility audit tools, or streamlining designer-developer handoffs. ● Delivers ten core features including eyedropper API integration, harmony visualization on an interactive color wheel, and intelligent color naming based on hue, saturation, and lightness ● Outputs organized code sections with inline comments, ES6+ JavaScript, ARIA labels, and progressive enhancement principles for evergreen browsers ● Includes WCAG contrast checker and colorblindness filters to meet accessibility standards in design workflows ● Provides export options for Adobe ASE, JSON, CSS custom properties, and SCSS variables with one-click copy for code snippets ## Prompt

```
## Role

You are a senior frontend architect specializing in design systems and color tooling. You understand the friction points in designer-developer workflows: format conversions under deadline, accessibility audits, and design handoffs. You build tools that anticipate the next action and serve both spatial (designer) and programmatic (developer) mental models without compromise.

## Task

Build a comprehensive, professional-grade color tool using HTML5, CSS3, and vanilla JavaScript. Create a fully functional web application with these components:

**Core Features**
1. **Color Selection Interface** – Multiple input methods (eyedropper API, color wheel, RGB/HSL sliders, direct input) with real-time preview
2. **Format Conversion System** – Bidirectional conversion between RGB, RGBA, HSL, HSLA, HEX, CMYK with one-click copy
3. **Palette Generator** – Algorithm-based generation for complementary, analogous, triadic, tetradic, and monochromatic schemes
4. **Favorites Management** – Local storage for saved colors with custom names and organized collections
5. **Color Harmony Visualization** – Interactive color wheel showing harmony rules with adjustable parameters
6. **Gradient Generator** – Linear, radial, and conic gradients with multiple color stops and CSS output
7. **Accessibility Checker** – WCAG contrast ratio calculator and colorblindness simulation (protanopia, deuteranopia, tritanopia)
8. **Code Export System** – Copy-ready snippets for CSS, SCSS, and SVG formats
9. **Color Naming Algorithm** – Intelligent naming based on hue, saturation, and lightness
10. **Export Functionality** – Export to Adobe ASE, JSON, CSS variables, and SCSS formats

## Context

{{use-case-and-requirements}}

**Default priorities:** Accessibility checker, format conversion, and palette generator take precedence unless specified otherwise.

**Technical requirements:** Standalone tool supporting latest evergreen browsers (Chrome, Firefox, Safari, Edge) with graceful degradation for eyedropper API. No external libraries—vanilla JavaScript only.

## Output

Provide complete, production-ready code organized into these sections:

### HTML Structure
Complete HTML5 markup with semantic elements, accessibility attributes (ARIA labels, roles), and organized sections for each tool component.

### CSS Styling
Comprehensive CSS3 with custom properties for theming, responsive layouts using mobile-first approach, smooth animations, and component-specific styles. Use logical grouping and consistent naming conventions.

### JavaScript Core
Core functionality including:
- Color conversion algorithms (RGB ↔ HSL ↔ HEX ↔ CMYK)
- State management for user preferences and collections
- Utility functions with error handling and input validation
- Performance optimization for real-time calculations

### Color Selection Module
Color picker interface implementation with multiple input methods, real-time preview, and eyedropper API integration with fallback.

### Palette Generator Module
Harmony algorithms (complementary, analogous, triadic, tetradic, monochromatic) with interactive controls and visualization.

### Gradient Builder Module
Visual gradient editor with color stop management and CSS output generation.

### Accessibility Tools Module
WCAG contrast ratio calculator and colorblindness simulation filters with visual feedback.

### Export System Module
Code generation for multiple formats and file export functionality.

### Storage Management Module
Local storage implementation for favorites, collections, and user preferences with data persistence.

### Integration Guide
Clear instructions for implementing, customizing, and extending the tool. Include code organization principles and extension points.

**Code requirements:**
- Modular, maintainable functions with clear separation of concerns
- Detailed inline comments explaining complex logic and architectural decisions
- Progressive enhancement principles
- Modern JavaScript (ES6+) with fallback considerations
- Keyboard navigation and screen reader support
- Visual feedback for all interactive states
- Responsive design patterns (desktop and mobile)
- Comprehensive error handling and input validation
- Copyable code blocks with proper syntax formatting
```

## 用法 / Usage
- 必填變數 / Variables: {{use-case-and-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Color Picker Tool Builder Prompt is a free AI prompt that generates fully functional color picker web appl…
