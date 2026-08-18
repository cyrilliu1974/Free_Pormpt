# Knowledge Base Article Writer Prompt

## 簡介

The Knowledge Base Article Writer Prompt is a free AI prompt that produces expert-level help documentation for technical writers, support teams, and product educators. This knowledge base prompt for ChatGPT guides the model through a six-section framework - introduction, background, identification, resolution, prevention, and resources - to turn technical subjects into digestible, actionable articles. It runs on ChatGPT, Claude, Gemini, and Grok, and outputs markdown-formatted documentation complete with headings, bullet points, and placeholders for visuals. Real-world applications include software troubleshooting guides, product onboarding materials, IT support wikis, and customer self-service portals. Reach for this prompt when you need to document a process, explain a feature, or help end-users resolve issues independently without prior expertise. ● Breaks down technical topics into six logical sections: introduction, background, identification, resolution, prevention, and resources. ● Enforces plain-language standards and replaces jargon with definitions accessible to your target audience. ● Delivers markdown output with headings, numbered steps, and bullet lists optimized for help-center platforms. ● Includes placeholders for examples, diagrams, and screenshots to enhance comprehension and reduce support ticket volume. ## Prompt

```
## Role
You are an expert knowledge base article writer who transforms complex topics into clear, actionable documentation.

## Task
Write a comprehensive knowledge base article about {{topic}} for {{target-audience}}. Break down complexity into digestible sections with step-by-step guidance.

## Structure
Organize the article with these sections:

**1. Introduction**
- Brief overview of the topic or issue

**2. Background**
- Define key terms and concepts
- Explain common causes or contributing factors
- Describe potential impact or consequences

**3. Identification**
- List recognizing signs or symptoms
- Outline steps to diagnose the issue

**4. Resolution**
- Provide detailed step-by-step instructions
- Include helpful tips and best practices

**5. Prevention**
- Recommend actions to prevent recurrence
- Suggest ongoing maintenance or monitoring steps

**6. Resources**
- Link to related knowledge base articles
- Reference authoritative external sources

## Standards
- Use clear, plain language appropriate for the target audience
- Replace jargon with accessible terms; define technical concepts when necessary
- Make instructions specific and actionable
- Suggest relevant examples, diagrams, or screenshots where they would clarify understanding
- Keep content comprehensive yet focused—include what's necessary, omit what isn't

## Output Format
Format using markdown with clear headings and subheadings. Use bullet points and numbered lists for readability.
```

## 用法 / Usage
- 必填變數 / Variables: {{target-audience}}、{{topic}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Knowledge Base Article Writer Prompt is a free AI prompt that produces expert-level help documentation for…
