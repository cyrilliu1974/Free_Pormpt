# Restructure Knowledge Base Taxonomies

## 簡介

The Restructure Knowledge Base Taxonomies prompt is a free AI prompt that redesigns organically-grown help centers into intuitive, customer-centric navigation systems for support teams and content strategists. This knowledge base taxonomy prompt for ChatGPT, Claude, Gemini, and Grok analyzes your existing categories and article structure, then proposes a complete reorganization using card-sorting and findability principles. It delivers a hierarchical outline of parent and child categories named in customer language, a migration table mapping every article from its old location to its new home, and actionable recommendations for splitting bloated articles or merging fragmentary ones. Real-world use cases include cleaning up legacy help centers with overlapping categories, eliminating internal jargon from navigation labels, and reducing time-to-resolution by ensuring first-time visitors reach answers within two clicks. Reach for this prompt when you have a knowledge base that grew organically, customers consistently fail to find answers, or support agents struggle to link the right articles because categories no longer make sense. ● Identifies dumping-ground categories, orphan articles, and confusing overlaps in your current structure ● Proposes category names based on customer search language instead of internal department labels ● Maps every existing article to its new location in a markdown migration table ● Recommends which articles to split for clarity or merge for coherence, with specific findability reasoning ## Prompt

```
## Role

You are an expert Information Architect specializing in knowledge base redesign for high-volume customer support organizations. Your expertise includes card sorting methodologies, findability optimization, and taxonomy design that reduces time-to-resolution for both agents and customers.

## Task

Propose a completely restructured taxonomy that transforms the provided organically-grown knowledge base into an intuitive navigation system where first-time visitors can find answers within two clicks from the homepage.

## Context

The current knowledge base has:
- Articles buried in wrong categories
- Overlapping and confusing category structures
- Categories that no longer serve their purpose
- Navigation patterns that cause customers to consistently fail at finding what they need

You will analyze the existing structure to identify:
- Categories that are too broad (dumping grounds with no coherent focus)
- Categories that are too narrow (fewer than 3 articles)
- Overlapping or confusingly named categories
- Internal jargon or department names instead of customer-centric language

**Company:** {{company-description}}

**Primary customer segments:** {{customer-segments}}

**Most common support topics:** {{support-topics}}

**Maximum top-level categories:** {{max-top-level-categories}}

**Current structure:** {{current-categories-and-articles}}

## Requirements

- Name every category using language customers would actually search for, not internal terminology
- Ensure no category contains fewer than 3 articles
- Avoid organizing by internal departments or organizational structure
- Map each existing article to its new proposed location
- Identify articles that should be split into multiple pieces or merged for better coherence

## Output

Deliver your restructured taxonomy in three sections:

**1. New Taxonomy Outline**

Present as an indented hierarchy:
```
Parent Category
 Subcategory
 Article Title
 Article Title
 Subcategory
 Article Title
```

**2. Migration Summary**

Provide a markdown table:

| Article Title | Old Location | New Location |
|---------------|--------------|---------------|

**3. Article Recommendations**

Bullet-point list of articles to split or merge, with specific reasoning for each recommendation focused on findability and coherence.
```

## 用法 / Usage
- 必填變數 / Variables: {{company-description}}、{{current-categories-and-articles}}、{{customer-segments}}、{{max-top-level-categories}}、{{support-topics}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Restructure Knowledge Base Taxonomies prompt is a free AI prompt that redesigns organically-grown help cen…
