# Meeting Notes Action Plan Generator

## 簡介

The Meeting Notes Action Plan Generator is a free AI prompt that converts unstructured meeting notes into organized, trackable action plans for managers, team leads, and project coordinators. This meeting notes prompt for ChatGPT analyzes transcripts or written notes to extract action items, decisions, and follow-up tasks, then organizes them into a structured format with clear ownership, deadlines, and task dependencies. It works across ChatGPT, Claude, Gemini, and Grok to transform conversational meeting records into actionable project plans. Teams use it after stand-ups, planning sessions, client calls, and retrospectives to ensure nothing falls through the cracks and every decision is documented with next steps. Reach for this prompt when you need to turn meeting discussions into accountability structures, prevent post-meeting confusion about who owns what, or create a single source of truth for project commitments made during group discussions. ● Categorizes meeting content into Action Items, Decisions Made, and Follow-Up Tasks with clear separation ● Assigns responsibility and realistic deadlines to every task based on complexity and context ● Identifies task dependencies and prerequisites to prevent execution bottlenecks ● Outputs table or list format that integrates easily into project tracking tools and team workflows ## Prompt

```
## Role

You are an expert in organizational productivity specializing in meeting management and task tracking.

## Task

Analyze the meeting notes to extract and organize all action items, decisions, and follow-up tasks into a structured action plan. Ensure no critical detail is overlooked. Identify dependencies between tasks to prevent bottlenecks and streamline execution.

## Process

1. Read through the meeting notes carefully to identify all tasks, decisions, and items requiring action or clarification.
2. Categorize the information into three sections: **Action Items**, **Decisions Made**, and **Follow-Up Tasks**.
3. For each **Action Item**:
   - Define the task clearly
   - Assign a responsible person or team
   - Set a realistic deadline based on complexity and dependencies
   - Identify and highlight any dependencies or prerequisites
4. For **Decisions Made**:
   - List each decision clearly
   - If a decision requires additional actions (e.g., communication to other departments), specify this as an action item
5. For **Follow-Up Tasks**:
   - Detail the task and its purpose
   - Assign a responsible party
   - Schedule any necessary follow-up meetings or check-ins to review progress
6. Suggest a brief kickoff meeting or email to align all parties on responsibilities and timelines.

## Context

Meeting notes:
{{meeting-notes}}

## Output

Provide a detailed, structured action plan formatted as a table or organized list that includes:

- **Action Items** with assigned responsibilities, deadlines, and dependencies
- **Decisions Made** during the meeting
- **Follow-Up Tasks** with responsible parties and deadlines

The plan must be clear, actionable, and easy to update and track over time.
```

## 用法 / Usage
- 必填變數 / Variables: {{meeting-notes}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Meeting Notes Action Plan Generator is a free AI prompt that converts unstructured meeting notes into orga…
