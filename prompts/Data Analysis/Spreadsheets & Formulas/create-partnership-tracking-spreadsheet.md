# Partnership Lead Tracker Spreadsheet Generator

## 簡介

The Partnership Lead Tracker Spreadsheet Generator is a free AI prompt that builds a complete Excel tracking system for businesses managing partnership opportunities. This partnership tracker prompt for ChatGPT creates a six-column spreadsheet with Partner Name, Contact Person, Last Contact Date, Follow-up Status, Lead Temperature, and Notes fields. The prompt configures data validation rules to prevent duplicate entries and enforce date logic, applies conditional formatting that color-codes leads based on temperature (Cold, Warm, Hot) and highlights overdue follow-ups older than 14 days, and embeds formulas that count pending actions and display the current date for reference. Runs on ChatGPT, Claude, Gemini, and Grok with implementation instructions tailored to beginner, intermediate, or advanced Excel users. Reach for this prompt when you need to organize business development pipelines, track outreach cadences, or maintain visibility into partnership conversations without building a spreadsheet structure from scratch. ● Enforces unique partner names and required contact fields through data validation rules ● Auto-highlights leads that have not been contacted in 14+ days and flags pending follow-ups in yellow ● Includes formulas that count pending actions and reference today's date for quick context ● Provides step-by-step setup instructions adjusted to your Excel proficiency level ## Prompt

```
## Role

You are an expert spreadsheet creator specializing in business partnership tracking systems.

## Task

Create a comprehensive Excel "Partnership Lead Tracker" spreadsheet with the structure, validation rules, conditional formatting, and formulas detailed below. Tailor the implementation guidance to {{user-experience-level}}.

## Spreadsheet Structure

**Columns:**

1. **Partner Name** [Text, Bold]
   - Data Validation: Unique values only
   - Conditional Formatting: Highlight green when lead status is "Confirmed Partnership"

2. **Contact Person** [Text, Bold]
   - Data Validation: Required field

3. **Last Contact Date** [Date, Bold]
   - Data Validation: Valid date, no future dates
   - Conditional Formatting: Highlight red if over 14 days old

4. **Follow-up Status** [Dropdown, Bold]
   - Data Validation: "Pending", "Completed", or "Not Required"
   - Conditional Formatting: Highlight "Pending" in yellow

5. **Lead Temperature** [Dropdown, Bold]
   - Data Validation: "Cold", "Warm", or "Hot"
   - Conditional Formatting: Cold=blue, Warm=orange, Hot=red

6. **Notes** [Text, Word Wrap]

**Sheet Formatting:**
- Freeze top row
- Auto-filter on all columns
- Alternating row colors

**Formulas:**
- Cell G2: `=TODAY()` (formatted as Date) for reference
- Cell H2: `=COUNTIFS(D:D,"Pending")` to track pending follow-ups

## Output

Provide step-by-step implementation instructions for {{user-experience-level}}, then explain:

**How to Use:**
1. Enter each partnership lead in a new row with all relevant details
2. Update Last Contact Date and Follow-up Status after each interaction
3. Regularly review Follow-up Status and Lead Temperature columns
4. Sort and filter to prioritize leads
5. Use Notes column to record key details and next steps

Conclude with how this tracker helps stay organized, follow up promptly, and convert leads into partnerships, emphasizing the at-a-glance insights provided by formatting and formulas.
```

## 用法 / Usage
- 必填變數 / Variables: {{user-experience-level}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Partnership Lead Tracker Spreadsheet Generator is a free AI prompt that builds a complete Excel tracking s…
