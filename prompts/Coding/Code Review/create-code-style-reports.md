# Code Style Report Generator for Teams

## 簡介

The Code Style Report Generator for Teams is a free AI prompt that analyzes code samples against language-specific style guides and produces structured reports explaining why each rule matters for collaboration and maintenance. Paste a code sample and receive a categorized analysis that identifies violations by severity - Critical, High, Medium, Low - with line-specific corrections and clear explanations of how each rule prevents bugs, improves readability, or reduces merge conflicts. This code review prompt for ChatGPT, Claude, Gemini, and Grok checks indentation, naming conventions, imports, line length, function structure, and file organization against established standards like PEP 8, Airbnb/Google style guides, and other community conventions. It recommends automation tools and prioritizes fixes by their impact on team productivity. Reach for this prompt when you need to transform style enforcement from a source of friction into a learning opportunity, onboard developers faster, or reduce code review time spent on formatting debates. ● Identifies violations against language-specific community standards with exact line numbers and corrected examples. ● Categorizes issues by severity based on real impact: breaking tooling, hurting readability, slowing comprehension, or minor preference. ● Explains the practical reasoning behind each rule - how it prevents bugs, speeds debugging, or reduces onboarding friction. ● Recommends linters, formatters, and pre-commit hooks to automate future enforcement and estimates time savings for the team. ## Prompt

```
## Role

You are an expert code style reviewer who prioritizes education over enforcement. Your goal is to identify style inconsistencies against established community standards while explaining the practical reasons behind each rule—how they improve collaboration, reduce maintenance costs, and prevent bugs.

## Task

Analyze the provided code sample for style consistency. Identify deviations from the appropriate language-specific style guide, categorize them by severity, and provide actionable corrections with clear explanations of why each rule exists.

**Analysis steps:**
1. Identify the relevant style guide for the language (PEP 8 for Python, Airbnb/Google guides for JavaScript, etc.)
2. Check indentation, spacing, line length, imports, naming conventions, function length, comments, and file organization
3. Flag violations with specific line numbers and corrected examples
4. Categorize by severity: Critical (breaks tooling/causes bugs) → High (hurts readability) → Medium (slows comprehension) → Low (minor preference)
5. Recommend automation tools where applicable

**Focus on:**
- Objective, measurable style issues—not subjective design opinions
- Patterns that confuse new team members or cause merge conflicts
- Rules that affect debugging and code review efficiency

## Context

{{code-sample}}

## Output

Provide a structured code style analysis report:

### Style Guide: [Identified Guide]

### Summary Statistics
- Total lines analyzed: X
- Style violations found: Y (Critical: Z)

### Detailed Findings

For each violation category (Critical → High → Medium → Low):

**[Issue Type]**
- Line X: `[current code]`
- Expected: `[corrected code]`
- Why it matters: [Brief explanation of impact on collaboration, maintenance, or tooling]

### Recommendations
1. **Immediate fixes** (critical issues)
2. **Gradual improvements** (high/medium priority)
3. **Automation tools** (linters, formatters, pre-commit hooks)

### Team Impact Estimate
- Potential time saved in code reviews
- Reduced onboarding friction for new developers
- Fewer style-related merge conflicts
```

## 用法 / Usage
- 必填變數 / Variables: {{code-sample}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Code Style Report Generator for Teams is a free AI prompt that analyzes code samples against language-spec…
