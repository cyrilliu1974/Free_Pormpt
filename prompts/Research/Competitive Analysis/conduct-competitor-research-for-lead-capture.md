# Competitor Lead Capture Research Prompt

## 簡介

The Competitor Lead Capture Research Prompt is a free AI prompt that conducts systematic competitive intelligence analysis of how competitors capture leads across digital channels. Acting as a competitive intelligence analyst, it guides ChatGPT, Claude, Gemini, or Grok to examine competitor websites, landing pages, and marketing channels, then deliver findings in a clean markdown table with specific methods and actionable takeaways. This lead capture research prompt for ChatGPT walks through five research stages: identifying main competitors, auditing their web properties, analyzing tactics like forms, pop-ups, content gates, and incentives, evaluating effectiveness against conversion best practices, and extracting insights tailored to your business context. You supply your business context (type, audience, current methods, goals) and a list of competitors; the AI returns a three-column table mapping each competitor to their lead capture tactics and strategic takeaways you can apply immediately. Marketing teams, growth managers, and entrepreneurs use it when planning lead generation campaigns, redesigning opt-in flows, or benchmarking against industry leaders. ● Systematically inventories competitor lead capture tactics including email gates, free trials, lead magnets, chatbots, and exit-intent pop-ups. ● Evaluates each method against user experience and conversion optimization benchmarks to highlight strengths and weaknesses. ● Delivers findings as a markdown table with Competitor Name, Lead Capture Method, and Key Takeaways columns for easy comparison. ● Tailors actionable insights to your specific business context, target audience, and improvement goals. ## Prompt

```
## Role
You are a competitive intelligence analyst specializing in lead capture strategy research.

## Task
Conduct a comprehensive analysis of competitors' lead capture methods and extract actionable insights. Follow this approach:

1. Identify the main competitors in the industry
2. Research each competitor's website, landing pages, and online marketing channels
3. Analyze their lead capture methods: forms, calls-to-action, incentives, pop-ups, content gates, and opt-in mechanisms
4. Evaluate effectiveness based on user experience and conversion optimization best practices
5. Extract key takeaways applicable to the business context

## Context
**Business context:** {{business-context}}
(Include: business type, target audience, current lead capture methods, and goals for improvement)

**Competitors to analyze:** {{competitors}}

## Output
Present your analysis as a markdown table with three columns:

| Competitor Name | Lead Capture Method | Key Takeaways |
|-----------------|---------------------|---------------|

For each competitor, provide:
- **Lead Capture Method:** Specific tactics, tools, and incentives used (e.g., email gates, free trials, lead magnets, chatbots, exit-intent pop-ups)
- **Key Takeaways:** Effectiveness assessment, strengths, weaknesses, and actionable insights for application to the specified business context

Ensure each row is concise yet comprehensive, focusing on differentiated strategies and their strategic value.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}}、{{competitors}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Competitor Lead Capture Research Prompt is a free AI prompt that conducts systematic competitive intellige…
