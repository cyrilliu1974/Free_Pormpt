# File Converter Web App Builder for React

## 簡介

The File Converter Web App Builder is a free AI prompt that generates production-ready React code for a universal file conversion tool with complete client-side processing for developers and engineers building privacy-first applications. This file converter prompt for ChatGPT, Claude, and Cursor produces a full-stack TypeScript application supporting documents (PDF, DOCX, TXT, Markdown, HTML), images (PNG, JPG, WEBP, SVG, GIF), spreadsheets (XLSX, CSV, JSON), and media (MP4, WEBM, GIF). The prompt outputs modular converter classes, streaming architecture for large files, shadcn/ui components, and comprehensive error recovery for corrupted files and edge cases. It handles real-world enterprise scenarios where sensitive data cannot leave the browser and files exceed memory limits. Reach for this prompt when you need a Squoosh.app-style converter with batch processing, quality controls, and WCAG 2.1 AA accessibility built in. ● Outputs modular converter classes with format validation, streaming support, and memory management for files exceeding browser limits ● Generates React + TypeScript components with dark mode, keyboard shortcuts, batch processing with progress tracking, and mobile-responsive touch controls ● Includes WCAG 2.1 AA accessibility implementation with ARIA labels, screen reader support, and full keyboard navigation ● Provides specific library integration examples (pdf-lib, mammoth, papaparse, ffmpeg.wasm) with error handling for corrupted files and unsupported formats ## Prompt

```
## Role

You are a senior full-stack engineer specializing in file processing systems. You build production-grade conversion pipelines that handle edge cases, corrupted files, and large file sizes with robust error recovery and optimal memory management.

## Task

Build a universal file converter web application with client-side processing that supports:

- **Documents**: PDF ↔ DOCX ↔ TXT ↔ MD ↔ HTML
- **Images**: PNG ↔ JPG ↔ WEBP ↔ SVG ↔ GIF
- **Spreadsheets**: XLSX ↔ CSV ↔ JSON
- **Media**: MP4 ↔ WEBM ↔ GIF

Create a clean, minimal interface inspired by Squoosh.app and Linear.app using React with TypeScript and shadcn/ui components.

## Context

The application must handle real-world enterprise scenarios: large files that exceed memory limits, corrupted data that crashes parsers, and sensitive documents that cannot be uploaded to servers. All processing must occur client-side using browser APIs for complete data privacy.

{{requirements}}

## Technical Requirements

**Architecture**
- Modular converter classes for each file type with format validation
- Streaming support for files exceeding memory limits
- TypeScript interfaces for type safety
- Browser APIs only (no server uploads)

**User Experience**
- Batch processing with progress tracking
- Quality settings and metadata preservation options
- Keyboard shortcuts and preference persistence
- Dark mode support
- Mobile-responsive with touch-friendly controls

**Accessibility**
- WCAG 2.1 AA compliance
- Screen reader support with ARIA labels
- Full keyboard navigation
- Focus management and skip links

**Reliability**
- Comprehensive error handling for corrupted files
- Graceful degradation when formats are unsupported
- Memory management strategies (chunking, workers, cleanup)
- Clear user feedback for all operations

## Output

Provide production-ready code organized as:

1. **Interface Design** – Component structure, user flow, and interaction patterns
2. **Technical Architecture** – React components, TypeScript interfaces, library integrations, and state management
3. **Conversion Engine** – Modular converter classes with validation, transformation logic, and error handling
4. **Performance Optimization** – Streaming implementation, memory management, and file size handling
5. **UX Features** – Batch processing, progress tracking, keyboard shortcuts, and settings persistence
6. **Accessibility Implementation** – ARIA attributes, keyboard navigation, screen reader announcements
7. **Error Handling** – Recovery strategies for corrupted files, validation failures, and browser limitations
8. **Implementation Guide** – Development roadmap, testing strategy, and deployment considerations

Include specific library recommendations (e.g., pdf-lib, mammoth, papaparse, ffmpeg.wasm) with integration examples.
```

## 用法 / Usage
- 必填變數 / Variables: {{requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Prompt&Manifest_Engineering · Manifest_Driven_Code_Skeleton_Generator
- 適用 / Use when: The File Converter Web App Builder is a free AI prompt that generates production-ready React code for a univer…
