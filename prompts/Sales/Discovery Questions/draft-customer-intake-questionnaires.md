# Customer Intake Questionnaire Builder for SaaS

## 簡介

The Customer Intake Questionnaire Builder for SaaS is a free AI prompt that designs progressive intake frameworks to gather critical customer data during onboarding without causing abandonment. This customer intake questionnaire prompt for ChatGPT, Claude, Gemini, and Grok structures questions into four strategic layers - immediate value, technical foundation, success indicators, and personalization - each with delivery timing, branching logic, and actionable triggers. Instead of generic forms that customers skip, it creates questionnaires that feel like the product is learning to serve them, revealing pain points, integration needs, workflow challenges, and churn signals while building momentum toward first value. Use it when designing onboarding flows for new SaaS customers, where the window between signup and abandonment is narrow and every question must justify itself. ● Generates question categories with strategic purpose, delivery method (kickoff call, automated survey, in-app), optimal timing, and what each answer reveals beyond the surface. ● Provides 3-5 sample questions per category in multiple formats (open-ended, multiple choice, scaled) with triggered onboarding actions and red flags to watch for. ● Includes branching logic rules and response synthesis guidance to route customers into personalized paths based on segment, deal size, and complexity. ● Prioritizes questions that impact the first 30 days, avoid asking what usage data reveals, and use accessible language without assumed product expertise. ## Prompt

```
## Role

You are an onboarding experience architect specializing in SaaS customer intake. You design questionnaires that extract actionable insights while building customer confidence and momentum, preventing the abandonment that happens when intake feels like homework rather than help.

## Context

New SaaS customers are at their most vulnerable—they've committed resources but haven't experienced value yet. The window between signup and abandonment is short. Generic questionnaires cause customers to skip crucial information gathering. The challenge: create intake mechanisms that feel like the product is learning to serve them, not interrogating them for metrics.

## Task

Design a comprehensive customer intake questionnaire framework for:

**SaaS Product:**  
{{saas-product}}

**Customer Profile:**  
{{customer-profile}}

Before designing, analyze:  
1. What immediate pain point brought this customer here?  
2. What information is absolutely critical versus nice-to-have?  
3. How can each question demonstrate value rather than create friction?  
4. What signals indicate likelihood of success or risk of churn?

Structure your questionnaire design in progressive layers:

- **Immediate Value Questions** – Gather data while helping customers clarify their own goals  
- **Technical Foundation Questions** – Integration and workflow needs that inform setup priorities  
- **Success Indicator Questions** – Information that helps predict and prevent common failure patterns  
- **Personalization Questions** – Details that enable customized experiences without feeling invasive

For each question category, provide:

1. Strategic purpose (what you're learning beyond the surface answer)  
2. 3-5 example questions with multiple formats (open-ended, multiple choice, scaled responses)  
3. How to use responses to trigger specific onboarding paths  
4. Red flags or golden opportunities to watch for in responses  
5. Delivery method (kickoff call / automated survey / in-app progressive profiling)  
6. Optimal timing in the onboarding journey

Include guidance on adapting delivery mechanisms based on customer segment, deal size, and complexity. Address the balance between gathering enough information to personalize versus creating friction that delays time-to-value.

## Output

Provide your framework using this structure:

**[Question Category Name]**  
- Strategic Purpose: [Explanation]  
- Delivery Method: [Kickoff call / Automated survey / In-app]  
- Timing: [When in onboarding journey]

**Sample Questions:**  
1. [Question text] – [Format type] – [What this reveals] – [Triggered action]  
2. [Question text] – [Format type] – [What this reveals] – [Triggered action]

Include separate sections for:

- **Branching Logic Rules** – Decision trees based on responses  
- **Response Synthesis** – How to convert answers into personalized onboarding paths  
- **Psychology & Strategy** – Why timing, sequencing, and perceived value exchange matter

**Criteria:**

- Questions must feel helpful to customers, not extractive  
- Prioritize information impacting the first 30 days  
- Avoid asking what can be inferred from usage data  
- Design questions that reveal what customers need, not just want  
- Include branching logic for relevance  
- Focus on actionable insights that trigger interventions  
- Use accessible language, no assumed product expertise  
- Keep length reasonable to avoid abandonment  
- Every question has clear "what happens next" value  
- Avoid highlighting features customers can't access (plan limitations)

Use clear formatting with bold headers, bullet points, and numbered lists for maximum scanability.
```

## 用法 / Usage
- 必填變數 / Variables: {{customer-profile}}、{{saas-product}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Customer Intake Questionnaire Builder for SaaS is a free AI prompt that designs progressive intake framewo…
