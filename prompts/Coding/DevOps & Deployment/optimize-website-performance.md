# PageSpeed Insights Tutorial Prompt for Website Performance

## 簡介

The PageSpeed Insights Tutorial Prompt for Website Performance is a free AI prompt that generates comprehensive, beginner-friendly tutorials for analyzing and improving website speed using Google's PageSpeed Insights tool. Whether you're auditing an e-commerce site, monitoring a blog, or optimizing a client's web presence, this website performance prompt for ChatGPT produces structured guides that explain critical metrics like First Contentful Paint, Largest Contentful Paint, and Time to Interactive in plain language, then walk users through actionable fixes such as image compression, CSS minification, browser caching, and render-blocking resource elimination. It runs on ChatGPT, Claude, and Gemini to deliver tutorials tailored to users with limited technical knowledge. Reach for this prompt when you need to create documentation, train team members on performance monitoring, or provide clients with clear optimization roadmaps. ● Produces numbered tutorials with sub-steps that explain how to access PageSpeed Insights, enter a URL, and interpret the results dashboard ● Breaks down five core performance metrics with real-world significance and guidance on identifying bottlenecks ● Delivers implementation instructions for common fixes like image optimization, code minification, caching configuration, and server response tuning ● Includes separate reference sections for key metrics and actionable improvements to serve as quick-lookup guides ## Prompt

```
## Role
You are a website performance optimization specialist with expertise in using PageSpeed Insights to identify and resolve performance bottlenecks.

## Task
Create a comprehensive, step-by-step tutorial on using PageSpeed Insights to monitor and analyze {{website-url}}. The guide should enable users to identify actionable improvements to enhance website speed and user experience.

## Tutorial Structure

**1. Introduction to PageSpeed Insights**
- Explain what PageSpeed Insights is and its purpose
- Highlight the importance of website performance optimization

**2. Setting up PageSpeed Insights**
- Describe how to access PageSpeed Insights (https://pagespeed.web.dev/)
- Provide instructions on entering the website URL for analysis

**3. Interpreting PageSpeed Insights Results**
- Explain these key metrics and their significance:
  - First Contentful Paint: time for first content to appear
  - Speed Index: how quickly content is visually displayed during page load
  - Largest Contentful Paint: time for the largest content element to appear
  - Time to Interactive: time for the page to become fully interactive
  - Total Blocking Time: total time the main thread was blocked between FCP and TTI
- Describe how to identify performance issues based on the results

**4. Actionable Improvements**
Provide step-by-step instructions for implementing these common fixes:
- Optimize images: compress and resize to reduce load times
- Minify CSS and JavaScript: remove unnecessary code and whitespace
- Leverage browser caching: set appropriate caching headers
- Reduce server response times: optimize server-side code and database queries
- Eliminate render-blocking resources: defer non-critical CSS and JavaScript

**5. Monitoring and Ongoing Optimization**
- Emphasize the importance of regular performance monitoring
- Provide tips for maintaining and continuously improving website performance

## Output Criteria
- Write for users with limited technical knowledge
- Clearly explain each step with relevant examples
- Focus on the most critical aspects of PageSpeed Insights and performance improvements
- Explain technical terms in plain language
- Encourage regular monitoring and ongoing optimization

## Format
Deliver the tutorial as a numbered list with clear sub-steps, followed by two reference sections: Key Performance Metrics (with descriptions) and Actionable Improvements (with implementation guidance).
```

## 用法 / Usage
- 必填變數 / Variables: {{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The PageSpeed Insights Tutorial Prompt for Website Performance is a free AI prompt that generates comprehensiv…
