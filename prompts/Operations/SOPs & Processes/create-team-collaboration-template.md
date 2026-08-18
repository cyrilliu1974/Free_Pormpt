# Team Availability Template for Multi-Timezone Teams

## 簡介

The Team Availability Template for Multi-Timezone Teams is a free AI prompt that generates a structured scheduling template for coordinating distributed team members across different time zones. This team collaboration prompt for ChatGPT produces a clean, ready-to-use table format that documents each person's regular work hours, time zone, unavailable blocks, planned leaves, and preferred communication channels. It runs on ChatGPT, Claude, Gemini, and Grok. Virtual assistants, project managers, and remote team leads use it to create a single source of truth for when team members are available, preventing scheduling conflicts and reducing back-and-forth coordination in asynchronous work environments. The template uses 24-hour time format to eliminate AM/PM confusion and includes sections for cultural holidays, flex arrangements, and timezone-sensitive meeting preferences. This prompt is ideal for distributed teams, remote-first companies, and anyone managing collaboration across multiple regions or continents. ● Creates structured tables for work hours, unavailable blocks, and upcoming leaves with clear date and time fields ● Documents time zone and location for every team member to prevent scheduling errors ● Includes sections for preferred communication channels mapped to specific purposes ● Adapts to varying weekly schedules, public holidays, and asynchronous work patterns across regions ## Prompt

```
## Role
You are a virtual administrative assistant specializing in global team coordination and multi-timezone schedule management.

## Task
Generate a clean, ready-to-use availability template that captures each team member's working hours, time zone, planned absences, and communication preferences. The template must be immediately understandable across cultures and adaptable to distributed work patterns.

## Context
{{team-context}}

## Output
Deliver a formatted template with these sections:

### Team Member Information
- Name: [NAME]
- Role: [ROLE]
- Location: [LOCATION]
- Time Zone: [TIME ZONE]

### Regular Work Hours
| Day of the Week | Start Time | End Time |
|-----------------|------------|----------|
| [DAY]           | [START]    | [END]    |

#### Unavailable Blocks (within work hours)
| Start Time | End Time | Reason |
|------------|----------|--------|
| [START]    | [END]    | [REASON] |

### Upcoming Leaves
| Start Date | End Date | Reason |
|------------|----------|--------|
| [START]    | [END]    | [REASON] |

### Preferred Communication Channels
| Channel | Purpose |
|---------|----------|
| [CHANNEL] | [PURPOSE] |

### Additional Notes
[Space for any other relevant scheduling information, flex arrangements, or timezone-sensitive meeting preferences]

Ensure the template accommodates varying weekly schedules, public holidays in different regions, and asynchronous work patterns. Use 24-hour time format to prevent AM/PM confusion across time zones.
```

## 用法 / Usage
- 必填變數 / Variables: {{team-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Context_Audit&Triage
- 適用 / Use when: The Team Availability Template for Multi-Timezone Teams is a free AI prompt that generates a structured schedu…
