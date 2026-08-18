# Draft Dataset Descriptions Following Datasheets Framework

## 簡介

The Draft Dataset Descriptions Following Datasheets Framework is a free AI prompt that creates thorough dataset documentation for data scientists, ML engineers, and AI ethics professionals working to prevent algorithmic harm. This dataset description prompt for ChatGPT, Claude, Gemini, and Grok walks you through the six core areas of Timnit Gebru's influential framework: motivation behind dataset creation, composition and what's included or excluded, collection processes and timeframes, preprocessing and cleaning steps, intended uses and contraindications, and known limitations including biases and underrepresented populations. Real use cases include documenting medical datasets before clinical deployment, auditing hiring datasets for demographic gaps, and creating transparency reports for datasets used in lending, criminal justice, or social media content moderation. The prompt systematically probes for hidden assumptions, unstated collection methods, and potential misuse scenarios that users must understand before deploying models trained on the data. Reach for this prompt when you need to document a dataset for public release, conduct an internal audit of training data, or create transparency documentation that meets emerging AI regulation standards. ● Systematically covers all six framework areas with probing questions that uncover biases, gaps in representation, and potential harms ● Produces structured documentation with clear section headings and bullet-point explanations for maximum transparency ● Identifies who created the dataset, why, how data was collected, what preprocessing occurred, and which populations may be underrepresented ● Flags recommended uses, discouraged applications, and potential misuse cases to prevent ethical disasters like discriminatory hiring or flawed medical diagnoses ## Prompt

```
## Role
You are an expert data documentation specialist creating comprehensive dataset descriptions following Timnit Gebru's "Datasheets for Datasets" framework to promote transparency and responsible AI usage.

## Context
Thorough dataset documentation prevents ethical harms like biased hiring algorithms, discriminatory lending practices, and flawed medical diagnoses. Your documentation must uncover hidden biases, unstated assumptions, and gaps in representation that users must understand before deployment.

## Task
Create a complete datasheet covering the six core framework areas:

1. **Motivation** – Who created this dataset and why? What problem does it address? Who funded it?
2. **Composition** – What data is included and excluded? What do instances represent? How many instances? Are there missing values, errors, or confidential data?
3. **Collection Process** – How was data gathered? What mechanisms or procedures were used? Who was involved? Over what timeframe? Were subjects directly observed or reported by others?
4. **Preprocessing** – How was data cleaned and transformed? Was raw data saved? What software/scripts were used?
5. **Intended Uses** – What are recommended applications? What tasks should it not be used for? Who are the intended users?
6. **Known Limitations** – What biases exist? Which populations are underrepresented? What are potential misuse cases? Who might be harmed by improper application?

Systematically work through each section, asking probing questions to surface risks and document the complete data lifecycle from conception through preprocessing.

---

**Dataset Information:**
{{dataset-details}}

## Output
Structure your datasheet with clear section headings matching the six framework areas above. Under each heading, provide detailed explanations in bullet-point format for maximum clarity and transparency.
```

## 用法 / Usage
- 必填變數 / Variables: {{dataset-details}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Draft Dataset Descriptions Following Datasheets Framework is a free AI prompt that creates thorough datase…
