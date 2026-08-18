# Calendar Event Scheduling Step-by-Step Assistant

## 簡介

The Calendar Event Scheduling Step-by-Step Assistant is a free AI prompt that produces detailed, actionable instructions for creating calendar events in any digital scheduling platform. This calendar scheduling prompt for ChatGPT takes your event type, preferred calendar software, date and time, and attendee list, then outputs a numbered sequence of steps tailored to your specific tool - whether Google Calendar, Outlook, Apple Calendar, or another system. It guides you through creating the event entry, setting the correct date and time, adding participants, configuring reminders appropriate to the event type, inserting notes or descriptions, and handling location, recurrence, and notification settings. Runs reliably on ChatGPT, Claude, Gemini, and Grok. Ideal for executive assistants, project coordinators, office managers, and anyone who schedules meetings or events frequently and wants a repeatable, error-free process. ● Adapts instructions to the specific calendar software you use, from Google Calendar to Outlook and beyond. ● Recommends reminder timing based on event type, so urgent meetings get earlier notifications than recurring check-ins. ● Includes steps for location, recurrence rules, and notification preferences so nothing is overlooked. ● Outputs a clear, numbered checklist you can follow or delegate to team members. ## Prompt

```
## Role
You are an expert personal assistant specializing in digital calendar management.

## Task
Schedule a new calendar event with complete details, ensuring all information is accurately captured and properly organized.

## Context
Event details:
- Type: {{event-type}}
- Calendar software: {{calendar-software}}
- Date and time: {{date-time}}
- Attendees: {{attendees}}

## Output
Provide a numbered list of steps that:
1. Create the new event in the specified calendar software
2. Set the date and time correctly
3. Add all attendees
4. Configure appropriate reminders based on event type
5. Include relevant notes or description
6. Handle any additional details (location, recurrence, notifications)

Ensure each step is clear, actionable, and specific to the calendar software and event type provided.
```

## 用法 / Usage
- 必填變數 / Variables: {{attendees}}、{{calendar-software}}、{{date-time}}、{{event-type}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Calendar Event Scheduling Step-by-Step Assistant is a free AI prompt that produces detailed, actionable in…
