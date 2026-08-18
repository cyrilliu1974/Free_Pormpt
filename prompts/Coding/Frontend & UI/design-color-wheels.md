# Color Wheel Application Generator

## 簡介

The Color Wheel Application Generator is a free AI prompt that produces complete React color wheel applications with professional-grade color theory and interactive features for designers and developers. This color wheel generator prompt for ChatGPT, Claude, and Cursor outputs a full TypeScript React component implementing HSB color space rendering, real-time harmony calculations (complementary, triadic, analogous, split-complementary), canvas-based interactions at 60fps, and RGB/HSL/hex conversion mathematics. Developers building design tools, prototyping color pickers, or creating educational color theory applications receive structured code with technical architecture, canvas rendering logic, UI layout, history management, keyboard shortcuts, and WCAG accessibility patterns. The prompt adapts to your skill level and deployment constraints via the developer-context variable. Reach for this prompt when you need a sophisticated color selection tool that goes beyond basic pickers, delivering the mathematical precision and user experience of industry design software. ● Outputs complete React + TypeScript component architecture with optimized color conversion mathematics across RGB, HSL, and HSB color spaces. ● Implements smooth canvas-based HSB color wheel rendering with interactive drag selection and 60fps performance optimization strategies. ● Generates color harmony calculation systems for complementary, triadic, analogous, and split-complementary schemes with visual preview. ● Includes professional UI patterns: real-time color displays in multiple formats, copy-to-clipboard functionality, history management, keyboard shortcuts, and WCAG accessibility compliance. ## Prompt

```
## Role
You are an expert creative developer and color theory specialist building production-grade interactive design tools.

## Task
Create a complete, production-ready color wheel application with advanced functionality matching professional design tool standards (Adobe, Figma). This is a sophisticated interactive tool for professional designers, not a basic color picker. It must handle complex color theory mathematics, deliver smooth 60fps interactions, and include advanced features like color harmony generation and history management.

## Context
{{developer-context}}

Provide:
- Technical skill level with React, TypeScript, and Canvas
- Target users (designers, artists, etc.) and their workflow needs
- Specific visual or functional preferences
- Deployment constraints or platform limitations
- Timeline and must-have feature priorities

## Output
Deliver a complete React component with detailed implementation guidance structured as:

### Technical Architecture
- Component structure and organization
- Color conversion mathematics (RGB, HSL, HSB)
- Performance optimization strategies for 60fps

### Canvas Implementation
- HSB color wheel rendering with smooth gradients
- Interactive selection and drag behavior
- Real-time visual feedback

### User Interface Design
- Clean, professional layout
- Real-time color displays (hex, RGB, HSL)
- Copy-to-clipboard functionality
- Responsive design approach

### Color Harmony System
- Mathematical calculations for complementary, triadic, analogous, and split-complementary schemes
- Visual harmony preview

### Advanced Features
- Color history management
- Keyboard shortcuts
- Accessibility (WCAG compliance)

### Code Quality
- TypeScript types and interfaces
- Error handling and edge cases
- Production optimization techniques

Present as implementable code with explanatory bullet points for each section.
```

## 用法 / Usage
- 必填變數 / Variables: {{developer-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Color Wheel Application Generator is a free AI prompt that produces complete React color wheel application…
