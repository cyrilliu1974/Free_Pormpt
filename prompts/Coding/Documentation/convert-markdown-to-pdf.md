# Markdown to PDF Conversion Workflow Generator

## 簡介

The Markdown to PDF Conversion Workflow Generator is a free AI prompt that creates complete Pandoc conversion pipelines for technical writers, developers, and documentation teams. This Markdown to PDF prompt for ChatGPT, Claude, and Cursor analyzes your source content, styling requirements, and document context to output executable scripts, CSS templates, preprocessing steps, and quality-assurance checklists. It handles complex elements like syntax-highlighted code blocks, mathematical notation, cross-references, tables, and images while maintaining typography consistency and professional page layout. Use it when you need a production-ready conversion workflow that goes beyond basic Markdown rendering - whether for API documentation, technical manuals, reports, or multi-format publishing pipelines. ● Produces executable Pandoc scripts with engine selection, metadata configuration, and flag explanations. ● Generates CSS or LaTeX styling templates for custom fonts, margins, headers, footers, and syntax highlighting. ● Identifies edge cases in your source Markdown and provides preprocessing commands to handle hierarchical headings, code blocks, math notation, and multimedia. ● Includes step-by-step usage instructions and troubleshooting guidance for link validation, bookmark generation, and image rendering. ## Prompt

```
## Role
You are a technical documentation specialist and PDF conversion engineer with expertise in Pandoc workflows and professional typesetting standards.

## Task
Generate a complete Markdown-to-PDF conversion workflow that preserves semantic structure and produces professional output. Include preprocessing steps, Pandoc command configurations, CSS styling, and post-processing validation.

## Context
The conversion must handle complex document elements: hierarchical headings, syntax-highlighted code blocks, mathematical notation, cross-references, and multimedia. Output must maintain consistent typography, proper spacing, and professional formatting.

## Input
{{markdown-source}}

{{styling-requirements}}

{{document-context}}

## Output
Deliver a comprehensive implementation guide structured as:

### 1. Document Analysis
- Structural complexity assessment
- Content type inventory (code, math, images, tables)
- Edge case identification

### 2. Conversion Script
Provide complete, executable scripts in code blocks:
- Preprocessing commands (if needed)
- Full Pandoc command with flags and options
- Metadata configuration (title, author, date, TOC settings)
- PDF engine selection and rationale

### 3. Styling Implementation
- CSS or LaTeX template for custom styling
- Font selection and embedding
- Page layout (margins, headers, footers)
- Syntax highlighting theme

### 4. Quality Assurance
- Validation checks (bookmarks, links, image rendering)
- Common issues and troubleshooting steps
- Output optimization recommendations

### 5. Usage Instructions
Step-by-step bullet points for executing the workflow, from file preparation through final PDF generation.

Format all scripts in fenced code blocks with appropriate language tags. Organize instructions as clear, actionable bullet lists.
```

## 用法 / Usage
- 必填變數 / Variables: {{document-context}}、{{markdown-source}}、{{styling-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Human_In_Loop_Workflow_Engineering · Prompt_Assembly_Integrity_Protocol
- 適用 / Use when: The Markdown to PDF Conversion Workflow Generator is a free AI prompt that creates complete Pandoc conversion …
