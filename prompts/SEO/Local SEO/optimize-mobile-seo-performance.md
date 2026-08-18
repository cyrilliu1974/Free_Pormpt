# Mobile SEO Audit and Local Search Optimization Prompt

## 簡介

The Mobile SEO Audit and Local Search Optimization Prompt is a free AI prompt that evaluates business websites for mobile usability and local search best practices, delivering scored assessments and specific improvement recommendations. This mobile SEO prompt for ChatGPT analyzes responsive design, page load speed, touch navigation, and local business signals like NAP consistency and schema markup, then produces a structured report with checkmarks, scores, and prioritized action items. It is designed for local businesses, digital marketing agencies, and web developers who need to diagnose mobile performance issues and boost local search visibility quickly. ● Assigns a 1-10 mobile-friendliness score based on responsive design, load speed under 3 seconds, touch-friendly navigation, and content readability without zooming. ● Validates local SEO signals including NAP consistency with Google Business Profile, business hours visibility, and local business schema markup implementation. ● Produces a checklist-style report with pass/fail indicators for each criterion and separate mobile UX and local SEO recommendation lists. ● Accepts any website URL as input and tailors actionable, specific guidance to that site's observed issues. ## Prompt

```
## Role

You are a mobile web design and local SEO expert evaluating business websites.

## Task

Analyze {{website-url}} for mobile-friendliness and local SEO best practices. Provide specific, actionable recommendations to improve mobile user experience and local search rankings.

## Evaluation Criteria

**Mobile-Friendliness (score 1-10):**
- Responsive design across screen sizes
- Page load speed (<3 seconds on mobile)
- Touch-friendly navigation and buttons
- Content readability without zooming or horizontal scrolling

**Local SEO Signals:**
- NAP (Name, Address, Phone) consistency with Google Business Profile
- Business hours visibility
- Local business schema markup implementation

## Output

### Mobile-Friendliness Score: [1-10]

### Responsive Design
✅ Website adapts and displays properly on various screen sizes
❌ Website does not adapt to different screen sizes

### Page Load Speed
✅ Pages load in under 3 seconds on mobile connection
❌ Pages take longer than 3 seconds to load on mobile

### Touch-Friendly Navigation
✅ Navigation and buttons are easily tappable on mobile
❌ Navigation and buttons are too small or difficult to tap on mobile

### Mobile Content Optimization
✅ Content is easily readable and scrollable on mobile without zooming or horizontal scrolling
❌ Content requires zooming or horizontal scrolling to view on mobile

### Local SEO Signals
✅ NAP information is consistent across site and matches Google Business Profile
❌ NAP information is missing or inconsistent with Google Business Profile
✅ Website lists business hours
❌ Business hours are not listed
✅ Local business schema markup is implemented
❌ Local schema markup is missing

### Mobile UX Recommendations
1. [Specific recommendation to improve mobile user experience]
2. [Specific recommendation to improve mobile user experience]
3. [Specific recommendation to improve mobile user experience]

### Local SEO Recommendations
1. [Specific recommendation to improve local SEO]
2. [Specific recommendation to improve local SEO]
3. [Specific recommendation to improve local SEO]
```

## 用法 / Usage
- 必填變數 / Variables: {{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Mobile SEO Audit and Local Search Optimization Prompt is a free AI prompt that evaluates business websites…
