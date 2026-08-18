# Peer Support Platform Research and Comparison Prompt

## 簡介

The Peer Support Platform Research and Comparison Prompt is a free AI prompt that helps education researchers compile and evaluate student peer support platforms across different education contexts. This peer support platform prompt for ChatGPT guides AI models (ChatGPT, Claude, Gemini, Grok) to research and analyze collaboration tools, study groups, mentorship services, and academic help platforms. It produces a formatted markdown table comparing platform names, key features (matching algorithms, moderation systems, learning resources, accessibility tools), and target audiences. Researchers can specify the education context (K-12, higher education, vocational), area of interest (STEM, humanities, test prep), and desired number of platforms to review. Each entry includes effectiveness assessments based on user reviews and real-world applicability. This prompt is ideal for education administrators, academic support coordinators, institutional researchers, and curriculum developers who need to recommend peer support solutions for specific student populations. ● Evaluates both established and emerging peer support platforms tailored to specific education levels ● Analyzes core functionality including matching algorithms, moderation features, and accessibility tools ● Produces clean markdown tables with aligned columns for platform name, key features, and target audience ● Supports customization by education context, subject area focus, and desired platform count ## Prompt

```
## Role
You are an education researcher specializing in peer support systems and student collaboration tools.

## Task
Research and analyze peer support platforms for students, then compile your findings into a structured comparison table. Evaluate each platform based on effectiveness, user reviews, accessibility, and relevance to the target education context.

## Context
Peer support platforms help students connect with classmates for academic help, mentorship, study groups, and emotional support. Your research should cover platforms appropriate for {{education-context}} and include both established and emerging options. If applicable, prioritize platforms relevant to {{area-of-interest}}.

## Output
Present your findings as a markdown table with three columns:
- **Platform Name**: The service or application name
- **Key Features**: Core functionality, unique offerings, and notable tools (learning resources, matching algorithms, moderation, accessibility features)
- **Target Audience**: Primary user demographic and education level

Include {{platform-count}} platforms. Ensure the table is properly formatted with clear rows and aligned columns.
```

## 用法 / Usage
- 必填變數 / Variables: {{area-of-interest}}、{{education-context}}、{{platform-count}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Peer Support Platform Research and Comparison Prompt is a free AI prompt that helps education researchers …
