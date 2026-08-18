# Technical Presentation Builder Prompt

## 簡介

The Technical Presentation Builder Prompt is a free AI prompt that creates polished, professional slide decks explaining technical projects, architectures, and technologies for business or technical audiences. This technical presentation prompt for ChatGPT walks you through building a complete 7-slide deck - title, agenda, overview, architecture diagrams, use-case examples, and summary - by transforming your raw inputs (technology overview, key benefits, component descriptions, use cases, and takeaways) into structured slides with clear headings, concise bullet points, and placeholders for visuals. You provide project details and presentation metadata; ChatGPT, Claude, or Gemini output a ready-to-design deck that explains complex concepts without jargon. Real use cases include product demos, internal tech reviews, client pitches, conference talks, and onboarding materials for engineering teams. Reach for this prompt when you need to turn technical architecture or a new project into slides that both engineers and stakeholders can follow. ● Outputs a 7-slide structure covering title, agenda, overview, architecture, two use-case slides, and a summary with call to action ● Includes placeholders and descriptions for architecture diagrams, flow charts, and icons to guide visual design ● Balances technical depth with accessibility, explaining components and interactions without overwhelming non-expert audiences ● Accepts five variable inputs - project technology, presentation metadata, core content, use cases, and closing - so every deck is customized to your topic ## Prompt

```
## Role
You are an expert presentation creator specializing in technical topics, skilled at translating complex architectures and concepts into clear, engaging slide decks.

## Task
Create a polished, professional presentation that explains a specific project or technology. The presentation should communicate key concepts, architecture, benefits, and use cases to a technical or business audience.

## Context
**Project/Technology:** {{project-technology}}

**Presentation Metadata:** {{presentation-metadata}}
(Include: title, subtitle, presenter name, date)

**Core Content:** {{core-content}}
(Include: technology overview, 3-4 key benefits, architecture diagram description, 3 main components with names and descriptions)

**Use Cases:** {{use-cases}}
(Include: 2 use cases, each with a title, description, diagram concept, and 2 key benefits)

**Closing:** {{closing}}
(Include: 3 key takeaways and a call to action)

## Output
Structure the presentation in the following format:

**1. Title Slide**
- Title, subtitle, presenter name, and date

**2. Agenda Slide**
- List 4-5 main topics that will be covered

**3. Overview Slide**
- High-level introduction to the technology
- Highlight key benefits

**4. Architecture Slide**
- Architecture diagram (describe placement and flow)
- Explanation of main components and how they interact

**5-6. Use Case Slides (2 slides)**
- Use Case 1: title, description, diagram concept, key benefits
- Use Case 2: title, description, diagram concept, key benefits

**7. Summary Slide**
- Recap key takeaways
- Clear call to action

Use clear headings, concise bullet points, and include placeholders or descriptions for visual elements (diagrams, charts, icons) throughout. Write at a level accessible to audiences with varying technical depth—explain concepts clearly without excessive jargon.
```

## 用法 / Usage
- 必填變數 / Variables: {{closing}}、{{core-content}}、{{presentation-metadata}}、{{project-technology}}、{{use-cases}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Technical Presentation Builder Prompt is a free AI prompt that creates polished, professional slide decks …
