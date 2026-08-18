# Stress Management Table Generator

## 簡介

The Stress Management Table Generator is a free AI prompt that produces a structured reference table matching stressors, their impacts, and actionable coping strategies for any specified audience. This stress management table prompt for ChatGPT creates a three-column HTML table that identifies five audience-specific stressors, explains their real-world impacts in clear language, and pairs each with immediately implementable coping techniques. The prompt instructs the AI to act as an expert counselor, focusing on realistic strategies rather than generic advice, and includes a reflection section that guides readers to identify personal stress triggers and commit to one strategy for the week. It runs reliably on ChatGPT, Claude, Gemini, and Grok, making it practical for professionals, students, caregivers, or any group facing specific stress patterns. Use this prompt when you need a quick-reference guide tailored to a particular audience's stressors - whether for wellness workshops, employee resource materials, client handouts, or personal stress audits. ● Produces a five-row HTML table with columns for Stressor, Impact, and Coping Strategy tailored to your specified audience ● Explains each stressor's real-world effects in relatable, non-clinical language ● Provides practical coping strategies that can be started immediately without special resources or training ● Includes a reflective closing section to encourage self-assessment and consistent practice ## Prompt

```
## Role

You are an expert counselor specializing in stress management techniques.

## Task

Create a comprehensive stress management reference table with three columns: Stressor, Impact, and Coping Strategy. Include 5 common stressors that affect {{target-audience}}, clearly explain each stressor's impact, and provide practical, actionable coping strategies.

## Requirements

- Focus on stressors relevant to {{target-audience}}
- Explain impacts in clear, relatable terms
- Provide realistic coping strategies that can be implemented immediately
- Avoid overly complex or unrealistic recommendations

## Output Format

Present your response as an HTML table with this structure:

```html
<table>
<tr>
<th>Stressor</th>
<th>Impact</th>
<th>Coping Strategy</th>
</tr>
<tr>
<td>[stressor]</td>
<td>[impact description]</td>
<td>[actionable strategy]</td>
</tr>
[...4 more rows...]
</table>
```

After the table, include a reflection section that encourages the reader to:

1. Review the table and identify which stressors impact them most frequently
2. Choose one coping strategy to focus on implementing this week
3. Remember that managing stress is a continuous process of self-awareness and proactive effort
4. Be patient and consistent in their stress management practices
```

## 用法 / Usage
- 必填變數 / Variables: {{target-audience}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Stress Management Table Generator is a free AI prompt that produces a structured reference table matching …
