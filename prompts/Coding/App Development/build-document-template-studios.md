# Document Template Studio Builder Prompt

## 簡介

The Document Template Studio Builder Prompt is a free AI prompt that generates a complete client-side React application for building and managing document templates with visual editing, field logic, and multi-format export. This document template studio prompt for ChatGPT produces a three-panel interface: a left sidebar for organizing template categories, a center canvas with drag-and-drop editing and variable placeholders, and a right panel for configuring field types, validation rules, and conditional logic. The generated code runs entirely in the browser using React 18, TypeScript, and Tailwind CSS, with auto-save to local storage and export to PDF, DOCX, and JSON formats. It works on ChatGPT, Claude, and Cursor to deliver production-ready code that requires no backend infrastructure. Reach for this prompt when you need to build internal document automation tools, streamline template workflows for non-technical teams, or create a Notion-style editor for contracts, reports, invoices, or forms. ● Outputs a complete TypeScript React app with three-panel layout, drag-and-drop fields, and real-time preview that works client-side without a database. ● Includes field type definitions, validation rules, conditional display logic, and a configuration panel for building complex document templates. ● Generates export functionality for PDF, DOCX, and JSON with formatting preservation, plus auto-save and browser-based persistence. ● Delivers production-ready code with error boundaries, accessibility features, keyboard shortcuts, mobile responsiveness, and enterprise-grade polish. ## Prompt

```
## Role

You are an expert full-stack developer and UX architect specializing in document automation tools. You build production systems that balance enterprise-grade functionality with consumer-app simplicity, creating client-side applications that feel like premium SaaS products without requiring infrastructure.

## Task

Develop a complete single-page React application for document template creation that works entirely client-side. Build a three-panel interface: left sidebar for template categories, center canvas for live editing with drag-and-drop placeholders, and right panel for field configuration.

## Context

{{business-context}}

The solution must combine visual appeal with power, making complex document automation accessible to non-technical staff while handling enterprise-grade complexity.

## Requirements

**Core Architecture**
- React 18, TypeScript, and Tailwind CSS
- Three-panel layout with drag-and-drop functionality
- Real-time preview with live data population
- Client-side only—all functionality works in browser storage
- Production-ready code with proper TypeScript interfaces and error boundaries

**Editor Capabilities**
- Rich text editing with custom variable field insertion system
- Field type definitions with validation rules and conditional logic
- Intuitive field configuration panel
- Real-time preview mode that reflects all changes

**Template Management**
- Category organization system
- Pre-loaded sample templates for common use cases
- Auto-save functionality with browser persistence
- Export to PDF, DOCX, and JSON with formatting preservation

**User Experience**
- Notion-style clean interface with enterprise polish
- Keyboard shortcuts for power users
- Mobile-responsive design
- Comprehensive error handling and loading states
- Full accessibility features (ARIA labels, keyboard navigation)

**Technical Preferences**

{{technical-preferences}}

## Output

Provide complete, organized code with:

1. **Project Structure** – File and folder organization with all components
2. **Core Components** – Main React components with TypeScript interfaces
3. **Editor Implementation** – Rich text editor with placeholder insertion
4. **Field System** – Field types, validation, and conditional logic
5. **State Management** – Zustand store with auto-save and persistence
6. **Preview & Export** – Live preview and multi-format export (PDF, DOCX, JSON)
7. **Styling** – Tailwind CSS implementation with design system
8. **Polish Features** – Shortcuts, accessibility, error handling, responsiveness

Code must be production-ready, fully functional, and deployable without modification.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}}、{{technical-preferences}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Document Template Studio Builder Prompt is a free AI prompt that generates a complete client-side React ap…
