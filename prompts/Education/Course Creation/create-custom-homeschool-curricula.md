# Homeschool Curriculum Builder for Any Subject and Grade

## 簡介

The Homeschool Curriculum Builder for Any Subject and Grade is a free AI prompt that compiles research-backed educational resources for homeschooling families planning lessons across any subject and grade level. This homeschool curriculum prompt for ChatGPT takes a subject and grade level as input and produces a structured markdown table listing at least 10 resources spanning textbooks, online courses, educational apps, websites, and hands-on kits. Each entry includes the resource type, cost indicator (free or paid), and a description of its pedagogical approach, interactivity, standards alignment, and unique strengths. The prompt runs on ChatGPT, Claude, and Gemini, and helps parents compare options that fit different learning styles and budgets while maintaining high educational standards. It is ideal for homeschooling parents assembling a year-long curriculum, tutors recommending supplemental materials, or educational consultants building resource lists for client families. ● Outputs a markdown table with resource name, type, cost, and detailed pedagogical features ● Flags highly recommended resources and distinguishes free versus paid options ● Covers multiple formats - textbooks, online courses, apps, websites, and hands-on kits - to suit varied learning preferences ● Designed for any subject and grade level, from elementary math to high-school science to language arts ## Prompt

```
## Role
You are an expert educational consultant specializing in homeschooling curricula across subjects and grade levels.

## Task
Compile a well-researched list of top-quality educational resources for the specified subject and grade level. Include diverse resource types—textbooks, online courses, educational apps, websites, and hands-on materials—that cater to different learning styles and budgets while maintaining high educational standards.

## Context
Subject and grade level: {{subject-and-grade}}

The parent needs resources that span multiple formats and price points to build a comprehensive, adaptable homeschool curriculum.

## Output
Present your findings as a markdown table with these columns:
- **Resource Name** (include ✅ for highly recommended items)
- **Type** (textbook, online course, app, website, kit, etc.)
- **Cost** (use 💰 for paid, 🆓 for free)
- **Key Features** (pedagogical approach, interactivity, alignment with standards, unique strengths)

Provide at least 10 resources. Lead with the title:

📚 **Homeschooling Resources for {{subject-and-grade}}**

End with the legend:

**Legend:**  
✅ = Highly Recommended  
💰 = Paid Resource  
🆓 = Free Resource
```

## 用法 / Usage
- 必填變數 / Variables: {{subject-and-grade}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Homeschool Curriculum Builder for Any Subject and Grade is a free AI prompt that compiles research-backed …
