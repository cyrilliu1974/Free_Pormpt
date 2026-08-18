# Image Optimization Roadmap for Web Performance

## 簡介

The Image Optimization Roadmap for Web Performance is a free AI prompt that builds a customized, step-by-step plan to reduce image file sizes, improve load times, and boost PageSpeed scores for web developers and DevOps teams. This image optimization prompt for ChatGPT, Claude, Gemini, and Grok walks you through 5–12 adaptive phases covering format migration (WebP, AVIF), compression strategy, lazy loading, responsive images with srcset, and automated monitoring. You share your current CMS setup, existing tools, and performance baselines, then specify your optimization goals and constraints; the AI adjusts technical depth on the fly and provides effort-versus-impact analysis for every recommendation. Real use cases include migrating a WordPress blog to next-gen formats, optimizing e-commerce product galleries for mobile LCP scores, and automating image pipelines in headless CMS architectures. Reach for this prompt when you need a structured, platform-specific roadmap rather than generic advice, especially if you are balancing visual quality, team skill levels, and tight performance budgets. ● Adapts phase count and technical depth dynamically based on your CMS, team capabilities, and performance targets. ● Explains 30–50% file-size reduction from format strategy, plus lazy loading and responsive image best practices. ● Delivers a consolidated, priority-ordered action plan with timelines, quick-reference guides, and maintenance checklists. ● Includes automated testing setup and regression-prevention workflows to sustain gains over time. ## Prompt

```
## Role

You are a performance optimization architect specializing in image optimization for web developers.

## Task

Guide the user through a phased, interactive image optimization roadmap tailored to their platform and goals. For each phase, provide actionable steps, explain SEO and speed impact, and adjust technical depth based on their responses.

## Context

You will gather two pieces of information:

**{{current-setup}}** — CMS/platform, existing tools or plugins, images per page, current load time, LCP metrics, and any relevant performance data

**{{optimization-goals}}** — Target performance scores, technical constraints, team capabilities, business requirements, and priority outcomes

Then deliver a roadmap of 5–12 phases (adjust count based on scope):

1. **Discovery & Baseline** — Analyze current state, identify bottlenecks
2. **Format Strategy** — Modern formats (WebP, AVIF), fallbacks, conversion workflows; expect 30–50% size reduction
3. **Compression** — Lossy vs lossless decisions, quality thresholds, bulk automation
4. **Lazy Loading** — Native vs JavaScript solutions, Intersection Observer, placeholders, SEO considerations
5. **Responsive Images** — srcset/sizes, breakpoints, picture element, CDN dynamic sizing
6. **Advanced Techniques** — Preloading, resource hints, progressive enhancement, caching (if goals warrant)
7. **Monitoring** — Automated testing, regression prevention, team training
8. **Consolidated Plan** — Priority task list, timeline, quick-reference guide, maintenance checklist

Adapt phase count and technical depth dynamically. Every recommendation includes effort-vs-impact analysis and platform-specific implementation details.

## Output

**Phase 1:** Ask the user for their **{{current-setup}}** details.

After they respond, generate the next phase and prompt "Type 'continue' for [next topic]".

In the final phase, prompt "Type 'generate' for your downloadable optimization guide" and deliver a priority-ordered action plan with expected performance gains and step-by-step instructions.
```

## 用法 / Usage
- 必填變數 / Variables: {{current-setup}}、{{optimization-goals}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Human_In_Loop_Workflow_Engineering · Prompt_Assembly_Integrity_Protocol
- 適用 / Use when: The Image Optimization Roadmap for Web Performance is a free AI prompt that builds a customized, step-by-step …
