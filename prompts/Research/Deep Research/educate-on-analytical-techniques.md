# Analytical Technique Research and Implementation Guide

## 簡介

The Analytical Technique Research and Implementation Guide is a free AI prompt that produces structured technical documentation for any statistical or analytical method within a specific research domain. This analytical technique prompt for ChatGPT walks through the theoretical foundations, practical implementation steps, and published literature examples of a chosen methodology. You specify the technique (regression analysis, sentiment analysis, machine learning algorithms, etc.) and the field (healthcare, finance, social sciences, marketing, etc.), and the prompt returns a research-grade overview complete with step-by-step instructions, code snippets, data preparation requirements, and a table of peer-reviewed studies demonstrating real-world applications. It runs on ChatGPT, Claude, and Gemini, adapting to the technical depth required by graduate students, data scientists, and research professionals. Reach for this prompt when you need to learn a new analytical method, document a technique for a research proposal, or understand how a statistical approach has been applied in published studies. ● Covers theory, applications, limitations, and implementation procedures in one structured output ● Includes a table of peer-reviewed case studies with objectives, datasets, and key findings ● Provides code snippets and data preprocessing requirements for hands-on implementation ● Cites sources in academic format with DOI or URL references for verification ## Prompt

```
## Role

You are an expert researcher and data analyst skilled in statistical and analytical methodologies across domains.

## Task

Provide a comprehensive technical overview of {{technique}} as applied in {{field}}, covering theory, implementation, and evidence from the literature.

## Output Structure

### 1. Introduction to {{technique}}
- Definition and key concepts
- Historical background and development

### 2. Applications in {{field}}
- Specific use cases and benefits
- Limitations and considerations

### 3. Implementation Guide
- Data preparation and preprocessing requirements
- Assumptions and prerequisites
- Step-by-step implementation procedure
- Code snippets in appropriate language (if applicable)
  ```
 [language]
 [working example code]
 ```

### 4. Literature Examples

Include at least three peer-reviewed studies using {{technique}} in {{field}}:

| Study | Objective | Dataset | Key Findings |
|-------|-----------|---------|-------------|
| [Citation] | [Research question] | [Data description] | [Main results] |
| [Citation] | [Research question] | [Data description] | [Main results] |
| [Citation] | [Research question] | [Data description] | [Main results] |

### 5. Conclusion
- Summary of key points
- Future directions and emerging developments

### References
Cite all sources in standard academic format with DOI or URL where available.

## Quality Standards

- Provide in-depth technical analysis, not superficial summaries
- Ensure all examples and studies are recent, relevant, and from reputable sources
- Make implementation steps actionable and include realistic code examples
- Ground all claims in cited evidence
```

## 用法 / Usage
- 必填變數 / Variables: {{field}}、{{technique}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Academic_Research_Synthesis_Pipeline · Writing_Quality_Multi_Dimension_Checker
- 適用 / Use when: The Analytical Technique Research and Implementation Guide is a free AI prompt that produces structured techni…
