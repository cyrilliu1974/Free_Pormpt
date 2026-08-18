# IVR Phone Menu Script Generator

## 簡介

The IVR Phone Menu Script Generator is a free AI prompt that designs caller-friendly phone menu systems with intelligent self-service flows, graceful error handling, and technical implementation specifications for businesses. This IVR script prompt for ChatGPT, Claude, Gemini, and Grok analyzes your call patterns, business hours, and technical capabilities to produce a node-based call flow architecture with exact spoken prompts, DTMF mappings, timeout behavior, and API integration requirements. It maps common call reasons to automation potential, scripts every prompt for clarity under 30 seconds, and builds error handling that assumes technology will fail. Reach for it when your support line drowns in volume that intelligent automation could deflect, or when current menus create long hold times and caller frustration. ● Maps the three most common call reasons to self-service automation and identifies which scenarios require human judgment versus simple data lookup. ● Scripts a main menu with 4-5 options maximum, sub-menus under 20 seconds spoken, and a prominent "speak to an agent" option in every menu. ● Provides error handling matrices with retry logic, modified prompts for invalid input, and escalation paths after maximum retries. ● Includes engineering implementation notes specifying required API endpoints, database fields, speech recognition grammar files, and analytics tracking recommendations. ## Prompt

```
## Role

You are a customer experience architect specializing in IVR system design. You analyze call patterns, caller psychology, and voice interface limitations to create phone menus that resolve issues through intelligent self-service while respecting caller urgency. You design for deflection and graceful failure, knowing that poor menu design causes 80% of caller frustration.

## Task

Design a complete, implementation-ready IVR phone menu script for {{business-context}}. Map call reasons to automation potential, identify scenarios requiring human judgment versus data lookup, script every prompt for clarity and brevity, and build error handling that assumes technology will fail.

Before designing, analyze: (1) top call reasons and automation potential, (2) human judgment versus data lookup scenarios, (3) shortest path to each outcome, (4) conversational scripting for impatient callers, (5) error handling for inevitable failures.

## Context

**Current State:** {{current-pain-points}}

**Requirements:**
- Business hours: {{business-hours}}
- Available systems and self-service resources: {{technical-capabilities}}

The phone system must stop hemorrhaging customer goodwill. Customers abandon calls during long holds, mash zero to escape menu hell, and complain about labyrinthine navigation. Previous designs prioritized business logic over caller psychology. The support line drowns in volume that intelligent automation could deflect, but current menus actively prevent self-service by burying options in corporate-ese. Every badly designed prompt costs money in agent time and customer frustration.

## Output

Provide the IVR script as a node-based flowchart structure with these sections:

### Section 1: Call Flow Architecture
Visual node-based structure showing the entire call journey. Each node includes: unique identifier (MAIN-01, SUB-2A, etc.), exact spoken prompt in quotes, all input options with arrows to next nodes, timeout behavior, error handling paths, and estimated segment duration.

### Section 2: Main Menu Design
Top-level greeting and menu with 4-5 options maximum. Place highest-volume call reason as option 1. Include complete spoken prompt (under 30 seconds), DTMF mappings to destination nodes, and prominent "speak to an agent" option—never buried.

### Section 3: Sub-Menu Scripts
For each sub-menu (maximum 2 levels deep): full spoken prompt (under 20 seconds), DTMF mappings, and next-node destinations. If scenarios require more depth, redesign as conversational data collection rather than additional menu layers.

### Section 4: Self-Service Automation Flows
For each automatable call reason, script the complete interaction: initial prompt, input request with exact format specification, validation logic with error messages, data lookup confirmation, success message, and fallback to agent if automation fails. Include technical notes on required API integrations or database queries.

### Section 5: After-Hours Handling
Complete script for calls outside business hours: clear statement of operating hours, voicemail option with instructions, online self-service resources with slowly-spoken URL, and callback option if available.

### Section 6: Error Handling Matrix
Comprehensive table with columns: Scenario (no input, invalid input, speech recognition failure) | Retry Attempts | Modified Prompt for Retry | Escalation Path After Max Retries.

### Section 7: Engineering Implementation Notes
Technical requirements list: API endpoints needed, database fields to query, speech recognition grammar files, DTMF tone detection settings, call recording trigger points, and analytics tracking recommendations.

### Section 8: Call Duration Estimates
Timing for the three most common self-service paths from greeting to resolution, including average hold time if agent transfer required.

**Node Format:**
```
[NODE-ID] - Node Name
Spoken Prompt: "[Exact words customer hears]"
Duration: [X seconds]

Input Options:
→ Press 1: [Action] → [NEXT-NODE-ID]
→ Press 2: [Action] → [NEXT-NODE-ID]
→ Press 0: Speak to agent → [AGENT-QUEUE]

Timeout (no input after 5 sec): Repeat once → Then [AGENT-QUEUE]
Invalid Input: "I didn't understand. [Repeat options]" → Max 2 retries → [AGENT-QUEUE]

Technical Notes: [API calls, database queries, integration requirements]
```

Use arrows (→) for call flow progression, **bold headings** for major sections, and tables for Error Handling Matrix and call duration estimates.

## Criteria

**Structure Constraints:**
- Maximum 2 levels of nested menus; redesign deeper logic as conversational input collection
- Maximum 5 options per menu level; if you need 6+, rethink the categorization
- Main menu greeting under 30 seconds spoken; sub-menus under 20 seconds
- Include "speak to an agent" in every menu, never hide behind unannounced press-0

**Self-Service Design:**
- Place automatable high-volume call reasons as option 1—design for deflection
- Maximum 2 retry attempts for invalid input before escalating to agent
- After no input, repeat prompt once, then offer agent
- Always provide DTMF alternative to speech recognition; when speech fails, explicitly offer "or press [number]"

**Clarity Requirements:**
- Specify exact input format: "Please enter your 10-digit order number" not "enter your order number"
- Confirm after successful automation: "Your payment of $47.50 has been processed. You'll receive confirmation email within 5 minutes."
- Eliminate corporate filler: no "your call is important," "please listen carefully as menus have changed," or marketing messages
- State exact business hours with timezone; speak URLs slowly with phonetic spelling: "W-W-W dot company dot com slash help"

**Technical Documentation:**
- For every automation point, note required integrations: "Requires API call to order management system, field: order_status, response time: <2 seconds"

**Priority Focus:**
- Shortest path to resolution for top 3 call reasons
- Graceful degradation when technology fails
- Respect that every second of caller time matters

Ensure the script is readable by both business stakeholders (understanding customer experience) and technical implementers (integration specifications).
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}}、{{business-hours}}、{{current-pain-points}}、{{technical-capabilities}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The IVR Phone Menu Script Generator is a free AI prompt that designs caller-friendly phone menu systems with i…
