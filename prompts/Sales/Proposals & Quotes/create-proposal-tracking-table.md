# Proposal Revision Tracking Table Generator

## 簡介

The Proposal Revision Tracking Table Generator is a free AI prompt that creates standardized four-column tables for monitoring client proposal changes and submission history. This proposal tracking prompt for ChatGPT transforms your proposal data into clean ASCII tables with unique identifiers, client names, original submission dates, and revision dates. The prompt enforces consistent YYYY-MM-DD date formatting and builds a clear visual structure that works in any text environment. Teams managing multiple client proposals use it to maintain an at-a-glance view of proposal lifecycles, revision frequency, and client engagement timelines. It runs on ChatGPT, Claude, Gemini, and Grok. Reach for this prompt when you need to organize proposal revision data into a format that your team can read, share, and update without specialized software. ● Outputs ASCII tables with four columns: Proposal ID, Client, Original Submission, and Date of Revision ● Enforces YYYY-MM-DD date formatting for consistency across all entries ● Automatically scales to accommodate any number of proposal records ● Produces plain-text tables that work in emails, documentation, and version control systems ## Prompt

```
## Role
You are a data architect designing an efficient table structure for tracking proposal revisions.

## Task
Create a 4-column table that monitors client proposal changes over time. The table must include:
- **Proposal ID**: Unique identifier (sequential number or descriptive code)
- **Client**: Client name associated with the proposal
- **Original Submission**: Initial proposal submission date
- **Date of Revision**: Most recent revision date

## Context
The table will provide a clear overview of {{proposal-data}}, enabling effective tracking of proposal progress and changes across multiple client engagements.

## Output
Deliver the table in ASCII format using consistent YYYY-MM-DD date formatting:

```
+-------------+----------------+---------------------+------------------+
| Proposal ID | Client | Original Submission | Date of Revision |
+=============+================+=====================+==================+
| | | | |
+-------------+----------------+---------------------+------------------+
| | | | |
+-------------+----------------+---------------------+------------------+
| | | | |
+-------------+----------------+---------------------+------------------+
| | | | |
+-------------+----------------+---------------------+------------------+
```

Populate all rows with the provided proposal information. Add rows as needed to accommodate all revisions.
```

## 用法 / Usage
- 必填變數 / Variables: {{proposal-data}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Proposal Revision Tracking Table Generator is a free AI prompt that creates standardized four-column table…
