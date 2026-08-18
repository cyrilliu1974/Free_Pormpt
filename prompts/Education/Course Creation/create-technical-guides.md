# Technical Guide Builder for Complex Procedures

## 簡介

The Technical Guide Builder for Complex Procedures is a free AI prompt that creates detailed instructional documentation for processes and procedures across any industry. This technical guide prompt for ChatGPT produces a seven-section framework covering introduction, prerequisites, step-by-step instructions, troubleshooting, best practices, safety considerations, and conclusion, with placeholders for visual aids and tiered explanations that serve both beginners and experienced practitioners. Whether you're documenting manufacturing workflows, IT deployment procedures, laboratory protocols, or construction sequences, this prompt runs on ChatGPT, Claude, Gemini, and Grok to deliver consistently structured, jargon-aware technical writing. Reach for it whenever you need to transform expert knowledge into accessible, actionable guides that prevent errors and accelerate learning. ● Produces a consistent seven-part structure (introduction, prerequisites, step-by-step instructions, troubleshooting, best practices, safety, conclusion) so readers always know where to find information ● Identifies where visual aids like diagrams or videos should be inserted, making guides easier to follow and reducing ambiguity ● Balances foundational explanations with expert insights, allowing a single guide to serve novices learning the basics and experienced users optimizing their workflow ● Highlights safety considerations and common pitfalls in dedicated sections, reducing accidents and rework ## Prompt

```
## Role
You are an expert technical writer specializing in creating comprehensive guides for complex processes and procedures across various industries.

## Task
Develop a detailed, step-by-step technical guide that breaks down the process into clear, actionable instructions. The guide must serve readers at multiple skill levels by providing foundational explanations alongside expert insights.

## Context
Process/procedure: {{process-procedure}}

Industry: {{industry}}

Target skill level: {{skill-level}}

## Output
Organize the guide using the following structure:

### 1. Introduction
- Brief overview of the process/procedure
- Importance within the industry
- Who this guide serves

### 2. Prerequisites
- Necessary tools, equipment, and materials
- Required skills or knowledge
- Safety gear and precautions

### 3. Step-by-Step Instructions
- Detailed explanation of each step
- Note where visual aids (images, diagrams, videos) would be helpful
- Tips and best practices for each step

### 4. Troubleshooting
- Common issues and challenges
- Practical solutions and workarounds

### 5. Best Practices and Tips
- Industry-specific best practices
- Expert recommendations for optimizing the process

### 6. Safety Considerations
- Key safety concerns
- Recommended safety measures and protocols

### 7. Conclusion
- Recap of key points
- Encouragement to practice
- Additional resources for further learning

**Writing guidelines:**
- Use clear, concise language
- Explain technical terms when first introduced
- Break complex steps into manageable substeps
- Highlight critical safety points
- Format using markdown with clear headings, subheadings, and bullet points
```

## 用法 / Usage
- 必填變數 / Variables: {{industry}}、{{process-procedure}}、{{skill-level}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Technical Guide Builder for Complex Procedures is a free AI prompt that creates detailed instructional doc…
