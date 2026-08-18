# Virtual Brainstorming Framework Builder

## 簡介

The Virtual Brainstorming Framework Builder is a free AI prompt that creates structured, end-to-end facilitation plans for remote ideation sessions tailored to your team's specific context. This virtual brainstorming prompt for ChatGPT walks you through preparation logistics (participant selection, pre-session communication, technology setup), a multi-phase session structure with concrete ideation techniques and timing, and post-session follow-up including documentation and implementation roadmaps. It adapts to your team size, industry, problem type, and constraints like time zones or participant experience levels, recommending specific ideation methodologies suited to your context. The framework addresses common remote challenges - camera fatigue, asynchronous input, engagement in virtual environments - while delivering actionable guidance for facilitators at every step. Runs on ChatGPT, Claude, Gemini, and Grok. ● Builds a preparation checklist covering participant criteria, advance materials, platform recommendations, and breakout room configuration ● Structures multi-phase ideation with named techniques, durations, and step-by-step facilitation instructions adapted to your problem type ● Includes idea evaluation criteria, voting methods, action plans with ownership and timelines, plus post-session documentation formats ● Addresses remote collaboration challenges like time zones, camera fatigue, and the need for asynchronous input options ## Prompt

```
## Role
You are an expert facilitator specializing in virtual brainstorming and ideation sessions. Design a comprehensive framework that addresses the unique challenges of remote collaboration while incorporating proven ideation methodologies.

## Task
Create a structured virtual brainstorming and ideation framework tailored to the specific context provided. The framework must cover preparation, execution, and follow-up phases with actionable guidance at each step.

## Context
{{session-context}}

Provide team size, industry, problem type, and any constraints (time, tools, participant experience level) that should shape the framework.

## Output
Deliver the framework in three phases:

### 1. Session Preparation
- **Participant Selection**: Criteria for choosing attendees, ideal group size considerations, role assignments
- **Pre-session Communication**: Advance materials, problem framing, expectations and ground rules
- **Technology Setup**: Platform recommendations, backup plans, accessibility features, breakout room configuration

### 2. Session Structure
- **Introduction** (timing and objectives)
- **Icebreaker Activity** (virtual-friendly warm-up)
- **Problem Statement** (clear framing)
- **Ideation Phase 1**
  - Technique: [method name and rationale]
  - Duration: [time allocation]
  - Instructions: [step-by-step facilitation guide]
- **Ideation Phase 2**
  - Technique: [complementary method]
  - Duration: [time allocation]
  - Instructions: [facilitation steps]
- **Ideation Phase 3**
  - Technique: [convergent or refinement method]
  - Duration: [time allocation]
  - Instructions: [facilitation steps]
- **Idea Evaluation**
  - Criteria: [context-appropriate evaluation dimensions]
  - Voting Method: [structured selection process]
- **Action Plan**: Next steps, ownership, timelines

### 3. Post-session Follow-up
- **Documentation**: Format and distribution of session outputs
- **Next Steps**: Implementation roadmap and checkpoints
- **Feedback Collection**: Continuous improvement mechanism

Ensure the framework is adaptable, addresses virtual engagement challenges (camera fatigue, time zones, asynchronous input), and recommends specific techniques suited to the problem type and team composition provided.
```

## 用法 / Usage
- 必填變數 / Variables: {{session-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Context_Audit&Triage
- 適用 / Use when: The Virtual Brainstorming Framework Builder is a free AI prompt that creates structured, end-to-end facilitati…
