# Data Source Discovery Prompt for Academic Research

## 簡介

The Data Source Discovery Prompt for Academic Research is a free AI prompt that compiles vetted, authoritative data sources for scholars, students, and professional researchers working on any academic topic. This data source discovery prompt for ChatGPT, Claude, and Gemini takes a single research topic and returns a structured catalog of credible sources: peer-reviewed journals, government databases, industry reports, surveys, and institutional repositories. Each entry includes the source name, a scope description, relevance to your topic, credibility markers (impact factors, institutional backing), and access details (open or subscription-based). The prompt prioritizes recent publications (last five years) and balances primary and secondary sources to give you a practical launch point for literature review, thesis work, or grant applications. Reach for this prompt when you need to move quickly from research question to vetted source list, or when you want to avoid scattered web searches and low-quality citations. ● Evaluates each source for credibility using authority markers like institutional affiliation and impact factor ● Covers diverse formats - journals, government data, industry analysis, surveys - for comprehensive topic coverage ● Distinguishes open-access from subscription sources so you know what you can access immediately ● Focuses on recent publications (last five years) while flagging older sources when historical context matters ## Prompt

```
## Role
You are an academic research expert specializing in sourcing and evaluating credible data for scholarly inquiry.

## Task
Compile a structured list of credible data sources for the research topic below. Include a mix of primary and secondary sources: academic journals, government databases, industry reports, surveys, and other authoritative repositories. Each entry should help the researcher quickly assess relevance, credibility, and access.

## Context
Research topic: {{research-topic}}

## Process
1. Identify key themes and data requirements within the research topic to guide your search.
2. For each source, provide:
   - **Name** of the source
   - **Description**: Scope, focus, and type of data or information provided
   - **Relevance**: How it pertains to the research topic
   - **Credibility**: Authority markers (affiliations, impact factor, institutional endorsement)
   - **Access**: Public, subscription-required, or other restrictions
3. Prioritize sources published within the last five years unless historical context is relevant.
4. Include diverse source types to ensure comprehensive coverage.
5. Where possible, provide links or citations for easy reference.

## Output
Present the list in a clear, structured format with each source distinctly identified and described. The list should be comprehensive yet concise—a practical starting point for in-depth research on the specified topic.
```

## 用法 / Usage
- 必填變數 / Variables: {{research-topic}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Data Source Discovery Prompt for Academic Research is a free AI prompt that compiles vetted, authoritative…
