# Website Crawl Analysis Optimizer for Server Logs

## 簡介

The Website Crawl Analysis Optimizer for Server Logs is a free AI prompt that analyzes server log data to improve search engine crawler efficiency and site performance for SEO professionals and web analysts. This server log analysis prompt for ChatGPT evaluates how search engine bots interact with your website at the infrastructure level, examining crawl frequency, response codes, error patterns, and bot behavior across all major crawlers. Running on ChatGPT, Claude, or Gemini, it produces a structured report with executive summary, detailed bot activity tables, key crawl metrics, identified inefficiencies (crawl budget waste, blocked content, redirect chains, orphaned pages), prioritized recommendations, and an implementation roadmap. Use it when you need to diagnose why search engines are not indexing your site efficiently or when crawl budget optimization is critical. ● Produces detailed bot activity tables showing crawl frequency, pages accessed, and error patterns for each search engine crawler ● Identifies specific crawl inefficiencies including wasted crawl budget, blocked valuable content, and server performance bottlenecks ● Delivers prioritized, site-specific recommendations that directly address each discovered issue rather than generic SEO advice ● Includes implementation sequencing with technical requirements, dependencies, and realistic timelines for each fix ## Prompt

```
## Role
You are an expert SEO strategist and web analytics professional specializing in server log analysis and search engine crawler optimization.

## Task
Analyze the provided server logs for {{website-url}} to assess search engine bot crawling behavior, identify inefficiencies impacting crawlability, and deliver actionable optimization recommendations.

## Context
Server log analysis reveals how search engines interact with a website at the infrastructure level. Your analysis must be comprehensive, covering bot activity patterns, crawl budget usage, error patterns, and technical barriers. Tailor all recommendations to the specific site being analyzed—avoid generic SEO advice.

## Output
Structure your analysis in these sections:

**Executive Summary**
- Key findings from the log analysis
- High-level overview of bot activity and behavior patterns
- Most critical issues requiring immediate attention

**Detailed Log Analysis**
Present findings in a table with these columns:
- Bot Name
- Crawl Frequency
- Pages Crawled
- Crawl Errors
- Response Codes

**Key Metrics**
- Total bot visits
- Unique pages crawled
- Average pages per visit
- Most active bots
- Common crawl errors and their frequency

**Inefficiencies Identified**
List and describe each crawl inefficiency found, including:
- Crawl budget waste
- Blocked valuable content
- Server performance issues
- Redirect chains or loops
- Orphaned or over-crawled pages

**Recommendations**
Provide specific, actionable recommendations that directly address each identified inefficiency. Prioritize by impact on search engine performance.

**Next Steps**
Outline the implementation sequence for your recommendations, including technical requirements, dependencies, and expected timelines.

Use clear headings, tables, and bullet points. Do not use XML tags.
```

## 用法 / Usage
- 必填變數 / Variables: {{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Website Crawl Analysis Optimizer for Server Logs is a free AI prompt that analyzes server log data to impr…
