# Website SEO Readability Audit Prompt

## 簡介

The Website SEO Readability Audit Prompt is a free AI prompt that analyzes webpage content for keyword optimization, placement strategy, and readability metrics to help marketers, content creators, and SEO specialists improve their on-page performance. This website SEO readiness prompt for ChatGPT examines your target URL and returns scored assessments of your top three keywords (density rated 1-5), verifies keyword placement across title tags, meta descriptions, headings, alt text, and body content, then calculates four industry-standard readability scores: Flesch Reading Ease, Flesch-Kincaid Grade Level, Gunning Fog Index, and SMOG Index. The output includes a prioritized table of improvement recommendations that address specific issues with concrete fixes, plus an overall SEO content score out of 100. Real use cases include auditing blog posts before publication, diagnosing why a landing page underperforms in search, and ensuring technical documentation remains accessible to its intended audience. Reach for this prompt when you need a structured, repeatable content audit that goes beyond basic keyword counting to evaluate how readable and SEO-friendly your pages truly are. ● Scores the top three keywords on a 1-5 density scale and checks their presence in title tags, meta descriptions, headings, alt text, and body copy ● Calculates four readability metrics (Flesch Reading Ease, Flesch-Kincaid Grade Level, Gunning Fog Index, SMOG Index) to ensure content matches audience comprehension levels ● Outputs a structured table of current issues and specific fixes, avoiding generic advice ● Provides an overall SEO content score out of 100 for quick benchmarking and progress tracking ## Prompt

```
## Role
You are an expert SEO and content readability analyst.

## Task
Analyze the content at {{website-url}} for SEO best practices, focusing on keyword density, placement, and readability. Deliver a comprehensive audit with summary scores and actionable improvement recommendations.

## Analysis Framework

**Keyword Density:**  
Identify the top 3 keywords and score their density on a scale of 1-5, ensuring they are used naturally and strategically throughout the content.

**Keyword Placement:**  
Evaluate presence (✓ or ✗) in:  
- Title tags  
- Meta descriptions  
- Headings (H1, H2, etc.)  
- Alt text  
- Body content

**Readability Scores:**  
Calculate:  
- Flesch Reading Ease (/100)  
- Flesch-Kincaid Grade Level  
- Gunning Fog Index  
- SMOG Index

Ensure the content is accessible and engaging for the target audience.

**Improvement Recommendations:**  
Provide concise, actionable fixes—avoid vague or generic advice.

## Output

**SEO Content Analysis Results:**

**Keyword Density:**  
[Keyword 1]: [Score]/5  
[Keyword 2]: [Score]/5  
[Keyword 3]: [Score]/5

**Keyword Placement:**  
Title Tags: [✓/✗]  
Meta Descriptions: [✓/✗]  
Headings (H1, H2, etc.): [✓/✗]  
Alt Text: [✓/✗]  
Body Content: [✓/✗]

**Readability Scores:**  
Flesch Reading Ease: [Score]/100  
Flesch-Kincaid Grade Level: [Grade Level]  
Gunning Fog Index: [Index]  
SMOG Index: [Index]

**Improvement Recommendations:**

| Area | Current Issue | Suggested Fix |
|------|---------------|---------------|
| [Issue 1] | [Description] | [Recommendation] |
| [Issue 2] | [Description] | [Recommendation] |
| [Issue 3] | [Description] | [Recommendation] |

**Overall SEO Content Score:** [Score]/100
```

## 用法 / Usage
- 必填變數 / Variables: {{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Website SEO Readability Audit Prompt is a free AI prompt that analyzes webpage content for keyword optimiz…
