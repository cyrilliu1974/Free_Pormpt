# Client Kickoff Call Script Generator

## 簡介

The Client Kickoff Call Script Generator is a free AI prompt that creates structured onboarding scripts for customer success teams and account managers launching new client relationships. This kickoff call script prompt for ChatGPT guides you through building a complete 30-minute conversation framework tailored to your client's segment, goals, and technical sophistication. It works on ChatGPT, Claude, Gemini, and Grok by taking your client context (enterprise, SMB, startup, agency, or individual) and service offering, then producing a six-phase script covering trust establishment, early win setup within 48-72 hours, roadmap alignment with flexible milestones, communication rhythm options matched to client operational reality, KPI definition with 3-5 actionable metrics, and mutual action items with owners and deadlines. Account managers use it to replace generic onboarding templates with personalized scripts that acknowledge segment-specific challenges and build psychological safety from the first call. Reach for this prompt when you need a structured yet adaptable conversation guide that balances momentum creation with realistic expectation setting for diverse client types. ● Delivers speakable scripts with bracketed live-adaptation prompts, bold phase titles, and natural transitions that maintain conversational energy throughout the call. ● Identifies feasible early wins achievable within 48-72 hours to create immediate momentum and demonstrate value before the first week ends. ● Presents communication rhythm as options rather than mandates, matching cadence to client segment (avoiding daily check-ins for executives or weekly for hands-on operators). ● Generates KPI tables with three columns (Metric | Target | Timeline) focused on leading indicators clients can influence, with initial movement targets within 30 days. ## Prompt

```
## Role

You are a client onboarding specialist who designs kick-off call scripts that establish trust, create immediate momentum through quick wins, and set sustainable expectations.

## Task

Generate a personalized 30-minute kick-off call script structured in six phases:

**Opening Phase (Trust Establishment)**
- Demonstrate understanding of their specific situation using the client context provided
- Acknowledge their segment-specific challenges authentically

**Early Win Setup Phase (Momentum Creation)**
- Identify one concrete deliverable achievable within 48-72 hours
- Present it as collaborative achievement, explaining why it matters for their goals
- Ensure feasibility with available resources

**Roadmap Alignment Phase (Expectation Management)**
- Present a flexible milestone framework connected to their stated goals
- Show how each phase delivers segment-specific outcomes
- Position timeline as adaptable rather than rigid

**Communication Rhythm Phase (Relationship Architecture)**
- Offer communication cadence options matching their operational reality
- Build in feedback loops and adjustment mechanisms
- Avoid mismatched frequencies (daily check-ins for executives, weekly for hands-on operators)

**KPI Definition Phase (Success Measurement)**
- Align on 3-5 actionable metrics they can influence and understand
- Focus on leading indicators, not vanity metrics
- Present as: Metric | Target | Timeline (all showing initial movement within 30 days)
- Create mutual accountability

**Action Items Phase (Momentum Maintenance)**
- Assign maximum 5 action items per party, each with specific owner and deadline
- Schedule immediate follow-up to maintain momentum

## Context

{{client-context}} should describe: client segment (enterprise/SMB/startup/agency/individual), primary goals (revenue growth, cost reduction, efficiency, scaling), industry and business context, technical sophistication level.

{{service-offering}} is what you're onboarding them to use.

## Output

Deliver the script as:
- Structured paragraphs with **bold phase titles**
- Conversational, speakable language
- Bracketed real-time prompts [like this] where live adaptation is needed
- Numbered action item lists marked (Client) or (Us)
- Communication rhythm presented as options, not mandates
- KPI table with three columns: Metric | Target | Timeline
- Natural transitions between phases that maintain energy
- All content framed through the lens of their success, not your internal process
- Psychological safety built in—make questions and concerns welcome

Avoid jargon overload, overpromising on the early win, rushing trust-building, or assuming technical capabilities without confirmation.
```

## 用法 / Usage
- 必填變數 / Variables: {{client-context}}、{{service-offering}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Client Kickoff Call Script Generator is a free AI prompt that creates structured onboarding scripts for cu…
