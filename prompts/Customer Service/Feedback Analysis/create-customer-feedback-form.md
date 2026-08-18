# Customer Feedback Form Builder for ChatGPT

## 簡介

The Customer Feedback Form Builder is a free AI prompt that creates structured, ready-to-publish feedback forms for any business or product. This feedback form prompt for ChatGPT produces a complete six-section survey that combines rating scales, multiple-choice questions, and open-ended text fields. You provide your target audience and business description, and the prompt generates an introductory paragraph, an overall satisfaction question, three aspect-specific questions tailored to your business, a qualitative feedback section, two demographic questions, and a closing thank-you with next steps. The output is formatted in clean markdown with every question type and answer option explicitly defined, so you can copy it directly into Google Forms, Typeform, SurveyMonkey, or any survey platform. It runs on ChatGPT, Claude, Gemini, and Grok. Reach for this prompt when you need to gather customer insights quickly without designing a form from scratch, whether you are launching a new product, auditing service quality, or measuring customer satisfaction at scale. ● Produces six structured sections: intro, overall satisfaction, three aspect-specific questions, open feedback, demographics, and outro. ● Specifies question type and answer options for every item, making implementation instant. ● Balances rating scales, multiple choice, and text fields to capture both scores and stories. ● Adapts to any industry by tailoring aspect questions to your business description and audience. ## Prompt

```
## Role

You write customer feedback forms. Given a business description and target audience, you produce a ready-to-publish form with a logical section order, a mix of question types, and a brief intro and outro.

## Context

- Target audience: {{target-audience}}
- Business / aspects to collect feedback on: {{business-description}}

## Task

Build a customer feedback form with the six sections below. For each question, specify the question text, question type, and answer options where relevant.

### 1. Intro

A short paragraph explaining the form's purpose and how responses will be used.

### 2. Overall Satisfaction

- Question: Ask about overall satisfaction with the business, product, or service.
- Type: Rating scale or multiple choice.
- Options: List the answer options.

### 3. Specific Aspects (3 questions)

Ask about satisfaction with three distinct aspects of the business. For each:

- Question text for that aspect
- Type: Specify the question type
- Options: List answer options if applicable

### 4. Freeform Feedback

- Question: One open-ended question inviting qualitative feedback.
- Type: Text box.

### 5. Demographic Info (2 questions)

Two demographic questions. For each:

- Question text
- Type: Specify the question type
- Options: List answer options if applicable

### 6. Outro

Thank the respondent. Include any follow-up instructions or next steps.

## Output

- Use markdown headings and bullet points for clear structure.
- Mix question types across the form: use rating scales, multiple choice, and open text.
- Keep each question specific and unbiased.
- Do not ask for sensitive personal information beyond what is needed.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-description}}、{{target-audience}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Customer Feedback Form Builder is a free AI prompt that creates structured, ready-to-publish feedback form…
