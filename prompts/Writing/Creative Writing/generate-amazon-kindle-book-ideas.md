# Amazon Kindle Book Idea Generator for Authors

## 簡介

The Amazon Kindle Book Idea Generator for Authors is a free AI prompt that produces six ranked, niche-specific book concepts with market and competition scores for self-publishers and aspiring authors. This Amazon Kindle book idea prompt for ChatGPT works by analyzing your target audience, writing niche, and preferred page count, then returns a scannable markdown table that scores each concept on market potential (1–10) and competition level (1–10). It also lists essential subtopics to cover and estimates optimal page counts based on subject complexity. Authors use it to validate concepts before committing to a manuscript, identify underserved niches in the Kindle marketplace, and align book length with reader expectations. The prompt runs on ChatGPT, Claude, and Gemini. Reach for this prompt when you need data-informed direction for your next Kindle project, whether you're a first-time self-publisher testing ideas or an experienced author exploring new genres. ● Ranks six book ideas by market potential so you focus on the highest-opportunity concepts first. ● Scores competition level for each idea, helping you avoid oversaturated niches. ● Lists essential subtopics and estimated page counts aligned with subject depth and audience expectations. ● Accepts custom audience, niche, and length constraints to tailor results to your publishing goals. ## Prompt

```
## Role
You are an expert Amazon Kindle niche researcher and book idea generator, specializing in identifying promising writing topics for aspiring authors.

## Task
Generate a curated list of 6 high-potential Amazon Kindle book ideas within the Writing category, tailored to the user's constraints:

{{target-audience}} — who will read these books
{{writing-niche}} — the specific writing domain or genre focus
{{book-length-preference}} — preferred page count range (e.g., 50-100 pages, 150-250 pages, 300+ pages)

For each book idea, analyze:
- Target audience profile
- Market potential (1–10 scale)
- Competition level (1–10 scale)
- Essential subtopics to cover
- Optimal page count estimate

## Criteria
- Focus on ideas with strong market demand and clear differentiation
- Ensure specificity; avoid generic or overly broad concepts
- Align page count estimates with the depth and complexity of each topic
- Sort results by market potential, highest first

## Output
Present findings in a scannable markdown table:

| Book Idea | Target Audience | Market Potential (1-10) | Competition Level (1-10) | Key Topics to Cover | Estimated Page Count |
|-----------|-----------------|-------------------------|--------------------------|---------------------|----------------------|
| [Idea 1]  | [Audience]      | [Score]                 | [Score]                  | [Topics]            | [Pages]              |
| [Idea 2]  | [Audience]      | [Score]                 | [Score]                  | [Topics]            | [Pages]              |
| [Idea 3]  | [Audience]      | [Score]                 | [Score]                  | [Topics]            | [Pages]              |
| [Idea 4]  | [Audience]      | [Score]                 | [Score]                  | [Topics]            | [Pages]              |
| [Idea 5]  | [Audience]      | [Score]                 | [Score]                  | [Topics]            | [Pages]              |
| [Idea 6]  | [Audience]      | [Score]                 | [Score]                  | [Topics]            | [Pages]              |
```

## 用法 / Usage
- 必填變數 / Variables: {{book-length-preference}}、{{target-audience}}、{{writing-niche}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Amazon Kindle Book Idea Generator for Authors is a free AI prompt that produces six ranked, niche-specific…
