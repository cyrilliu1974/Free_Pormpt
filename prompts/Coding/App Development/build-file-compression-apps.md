# File Compression App Builder

## 簡介

The File Compression App Builder is a free AI prompt that generates complete, production-ready code for a privacy-first file compression application built with React 18+ and TypeScript. It produces a full-stack codebase including format-specific compression engines, a real-time quality comparison interface inspired by Linear.app and Figma, and batch processing with progress tracking - all designed to run entirely client-side without server uploads. This file compression app prompt for ChatGPT works on ChatGPT, Claude, and Cursor to deliver architecture, components, compression algorithms, styling, and deployment documentation in a single pass. Reach for this prompt when you need to build a professional compression tool that prioritizes user privacy, transparent quality controls, and intelligent optimization across multiple file formats. ● Outputs client-side compression engines that analyze file characteristics and apply format-specific optimization without requiring server uploads. ● Generates a dark-mode interface with split-view previews, quality metrics, zoom controls, and educational tooltips explaining compression tradeoffs. ● Includes batch processing logic with progress tracking, failure recovery, and intelligent queue management for handling multiple files. ● Delivers organized project structure, component hierarchy, compression algorithms, styling with Tailwind or CSS, and setup documentation with inline comments. ## Prompt

```
## Role

You are a senior software engineer specializing in file compression systems, with expertise in codec theory, perceptual quality metrics, and format-specific optimization.

## Task

Build a complete, production-ready smart file compression application using React 18+ with TypeScript. The application must handle {{file-types}} with format-specific optimization engines, process everything client-side for privacy, and provide real-time quality comparisons.

## Context

This application prioritizes user privacy through client-side processing, provides transparent compression controls, and delivers optimization without quality degradation. The interface should feel fast, trustworthy, and educational—helping users understand compression tradeoffs.

## Requirements

**Architecture & Privacy**
- Client-side processing only—no server uploads
- Proper TypeScript interfaces throughout
- Comprehensive error boundaries and handling
- Performance optimization for large files

**Compression Engines**
- Format-specific optimization for each file type
- Intelligent algorithms that analyze file characteristics
- Quality metrics and perceptual analysis
- Lossless and lossy options with transparent controls

**User Interface**
- Design inspired by Linear.app and Figma's export panel
- Dark mode with clean typography and micro-animations
- Real-time preview with split-view comparison
- Quality metrics display and zoom controls
- Batch processing with progress tracking and failure recovery
- Educational tooltips explaining compression tradeoffs

**Technical Stack**
{{tech-stack}}

## Output

Deliver complete, production-ready code organized as follows:

1. **Project Structure**: File organization, component hierarchy, and module architecture
2. **Core Components**: File upload, compression panel, preview canvas, download management
3. **Compression Engines**: Format-specific optimization algorithms with quality analysis
4. **Preview System**: Real-time comparison interface with metrics and controls
5. **Batch Processing**: Multi-file queue management with progress tracking and error recovery
6. **Styling**: Complete CSS/Tailwind implementation with dark mode and responsive design
7. **Utilities**: Compression algorithms, format detection, quality analysis, file management
8. **Documentation**: Setup instructions, dependencies, and deployment guidelines

Include detailed inline comments explaining compression strategies, algorithm choices, and optimization techniques.
```

## 用法 / Usage
- 必填變數 / Variables: {{file-types}}、{{tech-stack}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The File Compression App Builder is a free AI prompt that generates complete, production-ready code for a priv…
