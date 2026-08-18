# Broken Link Audit and SEO Resolution Plan

## 簡介

The Broken Link Audit and SEO Resolution Plan is a free AI prompt that performs a technical broken link audit, assesses SEO impact, and creates a prioritized action plan for website managers and SEO professionals. This broken link audit prompt for ChatGPT systematically identifies every broken link across your website, catalogs where each link appears, evaluates its impact on keyword rankings and SEO performance, and outputs a structured resolution plan with effort estimates and deadlines. The prompt works on ChatGPT, Claude, Gemini, and Grok, delivering four distinct outputs: a broken link report table showing each URL's source page and priority rating (1-5 scale), an SEO impact analysis that highlights critical issues affecting search rankings, a resolution action plan assigning ownership and deadlines, and additional recommendations for link structure improvements, redirects, and navigation enhancements. Real use cases include quarterly site audits, pre-launch website checks, recovery from site migrations, and ongoing maintenance for large content libraries. This prompt is designed for technical SEO specialists, webmasters, digital marketing teams, and anyone responsible for maintaining site health and search visibility. ● Produces a CSV-formatted broken link report table with source pages, keyword impact assessment, and 1-5 priority ratings ● Analyzes how each broken link affects search engine rankings and site authority ● Generates a resolution action plan with assigned owners, effort estimates in hours, and recommended deadlines ● Includes strategic recommendations for redirect chains, internal link architecture, and navigation improvements ## Prompt

```
## Role
You are a technical SEO strategist specializing in broken link analysis and resolution.

## Task
Perform a comprehensive broken link audit on the provided website, assess the SEO impact, and develop a prioritized action plan for resolving the identified issues.

## Context
Website URL: {{website-url}}

{{audit-scope}}

## Audit Criteria
1. Identify all broken links on the website
2. Assess the impact of each broken link on SEO and keyword rankings
3. Prioritize broken links based on SEO impact and urgency
4. Develop clear, actionable resolution steps
5. Recommend improvements to overall link structure and SEO

## Output
Deliver your findings in the following structure:

**Broken Link Report:**
Present as a table with comma-separated values:
Broken Link,Linked From,Keyword Impact,Priority

(Priority scale: 1-5, where 5 is highest)

**SEO Impact Analysis:**
Provide a brief analysis of how the identified broken links impact site SEO performance and keyword rankings. Highlight the most critical issues.

**Resolution Action Plan:**
Present as a table with comma-separated values:
Resolution,Owner,Effort Estimate (hours),Deadline

**Additional Recommendations:**
Provide a bullet point list of SEO recommendations related to link structure, navigation, redirects, and related improvements.
```

## 用法 / Usage
- 必填變數 / Variables: {{audit-scope}}、{{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Broken Link Audit and SEO Resolution Plan is a free AI prompt that performs a technical broken link audit,…
