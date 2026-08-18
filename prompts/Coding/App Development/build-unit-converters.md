# Build Unit Converters

## 簡介

The Build Unit Converters prompt is a free AI prompt that generates complete, single-file React applications for converting units across length, weight, temperature, volume, area, speed, time, digital storage, pressure, and energy. This unit converter prompt for ChatGPT produces fully implemented code with real-time conversion as users type, bidirectional calculation logic, keyboard shortcuts (Tab switching, copy enhancements), conversion history tracking, and responsive design. The prompt works on ChatGPT, Claude, and Cursor, and takes two variables - tech-stack (React with Tailwind, styled-components, or CSS modules) and target-users (general public, engineers, students, etc.) - to tailor the output architecture and UX. Use it when you need a deployable converter without placeholders or TODO comments. Developers building measurement tools, students learning React component patterns, and teams prototyping utility applications will save hours of formula research and state-management setup. ● Implements precise conversion formulas for 10 categories with proper rounding and edge-case handling ● Includes real-time input validation, error boundaries, debouncing, and performance optimizations ● Provides keyboard shortcuts, one-click copy buttons, conversion history, and smooth animations ● Delivers complete component architecture, state management, and CSS styling with no placeholders ## Prompt

```
## Role
You are an expert full-stack developer building production-ready React applications.

## Task
Create a complete, single-file React universal unit converter application with comprehensive category coverage, real-time conversion, and professional UX.

## Context
Implement using {{tech-stack}}. Design for {{target-users}}.

## Requirements

**Conversion Categories**  
Implement full bidirectional conversion for: Length, Weight, Temperature, Volume, Area, Speed, Time, Digital Storage, Pressure, and Energy. Include comprehensive unit coverage with mathematical precision.

**Core Features**
- Real-time conversion as users type
- Keyboard shortcuts (Tab to switch fields, Cmd/Ctrl+C enhancements)
- Conversion history tracking
- One-click copy functionality
- Smooth animations and transitions
- Input validation and error handling
- Responsive design across all devices

## Output

Deliver production-ready code structured as:

**Component Architecture**: Define component hierarchy, state management approach, and data structures for conversion formulas

**Conversion Engine**: Implement precise mathematical conversion logic with proper rounding and edge case handling

**Visual Interface**: Create a clean, professional UI using modern CSS appropriate for the stack (Tailwind/styled-components/CSS modules)

**Interactive Logic**: Wire up real-time conversion, input handling, unit switching, and all user interactions

**Enhanced Features**: Add history tracking, keyboard shortcuts, copy buttons, and polished animations

**Performance & Polish**: Optimize re-renders, implement debouncing where needed, add loading states, and ensure error boundaries

Provide complete, working code with no placeholders or TODO comments. All functionality must be fully implemented and ready to deploy.
```

## 用法 / Usage
- 必填變數 / Variables: {{target-users}}、{{tech-stack}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Build Unit Converters prompt is a free AI prompt that generates complete, single-file React applications f…
