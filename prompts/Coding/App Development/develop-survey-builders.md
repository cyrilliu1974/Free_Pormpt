# Survey Builder Application Development Prompt

## 簡介

The Survey Builder Application Development Prompt is a free AI prompt that generates a complete, production-ready React survey platform for full-stack developers and product engineers. This survey builder prompt for ChatGPT, Claude, and Cursor produces a fully-functional web application combining intuitive design with enterprise features: conditional logic, drag-and-drop question management using @dnd-kit, 8+ question types (multiple choice, rating scales, file upload, matrix, and more), real-time preview, and separate builder and response interfaces. You provide your application requirements and tech stack preferences, and the prompt outputs a complete TypeScript codebase with Zustand state management, Framer Motion animations, and Tailwind CSS styling. Use it when you need to build a survey platform quickly without starting from scratch or when clients need a Google Forms alternative with advanced branching logic and a premium user experience. ● Delivers complete TypeScript interfaces, data models, and state management with auto-save and persistent storage. ● Implements a drag-and-drop builder interface with editors for text input, multiple choice, checkboxes, dropdowns, rating scales, file upload, date/time, and matrix questions. ● Includes a conditional logic engine supporting branching, skip logic, and real-time validation with error checking. ● Produces a mobile-responsive survey-taking interface with progress indicators, navigation, publishing workflow, and share link generation. ## Prompt

```
## Role
You are an expert full-stack product engineer building production-ready survey platform applications.

## Task
Create a complete, fully-functional React survey builder web application combining Google Forms simplicity with enterprise features: conditional logic, drag-and-drop question management, multiple question types, real-time preview, and separate builder/response interfaces. Deliver as a single artifact with no placeholders or TODOs.

## Context
**Application Requirements:**
{{application-requirements}}

**Technical Stack & Design Preferences:**
{{tech-stack}}

## Output
Deliver a complete React codebase with working implementations across all sections below, clearly commented:

**Data Architecture**
- Complete TypeScript interfaces and data models for surveys, questions, responses, and conditional logic rules

**State Management**
- Zustand store with auto-save and persistent storage

**Builder Interface**
- Drag-and-drop question bank using @dnd-kit
- Individual editor components for 8+ question types: text input, multiple choice, checkboxes, dropdowns, rating scales, file upload, date/time, matrix
- Conditional logic engine with branching and skip logic
- Real-time validation with error checking

**Response Interface**
- Clean, mobile-responsive survey-taking view
- Progress indicators and navigation
- Response submission with validation

**Publishing & Sharing**
- Survey settings configuration
- Publishing workflow
- Share link generation

**UI Polish**
- Framer Motion animations for smooth interactions
- Tailwind CSS with professional, premium aesthetic
- Consistent spacing, typography, and component hierarchy

Implement every feature as production-ready code with proper error handling and enterprise-quality UX. The application must feel polished with smooth interactions throughout.
```

## 用法 / Usage
- 必填變數 / Variables: {{application-requirements}}、{{tech-stack}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Survey Builder Application Development Prompt is a free AI prompt that generates a complete, production-re…
