# Proposal Performance Tracking Table Generator

## 簡介

The Proposal Performance Tracking Table Generator is a free AI prompt that creates structured tables for teams tracking sales proposal outcomes and win rates. This proposal performance tracking prompt for ChatGPT builds a ready-to-use markdown table with five columns - Proposal ID, Client Name, Accepted/Rejected status flags, and actionable Feedback - plus 5-7 realistic sample rows that demonstrate both wins and losses with specific client insights. It runs on ChatGPT, Claude, Gemini, and Grok, automatically generating varied feedback examples like "Pricing 15% above budget" or "Strong case studies sealed the deal" so teams can immediately spot patterns. After the table, the prompt delivers 2-3 analytical observations that highlight trends and suggest strategy adjustments. Sales teams, proposal managers, and business development analysts use it to replace ad-hoc spreadsheets with a consistent tracking format that surfaces what works and what doesn't. ● Creates a five-column markdown table with sequential IDs, client names, win/loss flags, and specific feedback ● Populates 5-7 sample rows illustrating varied outcomes and concrete reasons for acceptance or rejection ● Includes post-table analysis highlighting patterns and recommending future proposal strategy adjustments ● Adapts to any business context you provide, generating relevant client feedback and realistic scenarios ## Prompt

```
## Role

You are an expert data analyst specializing in proposal performance tracking and analysis.

## Task

Create a comprehensive proposal tracking table with starter data that demonstrates best practices for monitoring win rates and extracting actionable insights.

## Context

{{business-context}}

## Output

Deliver a markdown table with these 5 columns:

- **Proposal ID**: Sequential format (P001, P002, etc.)
- **Client Name**: Organization name
- **Accepted**: ✓ for won proposals, ✗ otherwise
- **Rejected**: ✓ for lost proposals, ✗ otherwise  
- **Feedback**: Concise, actionable insights on proposal strengths or improvement areas

Include 5-7 sample rows that illustrate:
- Both accepted and rejected proposals
- Varied, specific feedback (e.g., "Excellent value proposition," "Pricing 15% above budget," "Strong case studies sealed the deal")
- Patterns a user could analyze for trends

Format as a standard markdown table. After the table, provide 2-3 brief observations about patterns visible in the data and how they inform future proposal strategy.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Proposal Performance Tracking Table Generator is a free AI prompt that creates structured tables for teams…
