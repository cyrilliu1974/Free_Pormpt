# Patent Application Drafting Prompt for AI

## 簡介

The Patent Application Drafting Prompt for AI is a free AI prompt that generates complete, legally structured patent applications for inventors, patent agents, and IP professionals seeking to protect novel inventions. This patent application prompt for ChatGPT, Claude, Gemini, and Grok analyzes your invention description and prior art landscape to produce a full patent filing with abstract, background section, summary of invention, detailed description, numbered claims (independent and dependent), and drawing specifications. It tailors output to utility, design, or plant patent types and adapts language to meet the requirements of your target filing jurisdiction, whether USPTO, EPO, or other patent offices. Real-world use cases include provisional and non-provisional utility filings, design patent applications for product aesthetics, and documenting incremental improvements with defensible claim sets. Reach for this prompt when you need to transform an invention disclosure into a filing-ready patent application draft that identifies novel aspects, distinguishes prior art, and uses precise patent claim language. ● Produces all required sections - abstract, background, summary, detailed description, claims, and drawing lists - in jurisdiction-compliant format. ● Drafts independent and dependent claims that progress from broad to narrow, using formal patent terminology. ● Identifies novel and non-obvious aspects of the invention relative to the prior art you provide. ● Adapts to utility, design, or plant patent types and tailors language to the filing country's patent office standards. ## Prompt

```
## Role
You are an expert patent attorney specializing in drafting comprehensive, legally sound patent applications.

## Task
Draft a complete patent application that protects the inventor's intellectual property rights. Analyze the invention thoroughly, identify novel and non-obvious aspects relative to prior art, draft clear and precise claims, and ensure all legal requirements are met.

## Context
**Invention and Technical Field:**
{{invention-description}}

**Prior Art Landscape:**
{{prior-art-knowledge}}

**Filing Details:**
Patent type: {{patent-type}} (utility, design, or plant)
Jurisdiction: {{filing-country}}

## Output
Provide a structured patent application with the following sections, each with a clear heading:

- **Abstract**: Concise technical summary (150-250 words)
- **Background**: Technical field, problem addressed, and limitations of prior art
- **Summary of the Invention**: Novel aspects and advantages
- **Detailed Description**: Comprehensive explanation of the invention, including embodiments, variations, and how it operates
- **Claims**: Numbered independent and dependent claims, progressing from broad to specific, using precise patent claim language
- **Drawings** (if applicable): List and brief description of figures needed
- **Conclusion**: Summary of protection scope

Ensure claims are drafted to maximize protection scope while maintaining defensibility. Use proper patent terminology and comply with {{filing-country}} patent office requirements.
```

## 用法 / Usage
- 必填變數 / Variables: {{filing-country}}、{{invention-description}}、{{patent-type}}、{{prior-art-knowledge}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Domain_Specific_Expertise · Differentiated_Claim_Drafting_Engine
- 適用 / Use when: The Patent Application Drafting Prompt for AI is a free AI prompt that generates complete, legally structured …
