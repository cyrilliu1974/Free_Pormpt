# Feature Launch Knowledge Base Article Generator

## 簡介

The Feature Launch Knowledge Base Article Generator is a free AI prompt that creates comprehensive documentation sets for product teams preparing to release new features. It produces five interconnected articles - overview, getting started guide, how-to workflow, troubleshooting resource, and FAQ - along with a strategic cross-linking map that ensures users find answers regardless of their entry point. This feature launch knowledge base prompt for ChatGPT, Claude, Gemini, and Grok anticipates user confusion patterns and documents edge cases before customers encounter them, reducing launch-day support volume. Product documentation specialists, customer success managers, and technical writers reach for this prompt when they need complete feature documentation ready before release day, ensuring support teams have reference materials the moment users start exploring new capabilities. ● Creates five distinct article types that cover features from every user entry point, preventing the documentation gap that follows typical product releases. ● Includes troubleshooting guidance based on predictable failure points with specific diagnostic steps, not vague contact-support language. ● Generates a cross-linking map showing which articles reference others, where links appear, and what anchor text to use for navigation. ● Documents known limitations, edge cases, and prerequisite requirements explicitly so users understand boundaries and dependencies. ## Prompt

```
## Role

You are a product documentation specialist with deep customer support experience. You anticipate user confusion patterns, edge cases, and failure points before they occur. You write complete knowledge base ecosystems that prevent launch-day support floods by addressing every angle users approach a feature.

## Task

Create a complete, interconnected knowledge base article set for a new feature launching soon. Produce five distinct articles that cover the feature from every user entry point, preventing the documentation gap that turns launches into support chaos.

Before writing, consider:
- What is the user's entry point to this feature?
- What prerequisite knowledge are we assuming?
- What will they try first that won't work?
- What terminology will confuse them?
- What related features will they conflate this with?
- What will they expect that we don't deliver?

## Context

**Feature details:** {{feature-details}}

**Known limitations and caveats:** {{limitations}}

## Output

Deliver five complete articles as a sequential set:

### 1. Overview Article
Orients users to what exists and why it matters, without instructional steps. Helps users determine if this feature is relevant to their needs. Include prerequisite features, permissions, or plan requirements. Note any differences across user types.

### 2. Getting Started Guide
Walks through initial setup in prerequisite-first order. Gets users from zero to activated without confusion. Document required setup steps before attempting main workflows.

### 3. How-To Guide
Documents the primary intended workflow step-by-step. Enables successful execution of the core use case. Use numbered steps for sequential actions.

### 4. Troubleshooting Article
Addresses the 3-5 most predictable failure points with diagnostic steps and fixes. Unblocks users without requiring support contact. Format as problem-solution pairs with specific diagnostic steps.

### 5. FAQ Article
Captures 5-8 questions that don't fit cleanly into procedural documentation. Answers conceptual, limitation, and edge case questions. Format as question-answer pairs addressing real anticipated confusion.

### Cross-Linking Map
After all five articles, provide a structured table showing:
- Which articles link to which others
- Where in each article the links appear
- What anchor text to use for each link

## Guidelines

**Write for real user behavior:**
- Anticipate actual confusion patterns, not idealized workflows
- Document known limitations and edge cases explicitly
- Use prerequisite-first ordering in instructions
- Include specific diagnostic steps, not vague suggestions
- Address actual anticipated questions in FAQs, not filler content

**Maintain structural clarity:**
- Each article must stand alone while connecting to others
- Create clear article boundaries so users know which to consult
- Use consistent formatting across all five articles
- Keep setup steps in Getting Started, not in Overview
- Number procedural steps; use bullets for non-sequential information

**Avoid:**
- Marketing language or selling the feature's value
- Promising capabilities the feature does not have
- Skipping edge cases because they seem uncommon
- Writing a single overview instead of the full five-article set
- Vague troubleshooting advice like "contact support"
- Generic FAQs that could apply to any feature
- Assuming knowledge users don't have
```

## 用法 / Usage
- 必填變數 / Variables: {{feature-details}}、{{limitations}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Manifest_Heuristic_Consistency_Scanner
- 適用 / Use when: The Feature Launch Knowledge Base Article Generator is a free AI prompt that creates comprehensive documentati…
