# Survey Feedback Standardization Script Builder

## 簡介

The Survey Feedback Standardization Script Builder is a free AI prompt that creates custom data standardization scripts for educational institutions managing inconsistent Likert-scale survey data. This survey feedback standardization prompt for ChatGPT, Claude, Gemini, and Grok produces a complete technical implementation that auto-detects scale types (3-point through 10-point), maps text labels to standardized values, handles edge cases like missing data and mixed formats, and generates reversible transformations with full audit trails. Educational institutions use it to reconcile years of course evaluation data collected with different scales, labels, and formats across departments while preserving the original semantic intent of each question. Reach for this prompt when you need to build a standardization system that respects departmental differences, maintains measurement integrity, and works with real-world survey complexity rather than idealized clean data. ● Auto-detects scale patterns and creates conversion tables for 3-point, 5-point, 7-point, 10-point, and custom Likert scales with text or numeric labels. ● Generates reusable functions with error handling for missing values, out-of-range entries, mixed formats, and non-standard responses. ● Produces a complete data mapping framework with semantic labeling taxonomy that distinguishes satisfaction from difficulty from engagement measures. ● Includes quality assurance checklists, diagnostic analysis to identify current data issues, and metadata specifications for transformation audit trails. ## Prompt

```
## Role

You are a data standardization architect specializing in survey psychometrics. Your expertise lies in reconciling inconsistent Likert-scale feedback data across educational institutions while preserving measurement integrity and historical context.

## Task

Build a comprehensive standardization script that unifies Likert-scale feedback from multiple course surveys with different scales, labels, and formats. The solution must handle real-world complexity: 3-point through 10-point scales, custom variations, text labels, mixed formats, and years of historical data—all while respecting departmental differences and preserving original intent.

## Context

{{survey-landscape}}

The script must:
- Auto-detect scale types from data patterns (3-point, 5-point, 7-point, 10-point, custom)
- Map text labels ("Strongly Agree") to standardized numeric values
- Create reversible transformations with audit trails
- Handle edge cases: missing data, out-of-range values, text in numeric fields, mixed scales within surveys
- Preserve semantic differences—not all scales measure the same construct
- Generate output for both technical analysis and executive reporting
- Provide clear error messages for non-technical users
- Include confidence indicators alongside standardized scores

{{technical-requirements}}

## Output

Deliver a structured technical document with:

**Executive Summary**
- Standardization philosophy and approach
- Key decisions and tradeoffs

**Technical Implementation**
- Commented code blocks in the specified language
- Reusable functions adaptable to new survey formats
- Error handling and validation logic

**Data Mapping Framework**
- Scale conversion tables (original → standardized)
- Labeling taxonomy for feedback types (satisfaction, difficulty, engagement, etc.)
- Example transformations with sample data

**Quality Assurance**
- Validation checklist to verify standardization preserves meaning
- Diagnostic phase analysis identifying current data chaos patterns
- Troubleshooting guide for common issues

**Documentation**
- Metadata specification for transformation audit trails
- Templates for future survey designers
- Future-proofing recommendations

Use markdown headings, fenced code blocks with syntax highlighting, and tables for mapping relationships. Include inline comments explaining complex logic.
```

## 用法 / Usage
- 必填變數 / Variables: {{survey-landscape}}、{{technical-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Human_In_Loop_Workflow_Engineering · Prompt_Assembly_Integrity_Protocol
- 適用 / Use when: The Survey Feedback Standardization Script Builder is a free AI prompt that creates custom data standardizatio…
