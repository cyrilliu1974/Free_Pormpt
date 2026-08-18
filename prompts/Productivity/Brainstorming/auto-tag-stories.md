# Story Tagging and Categorization Prompt

## 簡介

The Story Tagging and Categorization Prompt is a free AI prompt that analyzes narrative content and generates structured metadata tags for writers, editors, and content managers. This story tagging prompt for ChatGPT reads your full story text, identifies key elements like themes, genre markers, tone, setting, character archetypes, and plot patterns, then outputs a markdown table showing each tag, its category (theme, genre, tone, etc.), and a clear justification for why that tag applies. It cross-references your existing tag library to maintain consistency, proposes new tags when gaps exist, and organizes tags hierarchically (for example, mapping a subgenre under its parent genre or a subtheme under a broader theme). The prompt runs on ChatGPT, Claude, Gemini, and Grok, making it adaptable to any text-generation workflow. Reach for this prompt when you need to standardize tagging across a story archive, prepare metadata for a content management system, or improve discoverability of fiction and non-fiction narratives. ● Extracts themes, genre markers, tone, setting, character types, and plot patterns from story text ● Cross-references an existing tag library to ensure consistency and suggests new tags when needed ● Outputs a markdown table with tag, category, and justification columns for easy import into CMS or taxonomy tools ● Organizes tags hierarchically to show parent-child relationships between genres, themes, and other categories ## Prompt

```
## Role
You are an expert content tagger specializing in story classification and metadata assignment.

## Task
Analyze the provided story and generate a comprehensive set of tags that accurately categorize its content. For each tag, specify its category and provide justification.

## Context
**Story:**
{{story-content}}

**Tag Library:**
{{tag-library}}

**Output Format:**
{{output-format}}

## Process
1. Read the story thoroughly to understand its narrative structure
2. Identify key elements: themes, genre markers, tone, setting, character types, and plot patterns
3. Select tags that are specific, relevant, and consistent with the existing tag library
4. Propose new tags when existing ones don't adequately capture essential story elements
5. Organize tags hierarchically where relationships exist (genre → subgenre, theme → subtheme)

## Output
Provide your tags in a markdown table:

| Tag | Category | Justification |
|-----|----------|---------------|
| ... | ... | ... |

Ensure each justification clearly explains why the tag applies to this specific story.
```

## 用法 / Usage
- 必填變數 / Variables: {{output-format}}、{{story-content}}、{{tag-library}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Story Tagging and Categorization Prompt is a free AI prompt that analyzes narrative content and generates …
