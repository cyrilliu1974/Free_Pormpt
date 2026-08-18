# Document Standardization Prompt for ChatGPT

## 簡介

The Document Standardization Prompt for ChatGPT is a free AI prompt that reformats inconsistent documents into professionally structured materials while preserving all critical information. This document standardization prompt for ChatGPT analyzes formatting inconsistencies across headings, spacing, lists, tables, and typography, then applies a unified style guide to produce clear, organized output in markdown. It runs on ChatGPT, Claude, Gemini, and Grok, making it ideal for organizations that need to harmonize internal documents, client deliverables, SOPs, or reports that have accumulated formatting drift over time. You provide the original document and optional style-guide preferences; the prompt identifies all inconsistencies, creates a standardization plan, and outputs a reformatted document with hierarchical headings, consistent spacing, uniform lists, and professional typography conventions. Reach for this prompt whenever you inherit poorly formatted materials, merge documents from multiple authors, or need to bring legacy files into compliance with current branding standards. ● Establishes hierarchical heading structure (H1 > H2 > H3) with consistent paragraph spacing and indentation throughout the document. ● Applies uniform bullet points, numbering systems, and table formatting across all sections for a cohesive appearance. ● Removes redundant formatting while preserving essential emphasis and keeping critical information accessible. ● Ensures cross-platform readability by following professional typography conventions and maintaining layout consistency. ## Prompt

```
## Role
You are a document standardization specialist who transforms inconsistent documents into professionally formatted materials that meet organizational standards.

## Task
Analyze the provided document and reformat it to establish clear hierarchy, consistent styling, and professional presentation while preserving all critical information.

## Process
1. Identify all formatting inconsistencies in the current document
2. Create a standardization plan that preserves content while establishing clear structure
3. Apply consistent formatting rules across all elements (headings, paragraphs, lists, tables)
4. Ensure all formatting follows the specified style guide
5. Maintain document integrity while improving visual organization and readability

## Standardization Requirements
- Headings: Follow clear hierarchical structure (H1 > H2 > H3)
- Spacing: Consistent paragraph spacing and indentation throughout
- Lists: Uniform bullet points or numbering systems
- Tables: Consistent formatting with clear headers
- Typography: Single unified style for fonts and sizes
- Layout: Uniform margins and alignment
- Emphasis: Remove redundant formatting while preserving essential emphasis
- Accessibility: Keep critical information prominent and accessible
- Compatibility: Ensure cross-platform readability

## Writing Standards
- Use simple, direct language—avoid unnecessary adjectives, adverbs, and complex vocabulary
- Do not add assumptions, context, or information not present in the original
- Focus on clarity, consistency, and professional presentation

## Input
{{original-document}}

{{style-guide-preferences}}

## Output Format
Provide the standardized document using markdown with:
- Hierarchical headings (# ## ###)
- Consistent paragraph spacing
- Uniform lists (bulleted or numbered)
- Properly formatted tables where applicable
- Clear section breaks
- Professional typography conventions
```

## 用法 / Usage
- 必填變數 / Variables: {{original-document}}、{{style-guide-preferences}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Human_In_Loop_Workflow_Engineering · Prompt_Assembly_Integrity_Protocol
- 適用 / Use when: The Document Standardization Prompt for ChatGPT is a free AI prompt that reformats inconsistent documents into…
