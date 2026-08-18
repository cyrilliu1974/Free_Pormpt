# Automated XML Sitemap Generator Script for Python

## 簡介

The Automated XML Sitemap Generator Script for Python is a free AI prompt that produces production-ready Python code for maintaining up-to-date XML sitemaps on any website stack. This sitemap automation prompt for ChatGPT walks through building a complete solution: detecting new or modified pages, generating standards-compliant XML sitemaps, and deploying them to your root directory. It runs on ChatGPT, Claude, Gemini, and Grok, outputting detailed sections covering prerequisites, script logic, change detection methods, sitemap generation with external libraries, deployment workflows, scheduling recommendations, and optimization strategies. Web developers and DevOps engineers use it to eliminate manual sitemap maintenance, reduce SEO indexing lag, and ensure every content update propagates immediately to search engines. ● Provides change detection logic that minimizes false positives while catching every new or updated page ● Outputs sitemap generation code using standard libraries that complies with XML sitemap protocol specifications ● Includes deployment instructions for reliably writing the sitemap to your website's root directory ● Suggests scheduling strategies and performance optimizations based on site size and update frequency ## Prompt

```
## Role
You are an expert web developer specializing in automated website maintenance.

## Task
Develop a Python script that automatically updates an XML sitemap whenever new pages are added or existing pages are significantly modified. The script must detect changes, generate an updated sitemap adhering to standard sitemap format, and deploy it to the website's root directory.

## Context
Website stack:
{{website-stack}}

## Requirements
- Accurately identify new pages and significant modifications while minimizing false positives
- Generate standards-compliant XML sitemap including all relevant pages
- Ensure reliable deployment with the sitemap accessible in the root directory
- Optimize for performance and scalability based on site size and complexity

## Output
Provide your solution in the following structure using markdown:

### Prerequisites
List prerequisite software, libraries, and tools needed

### Script Logic
Outline high-level logic and flow, describing key functions and their purposes

### Change Detection Method
Explain the approach for detecting new pages or significant changes to existing pages

### Sitemap Generation
Detail the sitemap generation process, including external libraries used

### Deployment Process
Describe how the script deploys the updated sitemap to the root directory

### Scheduling Recommendations
Recommend automation schedule (daily, weekly, etc.)

### Potential Optimizations
Suggest optimizations or additional features to enhance functionality

Format code snippets with proper indentation for readability.
```

## 用法 / Usage
- 必填變數 / Variables: {{website-stack}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Automated XML Sitemap Generator Script for Python is a free AI prompt that produces production-ready Pytho…
