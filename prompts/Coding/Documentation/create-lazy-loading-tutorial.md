# Lazy Loading Implementation Tutorial Generator

## 簡介

The Lazy Loading Implementation Tutorial Generator is a free AI prompt that creates detailed, developer-ready tutorials for implementing lazy loading techniques on any specified website. This lazy loading tutorial prompt for ChatGPT produces a complete guide covering the Intersection Observer API, HTML data attributes, CSS transitions, and both native and library-based approaches. It walks developers through identifying below-the-fold media, replacing src attributes with data-src, writing observer code, testing across devices and network conditions, and measuring performance improvements in PageSpeed Insights and Lighthouse. The output includes working code snippets in HTML, CSS, and JavaScript, plus guidance on responsive images, accessibility, SEO considerations, and Core Web Vitals optimization. It runs on ChatGPT, Claude, Gemini, and Grok. Reach for this prompt when you need to document lazy loading implementation for a specific website or create onboarding material for a development team tackling performance optimization. ● Covers Intersection Observer API, native loading attributes, and third-party library options with example code ● Includes testing procedures across devices, network conditions, and performance measurement tools ● Provides guidance on preventing layout shifts, handling responsive images, and maintaining SEO and accessibility ● Details common pitfalls like lazy loading hero images and missing noscript fallbacks for crawlers ## Prompt

```
## Role
You are an expert web developer specializing in website performance optimization through lazy loading techniques.

## Task
Create a comprehensive tutorial with step-by-step instructions on implementing lazy loading for images and videos to improve initial page load time and user experience for {{website-url}}.

## Structure

### 1. Introduction
- Explain the benefits of lazy loading (reduced initial load time, bandwidth savings, improved Core Web Vitals)
- Describe how lazy loading works at a high level (deferring off-screen resources until needed)
- Mention the technologies used: Intersection Observer API, HTML data attributes, CSS transitions

### 2. Prerequisites
- Basic HTML, CSS, and JavaScript knowledge
- Familiarity with the website's codebase
- Access to modify HTML, CSS, and JavaScript files

### 3. Step 1: Identify Images and Videos to Lazy Load
- Locate all images and videos that are below the fold or not immediately visible
- Prioritize larger media files that significantly impact load time
- Provide example HTML for an image to be lazy-loaded:
```html
<img data-src="image.jpg" alt="Description" class="lazy">
```

### 4. Step 2: Choose a Lazy Loading Library or Technique
- Recommend the native Intersection Observer API for modern browsers
- Mention alternatives: native loading="lazy" attribute, third-party libraries (lazysizes, lozad.js)
- Include code snippet demonstrating Intersection Observer setup:
```javascript
const observer = new IntersectionObserver((entries) => {
 entries.forEach(entry => {
 if (entry.isIntersecting) {
 const img = entry.target;
 img.src = img.dataset.src;
 observer.unobserve(img);
 }
 });
});
```

### 5. Step 3: Implement Lazy Loading
- Replace `src` with `data-src` for images/videos to be lazy-loaded
- Add `class="lazy"` to target elements
- Write JavaScript to observe elements and load them when entering viewport
- Update CSS for loading transitions:
```css
img.lazy {
 opacity: 0;
 transition: opacity 0.3s;
}
img.lazy.loaded {
 opacity: 1;
}
```

### 6. Step 4: Test and Optimize
- Test on multiple devices (mobile, tablet, desktop) and network conditions (3G, 4G, WiFi)
- Verify images/videos load correctly when scrolling into view
- Check for layout shifts using Chrome DevTools and Lighthouse
- Confirm performance improvements in PageSpeed Insights
- Optimize by adjusting intersection threshold (rootMargin)
- Handle responsive/retina images with srcset
- Provide noscript fallback for non-JavaScript users

### 7. Best Practices
- Use low-quality image placeholders (LQIP) or solid color backgrounds to prevent layout shifts
- Set explicit width and height attributes on img/video elements
- Lazy load content slightly before it enters viewport (100-200px margin)
- Apply lazy loading to CSS background images using similar techniques
- Monitor Core Web Vitals (LCP, CLS) after implementation

### 8. Potential Pitfalls
- Never lazy load hero images or above-the-fold content
- Ensure lazy-loaded images include proper alt text for accessibility and SEO
- Add `<noscript>` tags with regular img elements for SEO crawlers
- Test carousel/slider implementations carefully to ensure images load before user interaction
- Avoid excessive lazy loading that causes constant loading during scroll

### 9. Conclusion
- Summarize the implementation steps: identify candidates, choose technique, implement observer, test thoroughly
- Encourage ongoing performance monitoring and iteration
- Provide resources: MDN Intersection Observer documentation, web.dev lazy loading guide, Chrome DevTools performance profiling

## Output Format
Deliver the tutorial using markdown with clear headings, bullet points, and properly formatted code blocks. Make the tutorial accessible to developers with basic web development knowledge.
```

## 用法 / Usage
- 必填變數 / Variables: {{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Lazy Loading Implementation Tutorial Generator is a free AI prompt that creates detailed, developer-ready …
