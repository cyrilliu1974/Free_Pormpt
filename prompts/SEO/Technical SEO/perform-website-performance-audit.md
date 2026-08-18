# Website Performance Audit Prompt for ChatGPT

## 簡介

The Website Performance Audit Prompt for ChatGPT is a free AI prompt that delivers structured technical audits for website owners, developers, and SEO professionals. By analyzing a target URL, this website performance audit prompt for ChatGPT produces a detailed checklist covering page load performance, mobile responsiveness, HTTPS implementation, accessibility standards, and overall site health. It runs on ChatGPT, Claude, and Gemini, transforming complex technical analysis into prioritized action items that site owners can immediately implement to improve speed, security, and user experience. This prompt is ideal for technical SEO audits, pre-launch website checks, performance optimization projects, and ongoing site maintenance workflows. ● Evaluates page load times against 3-second benchmarks and identifies optimization opportunities for images, CSS, JavaScript, caching, and server response ● Assesses mobile responsiveness across devices, checking touch targets, font readability, navigation functionality, and viewport rendering ● Audits HTTPS implementation, SSL certificates, mixed content warnings, and security vulnerabilities to ensure data protection ● Reviews accessibility compliance against WCAG 2.1 guidelines, including alt text, color contrast, keyboard navigation, and multimedia alternatives ● Delivers findings in a checkbox format that allows site owners to track progress and prioritize fixes based on impact ## Prompt

```
## Role

You are an expert technical website auditor specializing in site performance analysis and actionable optimization recommendations.

## Task

Perform a detailed technical audit of {{website-url}}, evaluating page load times, mobile responsiveness, HTTPS implementation, accessibility, and overall site health. Compile findings into a structured checklist with checkboxes for the site owner to review and prioritize improvements.

## Output

Deliver a comprehensive audit checklist organized into these sections:

### Page Load Performance
- [ ] Evaluate overall page load times (target: under 3 seconds)
- [ ] Identify and optimize large images or media files
- [ ] Minify HTML, CSS, and JavaScript files
- [ ] Leverage browser caching for static assets
- [ ] Minimize redirects and server response times

### Mobile Responsiveness
- [ ] Verify responsive design across devices (desktop, tablet, mobile)
- [ ] Ensure touch targets are appropriately sized for mobile interaction
- [ ] Check for mobile-friendly font sizes and readability
- [ ] Test mobile navigation and menu functionality
- [ ] Confirm absence of horizontal scrolling on mobile views

### HTTPS and Security
- [ ] Implement SSL/HTTPS across all site pages
- [ ] Ensure secure protocol for collecting user data and transactions
- [ ] Check for mixed content warnings (HTTP content on HTTPS pages)
- [ ] Verify up-to-date SSL certificate installation
- [ ] Scan for potential security vulnerabilities or outdated software

### Accessibility
- [ ] Evaluate site against WCAG 2.1 guidelines
- [ ] Ensure all images have appropriate alt text
- [ ] Check for sufficient color contrast ratios
- [ ] Verify keyboard navigation and focus indicators
- [ ] Provide text alternatives for multimedia content

### Additional Technical Considerations
- [ ] Optimize CSS delivery and remove unused styles
- [ ] Minimize use of render-blocking JavaScript
- [ ] Leverage CDN for improved asset delivery and performance
- [ ] Implement proper canonicalization and 301 redirects
- [ ] Verify XML sitemap and robots.txt for optimal crawlability

Provide specific, tailored findings for each checklist item rather than generic observations. Prioritize issues based on their impact on site performance and user experience.
```

## 用法 / Usage
- 必填變數 / Variables: {{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Academic_Research_Synthesis_Pipeline · Writing_Quality_Multi_Dimension_Checker
- 適用 / Use when: The Website Performance Audit Prompt for ChatGPT is a free AI prompt that delivers structured technical audits…
