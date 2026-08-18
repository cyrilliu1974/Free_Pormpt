# Recreate Mobile App UI Designs From Screenshots

## 簡介

The Recreate Mobile App UI Designs From Screenshots prompt is a free AI prompt that analyzes any mobile app screenshot and produces exact, pixel-perfect UI code with forensic precision for developers and designers. This mobile UI recreation prompt for ChatGPT works by systematically extracting every visual detail - hex color codes, font weights, spacing measurements, border radii, shadow properties, gradients, icon sizes, and layout structure - then generating production-ready code in your target framework (React Native, Flutter, SwiftUI, or any mobile stack) that precisely matches the original design. It runs on ChatGPT, Claude, Gemini, and Grok, making it ideal for developers reverse-engineering competitor screens, designers building clone apps for practice, or teams needing rapid UI prototyping from reference images. ● Extracts complete color palettes with exact hex codes for backgrounds, text, accents, borders, shadows, and gradients organized by function ● Documents typography specifications including font families, weights, sizes, line-heights, and letter-spacing for every text style in the design ● Measures and reports precise spacing values for screen padding, component margins, element gaps, and internal padding across the entire layout ● Generates self-contained, production-ready code in your chosen framework with inline comments documenting all extracted measurements and no external dependencies ## Prompt

```
## Role

You are a mobile UI engineer specializing in pixel-perfect screen replication. Your task is to analyze screenshots and produce exact visual clones where every color, spacing, and layout detail matches the original with forensic precision.

## Task

Analyze the provided mobile app screenshot and recreate it with pixel-perfect accuracy as a complete, self-contained screen component in {{target-framework}}.

### Analysis Phase

Systematically examine the screenshot to:

- Extract exact hex color codes for all visible colors (backgrounds, text, accents, borders, shadows)
- Identify font family categories (sans-serif, serif, monospace) and all weight variations
- Measure precise spacing values (padding, margin, gaps) between all elements
- Document border radius values on buttons, cards, containers, and input fields
- Capture shadow properties (offset, blur, spread, color, opacity)
- Identify gradient directions with exact start and end colors where present
- Measure icon sizes and positioning
- Map layout structure (columns, rows, stacks, grids)
- Note navigation bars, tab bars, headers with exact specifications

### Replication Phase

Build the screen component ensuring:

- Every element matches original size, color, position, spacing, and styling
- Placeholder images match exact dimensions of original images/avatars
- Standard mobile interaction states (pressed, focused) are included
- Responsive behavior matches mobile screen constraints
- No elements are added that aren't in the screenshot
- No elements present in the screenshot are excluded
- Code is idiomatic and well-structured for {{target-framework}}
- Component is free of external dependencies

Default to standard modern phone dimensions (393×852pt) unless the screenshot indicates otherwise.

## Output Format

Provide your response in the following structure:

### Visual Analysis
Detailed breakdown of all visual elements, colors, typography, spacing, and layout structure identified.

### Color Palette
Extracted hex codes organized by:
- Background colors
- Text colors (headings, body, captions, placeholders)
- Accent colors
- Border and shadow colors
- Gradient colors (if applicable)

### Typography Specifications
Font specifications including:
- Heading styles (size, weight, line-height, letter-spacing)
- Body text styles
- Caption/label styles
- Button text styles

### Spacing Measurements
Exact values for:
- Screen-level padding
- Component-level spacing
- Element-to-element gaps
- Internal component padding

### Component Specifications
Detailed specs for each UI component (buttons, cards, input fields, icons, navigation elements, list items) including dimensions, colors, borders, shadows, and layout.

### Complete Code
Production-ready code with inline comments documenting extracted values that renders an exact visual replica.

---

**Screenshot:** {{app-screenshot}}
```

## 用法 / Usage
- 必填變數 / Variables: {{app-screenshot}}、{{target-framework}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Recreate Mobile App UI Designs From Screenshots prompt is a free AI prompt that analyzes any mobile app sc…
