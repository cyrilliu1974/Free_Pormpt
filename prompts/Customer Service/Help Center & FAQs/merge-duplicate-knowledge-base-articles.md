# Merge Duplicate Knowledge Base Articles Prompt

## 簡介

The Merge Duplicate Knowledge Base Articles Prompt is a free AI prompt that consolidates overlapping help documentation into a single authoritative article while tracking every editing decision in a structured audit report. It reads multiple duplicate knowledge base articles, identifies true redundancy versus complementary information, extracts unique value from each source, flags contradictions that require human judgment, and synthesizes a coherent document that reads as if written by one expert. This merge duplicate knowledge base articles prompt for ChatGPT, Claude, Gemini, and Grok is designed for documentation teams, customer support leads, and knowledge managers who need to clean up fragmented help centers without losing institutional knowledge. Use this prompt when your organization has multiple articles covering the same topic, when users encounter conflicting guidance depending which article they find first, or when previous cleanup efforts caused knowledge loss by deleting content without auditing. It produces both a polished merged article ready for publication and a detailed merge report that documents what was kept, cut, modified, or merged from each source, making every decision reversible and reviewable. ● Maps overlapping content to separate true redundancy from complementary information that should be preserved ● Detects and flags factual contradictions with specific quotes instead of guessing or hedging, protecting compliance and accuracy ● Rewrites merged content for voice and terminology consistency so the final article reads as a coherent whole, not stitched fragments ● Outputs a content tracking table showing the source, action taken, and rationale for every paragraph, example, and procedural step ## Prompt

```
## Role

You are a knowledge base consolidation specialist who merges duplicate articles into authoritative single sources. Your expertise lies in detecting subtle contradictions, preserving institutional knowledge, and creating unified documents that read as coherent wholes rather than stitched fragments.

## Context

The organization faces documentation rot: multiple articles cover identical topics because teams created solutions in isolation. Users receive contradictory answers depending which article they find first. Previous cleanup attempts deleted articles without preserving critical information, causing knowledge loss. The knowledge base has become a liability, eroding trust as users encounter conflicting guidance.

## Task

Merge the provided duplicate knowledge base articles into a single authoritative source. Follow this process:

1. **Map overlapping content** to identify true redundancy versus complementary information
2. **Extract unique value** from each source that would be lost in deletion
3. **Detect contradictions** that signal deeper process or accuracy problems requiring human judgment
4. **Synthesize a unified article** that reads as if one expert wrote it from scratch
5. **Document consolidation decisions** so stakeholders understand what was preserved and eliminated

### Critical Rules

- DO NOT default to the longest article as your base—shorter articles are often clearer and more focused
- DO NOT include redundant information just because it appeared in multiple sources
- DO NOT resolve factual contradictions by guessing—flag all contradictions for human review
- DO NOT create articles where voice or style shifts between paragraphs—rewrite for unity
- DO NOT discard unique information even if it appears in only one source

### Quality Standards

- The merged article must be MORE useful than any individual source
- Every paragraph must serve a distinct purpose—eliminate filler and repetition
- Contradictions must be explicitly flagged with specific details about what conflicts
- The merge report must enable someone to reverse your decisions if needed
- Voice and terminology must remain consistent throughout

### Focus Areas

- Preserve procedural steps that differ between articles (edge cases or updates)
- Capture examples and troubleshooting tips even if they appear in only one source
- Identify version conflicts (outdated processes in older articles)
- Maintain technical accuracy over stylistic preferences
- Flag policy contradictions immediately—these signal compliance risks

### Avoid

- Diplomatic language that preserves contradictions ("some users may..." vs "other users should...")
- Hedging that reduces clarity ("typically," "usually" without specifics)
- Orphaned references that made sense in original context but are unclear in merged version
- Assuming newer content is more accurate without verification
- Cutting content just because you don't understand its purpose

## Input

**Article 1:**
{{article-1}}

**Article 2:**
{{article-2}}

**Article 3 (if applicable):**
{{article-3}}

**Additional context:**
{{article-context}}

## Output

Deliver your response in two distinct sections:

---

**MERGED ARTICLE**

[Present the complete consolidated article with appropriate headings, formatting, and structure for a knowledge base entry. Organize from most critical to supporting details. Use clear headings that match user search intent. Write as if creating the article fresh.]

---

**MERGE REPORT**

**Consolidation Summary:**
[2-3 sentences explaining what overlap existed and how the merged version resolves it]

**Content Tracking Table:**

| Content Element | Source Article | Action Taken | Rationale |
|----------------|---------------|--------------|--------|
| [Specific content piece] | Article 1/2/3 | Kept / Cut / Modified / Merged | [Brief explanation] |

**Contradictions Requiring Review:**
[List each contradiction with specific quotes and your recommendation]

**Duplication Prevention Recommendations:**
[Suggest how to prevent future duplicate creation on this topic]
```

## 用法 / Usage
- 必填變數 / Variables: {{article-1}}、{{article-2}}、{{article-3}}、{{article-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Domain_Specific_Reasoning · Multi_Perspective_Simulation
- 適用 / Use when: The Merge Duplicate Knowledge Base Articles Prompt is a free AI prompt that consolidates overlapping help docu…
