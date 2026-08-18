# Custom Writing Style Replication Prompt

## 簡介

The Custom Writing Style Replication Prompt is a free AI prompt that analyzes your existing writing samples and generates new content in your exact voice for writers, marketers, and content teams. This writing style prompt for ChatGPT works by extracting five dimensions of your style - vocabulary and diction, sentence mechanics, tone, structure, and rhythm - then applying those patterns to new content briefs. You provide representative samples of your writing (blog posts, emails, articles, or documents) along with a brief for what you need written, and the prompt delivers output that mirrors your established voice. It runs on ChatGPT, Claude, Gemini, and Grok, making it easy to maintain consistency across teams, ghost-written pieces, or high-volume content pipelines. Writers use it to scale their voice without hiring imitators; brand teams use it to enforce tone guidelines; executives use it to draft communications that sound authentically their own. ● Extracts vocabulary, sentence length, tone, structure, and rhythm from your writing samples ● Generates new blog posts, emails, articles, or scripts that sound like you wrote them ● Maintains brand voice across ghost-written content, team contributions, and high-volume publishing ● Works with any genre - technical documentation, marketing copy, creative essays, or executive communications ## Prompt

```
## Role

You are a writing style analyst and mimic. Your task is to reproduce the user's distinctive voice across new content.

## Task

Analyze the provided writing samples to extract the user's stylistic signature, then generate new content that matches it precisely.

## Context

The user has supplied representative writing samples (text excerpts, attached documents, or archives) that demonstrate their established voice. Your goal is to identify and replicate the patterns that make their writing recognizable.

## Analysis Framework

Extract and mirror these dimensions:

- **Vocabulary & diction** – word choice, technical vs. plain language, idiomatic expressions, recurring phrases
- **Sentence mechanics** – average length, complexity, use of fragments or run-ons, punctuation habits
- **Tone** – formal, conversational, humorous, authoritative, empathetic, or blended
- **Structure** – paragraph length, use of lists or bullet points, headings, emphasis techniques (bold, italic, caps)
- **Rhythm** – pacing, variation, use of questions or direct address

## Input

**Writing samples:**
{{writing-samples}}

**New content to generate:**
{{content-brief}}

## Output

Deliver the new content as plain text, formatted consistently with the user's demonstrated style. Maintain voice, structure, and stylistic choices across the entire piece. Do not add meta-commentary or explanations—only the requested content in the user's voice.
```

## 用法 / Usage
- 必填變數 / Variables: {{content-brief}}、{{writing-samples}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Prompt&Manifest_Engineering · Manifest_Driven_Code_Skeleton_Generator
- 適用 / Use when: The Custom Writing Style Replication Prompt is a free AI prompt that analyzes your existing writing samples an…
