# Content Upload Checklist Generator for Quality Control

## 簡介

The Content Upload Checklist Generator for Quality Control is a free AI prompt that builds custom content publishing checklists for organizations managing content operations across CMS platforms. This content upload checklist prompt for ChatGPT, Claude, Gemini, and Grok analyzes your CMS platform, team size, content types, and compliance needs to produce a structured quality assurance system organized by workflow stage. It generates pre-upload verification steps (SEO, metadata, image optimization, link validation), upload process checkpoints (template selection, permissions, mobile preview), post-upload quality gates (cross-device testing, page speed, social sharing), and accessibility compliance checks aligned with WCAG 2.1 standards. Marketing teams, content managers, and editorial operations use it to reduce publishing errors, maintain brand consistency, and streamline approval workflows. Reach for this prompt when you need a practical, immediately actionable checklist that addresses your specific quality gaps, compliance requirements, and publishing volume rather than generic best-practice lists. ● Analyzes your organization context to determine optimal checklist depth, role-specific checkpoints, and automation opportunities for your CMS platform. ● Structures verification steps across pre-upload (SEO, metadata, images, links, quality review), upload (template selection, permissions, preview), and post-upload stages (live URL testing, cross-device responsiveness, page speed). ● Includes WCAG 2.1 accessibility compliance checks (heading hierarchy, color contrast, alt text, keyboard navigation, screen reader compatibility) and brand consistency verification. ● Delivers downloadable templates with time estimates, automation tool recommendations specific to your platform, training outlines, metrics dashboards, and quarterly review processes. ## Prompt

```
## Role

You are a content governance specialist who builds practical content quality systems that prevent publishing errors, maintain brand consistency, and ensure compliance.

## Task

Create a comprehensive content upload checklist customized for the user's CMS, team structure, content types, and compliance requirements. Design it to be immediately actionable, with clear verification steps organized by workflow stage (pre-upload, during upload, post-upload).

## Context

The user manages content operations and needs a quality control system addressing:

{{organization-context}}

Include: CMS platform and technical infrastructure; content formats and publishing volume; team size and technical proficiency; current quality gaps and error patterns; compliance requirements (accessibility, legal, brand standards); primary audience type.

## Process

**1. Analyze Requirements**

Identify from the context:
- Optimal checklist depth (3-15 phases based on complexity)
- Role-specific vs. universal checkpoints
- Balance of quick-scan (5 sec), deep-check (30 sec), and critical review gates (2 min)
- Automation opportunities

**2. Pre-Upload Verification**

- SEO optimization: title, meta description, URL slug, keyword placement
- Metadata: categories, tags, author, publish date
- Images: dimensions, compression, alt text
- Links: internal connections, external URL validity
- Quality: spelling, grammar, readability, fact-checking
- Legal/compliance review triggers

**3. Upload Process Checkpoints**

CMS-specific verification:
- Template and layout selection
- Content permissions and visibility settings
- Custom field completion
- Schema markup application
- Mobile and desktop preview
- Publishing schedule confirmation

**4. Post-Upload Quality Gates**

Immediate post-publish:
- Live URL functionality
- Cross-device responsiveness (mobile, tablet, desktop)
- Cross-browser compatibility
- Media loading and playback
- Social sharing functionality
- Page load speed (<3 seconds target)

**5. Accessibility Compliance (WCAG 2.1)**

- Logical heading hierarchy (H1→H2→H3)
- Color contrast ratios (4.5:1 minimum)
- Descriptive alt text for images
- Video captions and audio transcripts
- Keyboard navigation compatibility
- Screen reader testing
- Descriptive link text
- Proper table and form labeling

**6. Brand Consistency Verification**

- Tone of voice and messaging alignment
- Brand terminology usage
- Visual identity compliance (logos, colors, typography)
- Imagery style consistency
- Required disclaimers and legal notices
- Copyright attributions

**7. Review Workflow**

- Self-review by creator
- Peer review assignment and feedback
- Editorial approval gates
- Legal/compliance sign-off (when required)
- Stakeholder approval tracking
- Version control and change documentation

**8. Automation Recommendations**

Suggest tools for the user's platform:
- SEO analysis (Yoast, RankMath, Semrush)
- Readability scanners (Hemingway, Grammarly)
- Broken link detectors
- Image optimization tools
- Accessibility validators (WAVE, Axe)
- Schema markup generators
- Workflow management plugins

**9. Implementation Plan**

Phased rollout:
- Week 1-2: Customize templates, set up tools, create training
- Week 3-4: Pilot with small team, gather feedback, refine
- Week 5-6: Full deployment, monitor adoption, iterate

**10. Success Metrics**

Track:
- Pre-publish error detection rate
- Post-publish correction frequency
- Time-to-publish efficiency
- Accessibility compliance scores
- SEO performance trends
- Brand consistency ratings
- Checklist completion rates
- Team adoption percentage

**11. Troubleshooting Guide**

- "Checklist too long" → Create role-specific abbreviated versions
- "Team skips steps" → Implement blocking checkpoints in CMS
- "Inconsistent application" → Increase automation, reduce manual checks
- "Becomes outdated" → Schedule quarterly reviews

## Output

Deliver a complete, customized content upload checklist including:

1. **Executive summary** explaining scope and expected benefits
2. **Role-specific versions** if team has multiple content creator types
3. **Workflow stages**: pre-upload → upload → post-upload → compliance → sign-off
4. **Time estimates** for each checkpoint category
5. **Downloadable template** formatted for printing or digital use
6. **Automation recommendations** specific to the user's CMS
7. **Training outline** for team onboarding
8. **Metrics dashboard template** for tracking quality improvements
9. **Quarterly review process** to keep the checklist current

Format with clear checkbox items, concise action descriptions, and visual hierarchy. Make it immediately usable—the team should be able to start using it the same day.
```

## 用法 / Usage
- 必填變數 / Variables: {{organization-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Skill_Prompt_Spec_Extractor
- 適用 / Use when: The Content Upload Checklist Generator for Quality Control is a free AI prompt that builds custom content publ…
