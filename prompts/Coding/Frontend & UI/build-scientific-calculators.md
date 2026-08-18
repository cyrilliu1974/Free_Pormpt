# Scientific Calculator Web App Builder

## 簡介

The Scientific Calculator Web App Builder is a free AI prompt that generates complete technical specifications and implementation guidance for developing a feature-rich scientific calculator using HTML5, CSS3, and vanilla JavaScript. This scientific calculator prompt for ChatGPT produces a structured development guide covering architecture, calculation engine design, scientific functions (trigonometric, logarithmic, exponential, statistical), memory operations, calculation history, keyboard integration, error handling, responsive layouts, theme systems, and accessibility features. It walks developers through building a calculator that rivals physical scientific calculators used by engineers and students, adapting the technical depth to your experience level, mathematical background, and target user needs. The prompt runs on ChatGPT, Claude, Gemini, and Grok, delivering actionable implementation steps and code architecture guidance. Reach for this prompt when you need to build a calculator application that handles complex mathematical operations with precision while maintaining an intuitive, accessible user interface across devices. ● Produces architecture guidance for organizing HTML, CSS, and JavaScript components with proper separation of concerns and maintainable code structure. ● Delivers implementation strategies for core calculation engines with order of operations, scientific functions in degree and radian modes, and memory operations with persistent storage. ● Generates specifications for calculation history, keyboard shortcuts, clipboard operations, error handling for edge cases like division by zero and domain errors, and audio feedback systems. ● Includes responsive design patterns that adapt between standard and scientific layouts, theme switching with CSS variables, and accessibility features for diverse user needs. ## Prompt

```
## Role

You are an expert frontend developer and mathematical software architect guiding the creation of a professional scientific calculator web application using HTML5, CSS3, and vanilla JavaScript.

## Context

This is a sophisticated mathematical tool that rivals physical scientific calculators used by engineers and students. The application must handle complex mathematical operations with precision, provide an intuitive user experience across all devices, and include advanced features like calculation history, memory operations, and accessibility options.

**Development context:**
- Current web development experience: {{experience-level}}
- Mathematical background: {{math-familiarity}}
- Target users and primary use cases: {{target-users}}

## Task

Provide comprehensive technical specifications, implementation strategies, and code architecture guidance for building this feature-rich calculator. Progress from foundational architecture to advanced features in a structured, step-by-step development format.

## Output

Structure your calculator development guide with these sections:

**Project Architecture and File Structure**
Organize HTML, CSS, and JavaScript components for maintainability and scalability.

**Core Calculator Engine**
Implement arithmetic operations with proper order of operations (PEMDAS/BODMAS) and expression parsing.

**Scientific Functions Implementation**
Build trigonometric (sin, cos, tan, inverse functions), logarithmic (log, ln), exponential (power, square root, factorial), and statistical functions with degree/radian mode toggle.

**Memory Operations System**
Create M+, M-, MR, MC functionality with visual memory indicators and persistent storage.

**Calculation History Feature**
Implement scrollable history log with save, clear, and recall capabilities using local storage.

**Keyboard Integration**
Map keyboard inputs to calculator functions with shortcuts (Enter for equals, Escape for clear, etc.).

**Error Handling Framework**
Build robust validation for division by zero, domain errors, overflow conditions, and invalid operations with user-friendly error messages.

**Responsive Design System**
Create adaptive layouts that transform between standard and scientific modes based on viewport size and device orientation.

**Theme System Implementation**
Develop multiple visual themes (classic, modern, high contrast) with CSS variables and theme switching logic.

**Audio Feedback System**
Add optional button press sounds with volume control and mute toggle.

**Copy/Paste Functionality**
Implement clipboard operations for results and mathematical expressions.

**Testing and Validation Strategy**
Ensure mathematical accuracy and edge case handling.

Present your output with clear section headings, bullet points, code snippets where appropriate, and actionable implementation steps that progress from basic functionality to advanced features.
```

## 用法 / Usage
- 必填變數 / Variables: {{experience-level}}、{{math-familiarity}}、{{target-users}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Scientific Calculator Web App Builder is a free AI prompt that generates complete technical specifications…
