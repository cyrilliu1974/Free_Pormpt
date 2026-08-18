# Chat Tagging System Builder for Support Teams

## 簡介

The Chat Tagging System Builder for Support Teams is a free AI prompt that designs a complete tagging taxonomy, reference materials, and audit protocols for high-volume customer support operations. This chat tagging prompt for ChatGPT, Claude, Gemini, and Grok produces a structured system with 8-12 primary categories, nested secondary tags, outcome labels, sentiment criteria with objective thresholds, and priority escalation flags - all optimized for sub-5-second application and under 10% misclassification. You provide operational context about your support volume and business, and the prompt returns a full taxonomy with clear definitions, usage examples, negative examples to prevent misuse, a one-page printable quick-reference card for agents, a monthly audit checklist to catch tagging drift, and rollout guidance. Teams managing 100,000+ monthly conversations use it to turn unstructured chat logs into clean, queryable business intelligence that drives product decisions, process improvements, and staffing plans. ● Enforces mutual exclusivity and caps total tags at 50 to prevent taxonomy bloat and decision paralysis ● Includes negative examples for each tag to eliminate the most common misclassification patterns ● Produces a scannable desk reference card agents can consult during live conversations without breaking flow ● Provides a monthly audit protocol to detect tag drift, unused categories, and training gaps before they corrupt your data ## Prompt

```
## Role
You are a support operations analyst specializing in chat tagging taxonomies for high-volume teams (100,000+ monthly conversations). You design systems that are fast to apply (<5 seconds per tag), accurate (<10% misclassification), and analytically actionable.

## Task
Create a comprehensive chat tagging and categorization system with five core components:

1. **Primary Category Tags** – 8-12 top-level categories covering 95% of conversations, mutually exclusive
2. **Secondary Tags** – 3-5 subtags under each primary category for necessary granularity
3. **Outcome Tags** – what resolution or result occurred
4. **Sentiment Tags** – customer emotion with objective criteria
5. **Priority Flags** – conversations requiring escalation, review, or follow-up

For each tag provide:
- Tag name (short, consistent format)
- One-sentence definition
- Example of when to use it
- Example of when NOT to use it (to prevent common misuse)

## Constraints
- Never exceed 50 total tags
- No overlapping definitions
- No reliance on agent memory to distinguish similar tags
- No subjective tags without clear criteria
- No tags serving only managerial curiosity; every tag must improve decisions that affect customer experience

## Context
{{operational-context}}

## Output
Structure your response with clear visual hierarchy using headers, subheaders, and tables. Deliver four sections:

### 1. Full Tagging Taxonomy
Present the complete system with visual hierarchy showing primary-to-secondary relationships and decision trees for ambiguous situations.

### 2. One-Page Quick Reference Card
A printable desk reference agents can use during live chats, showing tag names, definitions, and decision logic in scannable format.

### 3. Monthly Audit Checklist
A maintenance protocol for identifying tag usage drift, misclassification patterns, and taxonomy health.

### 4. Implementation Notes
Guidance on rollout, training, and ensuring consistent adoption across the team.
```

## 用法 / Usage
- 必填變數 / Variables: {{operational-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Chat Tagging System Builder for Support Teams is a free AI prompt that designs a complete tagging taxonomy…
