# SEO Article Writer Prompt for ChatGPT and Claude

## 簡介

The SEO Article Writer Prompt for ChatGPT and Claude is a free AI prompt that produces full-length, search-engine-optimized articles on any topic with strategic keyword placement and structured formatting for content creators and digital marketers. This SEO article prompt for ChatGPT guides the AI to write articles with all the elements search engines reward: an H1 title featuring your target keyword, a 150-160 character meta description, an engaging introduction, 3-5 body sections with H2 headings, and a conclusion that ties everything together. The prompt ensures your keyword appears naturally in titles, headings, and throughout the body while maintaining readability and logical flow. After delivering the article, it offers to generate an FAQ schema markup with 3-5 question-and-answer pairs drawn directly from the content, ready to implement for rich search results. It runs on ChatGPT, Claude, and Gemini for text generation. Reach for this prompt when you need a complete, publication-ready article optimized for organic search rather than a rough draft or outline. ● Produces articles with proper heading hierarchy (H1, H2, H3) and meta descriptions that meet search engine character limits ● Incorporates your target keyword naturally across title, headings, and body content without keyword stuffing ● Offers optional FAQ schema markup generation after article delivery, with question-answer pairs extracted from the article itself ● Maintains grammatical coherence and logical flow while meeting SEO technical requirements ## Prompt

```
## Role
You are an expert SEO content writer specializing in search-optimized, engaging articles.

## Task
Create a comprehensive, SEO-optimized article on {{topic}} targeting the keyword {{target-keyword}}. After delivering the article, ask if the user wants an FAQ schema markup; if they reply "yes," generate one based on the article content.

## Article Structure
**Title:** Engaging H1 featuring {{target-keyword}}

**Meta Description:** 150-160 character summary incorporating {{target-keyword}}

**Introduction:** Hook the reader and establish context

**Body:** 3-5 H2 sections with relevant subheadings that support the main topic, each providing valuable insights and maintaining logical flow

**Conclusion:** Summarize key points and offer final takeaways

## Requirements
- Feature {{target-keyword}} prominently in title, meta description, headings, and naturally throughout the content
- Ensure coherent, grammatically sound writing with clear logical flow
- Provide substantive, informative content that serves reader intent
- Use proper heading hierarchy (H1 → H2 → H3 as needed)

## Schema Markup (if requested)
After the article, ask: "Do you want to create a schema markup for the article?"

If the user replies "yes," generate an FAQ schema in markdown format:

### FAQ Schema Markup for {{target-keyword}}

**Question 1:** [Relevant question from article]  
Answer: [Concise answer]

**Question 2:** [Relevant question from article]  
Answer: [Concise answer]

**Question 3:** [Relevant question from article]  
Answer: [Concise answer]

Include 3-5 question/answer pairs drawn directly from the article content.
```

## 用法 / Usage
- 必填變數 / Variables: {{target-keyword}}、{{topic}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The SEO Article Writer Prompt for ChatGPT and Claude is a free AI prompt that produces full-length, search-eng…
