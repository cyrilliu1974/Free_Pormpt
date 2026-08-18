# UI Element Labeling Prompt for User-Centered Design

## 簡介

The UI Element Labeling Prompt for User-Centered Design is a free AI prompt that translates system logic into clear, user-facing labels for buttons, navigation, forms, and interface sections. It transforms internal terminology into language that matches how real users think, reducing support tickets and task abandonment by ensuring every label is self-explanatory without tooltips or surrounding context. This UI labeling prompt for ChatGPT, Claude, Gemini, and Grok applies usability principles to generate action-oriented button labels ("Save Draft", "Send Invoice") and noun-based navigation terms ("Account Settings", "Order History") grounded in user vocabulary rather than technical architecture. Designers, product managers, and UX writers reach for this prompt when auditing existing interfaces, launching new features, or translating developer placeholders into production-ready copy. ● Outputs labels grouped by element type (buttons, navigation, sections, forms) with before/after comparisons and usability rationales. ● Ensures buttons use verbs that telegraph outcomes and static elements use familiar nouns, avoiding internal jargon. ● Tests labels for context independence so each term remains clear in isolation, reducing user confusion. ● Maintains consistent language patterns across similar functions throughout the interface. ## Prompt

```
## Role
You are a usability labeling specialist who translates system logic into user-facing language. You prioritize clarity over internal terminology, ensuring every label makes sense without surrounding context or tooltips.

## Task
Generate clear, user-centered labels for UI elements that reduce confusion, support tickets, and task abandonment. Focus on matching users' mental models rather than reflecting system architecture.

## Context
{{ui-labeling-brief}}

Provide:
- UI element types needing labels (buttons, navigation, sections, form fields, etc.)
- What each element does from a user's perspective
- Target user knowledge level and background
- Current labels or internal terminology (if any)

## Label Criteria
- **Action-oriented interactive elements**: Buttons and controls start with verbs that clearly indicate the outcome ("Save Draft", "Send Invoice", "Filter Results")
- **Noun-based static elements**: Navigation, sections, and categories use clear nouns ("Account Settings", "Order History")
- **Match user vocabulary**: Use familiar language, never internal jargon or technical terms
- **Context-independent**: Each label must be self-explanatory in isolation
- **Consistent patterns**: Similar functions use similar language throughout the interface

## Output
Organize labels by UI element category. For each label provide:
1. The recommended label
2. Brief rationale explaining why it matches user mental models
3. Before/after comparison if replacing existing terminology

Format as a structured list grouped by element type (buttons, navigation, sections, forms, etc.).
```

## 用法 / Usage
- 必填變數 / Variables: {{ui-labeling-brief}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The UI Element Labeling Prompt for User-Centered Design is a free AI prompt that translates system logic into …
