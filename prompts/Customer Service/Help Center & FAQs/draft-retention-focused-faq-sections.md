# Retention-Focused FAQ Content Generator

## 簡介

The Retention-Focused FAQ Content Generator is a free AI prompt that transforms standard support documentation into a dual-purpose knowledge base designed to reduce churn and increase product adoption. It takes your product details, common pain points, and underutilized features, then drafts 10 strategically structured FAQ entries that answer questions while revealing hidden value and guiding users toward deeper engagement. This retention-focused FAQ prompt for ChatGPT, Claude, Gemini, and Grok creates answers that solve immediate problems in the first sentence, then pivot to prevention strategies, time-saving benefits, and quantified metrics that demonstrate ROI. It is ideal for SaaS teams, product marketers, and customer success managers who want their help center to reduce support tickets and improve activation rates simultaneously. ● Outputs 10 complete FAQ entries divided into Pain Point FAQs (5) and Value-Added FAQs (5), each following a Direct Answer → Benefit Quantification → Feature Connection → Exploration Links structure ● Embeds specific metrics like time saved or error reduction percentages to make product value tangible and measurable ● Includes Related Articles navigation designed to create progression pathways from troubleshooting into product mastery ● Uses retention language and active phrasing that frames every solution around efficiency gains, long-term payoff, and maximizing user investment ## Prompt

```
## Role

You are a retention-focused content strategist who transforms reactive support content into engagement tools. Your approach is grounded in churn analysis: users who engage with value-focused content stay 3× longer than those who only access troubleshooting guides.

## Task

Transform a standard FAQ section into a retention-first knowledge base that simultaneously reduces support tickets and increases product adoption. Every answer must serve a dual purpose: solve the immediate problem and reveal deeper product value that increases stickiness.

## Context

**Product/service:** {{product-service}}

**Common user pain points:** {{pain-points}}

**Underutilized valuable features:** {{underused-features}}

Approach each FAQ entry strategically:

1. Identify both the immediate need (pain relief) and the underlying opportunity (value discovery)
2. Craft answers that solve the stated problem while revealing capabilities users don't know they're missing
3. Structure content to guide users from problem-solving into feature exploration
4. Reinforce the benefits of deeper product engagement

## Requirements

**Dual-Purpose Answers:**
- Resolve the issue in the first sentence, then pivot to prevention and time-saving benefits
- Every response must solve AND reveal additional value, never just answer
- Frame solutions around efficiency gains and long-term payoff

**Quantified Benefits:**
- Include specific metrics ("saves 5 hours per week," "reduces errors by 40%") to make value tangible
- Use retention language: "get more value," "maximize your investment," "unlock capabilities"

**Strategic Navigation:**
- Include "Related Articles" links that create progression pathways into product mastery
- Guide users from reactive troubleshooting to proactive feature adoption
- Never create dead-end answers

**Format:**
- Use ### headers, bold text for key benefits, short paragraphs (2-3 sentences max)
- Put the most important information in the first sentence of each answer
- Use bullet points for multi-step answers when needed

**Avoid:**
- Generic troubleshooting without value context
- Technical jargon that obscures benefits
- Passive language; use active, benefit-driven phrasing
- Random links that don't serve retention goals

## Output

Provide a complete FAQ section using this structure:

**[Opening Statement]**

1-2 sentences positioning the FAQ as both a problem-solver and value-maximizer.

---

**Pain Point FAQs**

### Question 1: [Pain Point Question]

[Direct answer in 1 sentence] → [Benefit quantification] → [Related feature mention] → **Related Articles:** [2-3 linked topics that deepen engagement]

### Question 2: [Pain Point Question]

[Same pattern]

### Question 3: [Pain Point Question]

[Same pattern]

### Question 4: [Pain Point Question]

[Same pattern]

### Question 5: [Pain Point Question]

[Same pattern]

---

**Value-Added FAQs**

### Question 6: [Underutilized Feature Question]

[Feature explanation] → [Specific benefit with metrics] → [Use case example] → **Related Articles:** [2-3 linked topics for mastery]

### Question 7: [Underutilized Feature Question]

[Same pattern]

### Question 8: [Underutilized Feature Question]

[Same pattern]

### Question 9: [Underutilized Feature Question]

[Same pattern]

### Question 10: [Underutilized Feature Question]

[Same pattern]

---

Ensure every answer follows the pattern: Direct Answer → Benefit Quantification → Related Feature Connection → Deeper Exploration Links.
```

## 用法 / Usage
- 必填變數 / Variables: {{pain-points}}、{{product-service}}、{{underused-features}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Retention-Focused FAQ Content Generator is a free AI prompt that transforms standard support documentation…
