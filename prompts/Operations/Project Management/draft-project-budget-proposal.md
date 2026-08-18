# Project Budget Proposal Generator for Financial Planning

## 簡介

The Project Budget Proposal Generator for Financial Planning is a free AI prompt that creates detailed project budgets with expense categorization, cost estimation, and phase-based timelines for financial analysts and project managers. This project budget prompt for ChatGPT guides you through systematic budget development by analyzing project scope, identifying direct and indirect costs, estimating expenses using industry benchmarks, and mapping costs to project phases. It runs on ChatGPT, Claude, and Gemini, producing structured budget proposals that include personnel, materials, equipment, services, overhead, and contingency categories. Use it when you need to justify expenses to stakeholders, align budget planning with project objectives, or demonstrate how budget constraints impact scope and approach. ● Systematically categorizes all project expenses including personnel, materials, equipment, services, overhead, and contingency funds ● Estimates costs using market research and industry-standard benchmarks tailored to your specific industry and project duration ● Maps expenses to project lifecycle phases with timing and justification for each major cost item ● Addresses budget constraints explicitly, showing how limitations impact scope and delivery approach ## Prompt

```
## Role
You are an expert financial analyst specializing in project budget development.

## Task
Create a comprehensive project budget proposal that outlines all necessary expenses, resources, and timelines. Analyze the project scope, identify and categorize potential expenses (direct costs, indirect costs, contingencies), estimate costs based on market research and industry standards, and develop a timeline for when expenses will occur throughout the project lifecycle.

## Context
Project: {{project-name}}
Duration: {{project-duration}}
Industry: {{industry}}
Budget constraints: {{budget-constraints}}
Key objectives: {{key-objectives}}

## Process
1. Analyze the project scope and requirements based on the objectives provided
2. Identify all potential expense categories (personnel, materials, equipment, services, overhead, contingencies)
3. Estimate costs for each category using industry benchmarks and market rates
4. Map expenses to project timeline phases
5. Include justifications for major cost items
6. Highlight any budget constraint impacts on scope or approach

## Output
Provide a brief introduction (2-3 sentences) explaining the project and budget approach.

Then present the budget in a markdown table with three columns:
- **Expense Category**: type of cost (e.g., Personnel, Equipment, Materials, Services, Overhead, Contingency)
- **Estimated Cost**: dollar amount or range
- **Notes**: timing, justification, and any assumptions

Conclude with a summary paragraph covering total estimated cost, major cost drivers, risk factors, and how the budget aligns with stated objectives and constraints.
```

## 用法 / Usage
- 必填變數 / Variables: {{budget-constraints}}、{{industry}}、{{key-objectives}}、{{project-duration}}、{{project-name}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Project Budget Proposal Generator for Financial Planning is a free AI prompt that creates detailed project…
