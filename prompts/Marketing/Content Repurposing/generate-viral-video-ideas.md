# Viral Video Advisor for YouTube Content Strategy

## 簡介

The Viral Video Advisor for YouTube Content Strategy is a free AI prompt that analyzes successful videos from a specific channel and generates original content ideas based on proven viral patterns. This viral video advisor prompt for ChatGPT works in two phases: first, it dissects each provided viral video by extracting its title, describing the exact thumbnail composition for recreation, and identifying the specific elements that drove its success. Second, it brainstorms 10 entirely new video concepts tailored to your channel theme and target audience, complete with optimized titles, visual thumbnail blueprints, and concrete virality predictions. The prompt runs on ChatGPT, Claude, Gemini, and Grok, making it accessible across all major text-generation models. YouTube creators use it to reverse-engineer what works on their channel, spot patterns they might miss manually, and systematically develop content strategies grounded in real performance data rather than guesswork. Reach for this prompt when you have a collection of high-performing videos and need a structured framework to extract their common threads and expand your content roadmap without repeating the same concepts. ● Deconstructs every viral video into title, exact thumbnail description, and success factors with one sharpening suggestion per video. ● Generates 10 genuinely original video ideas that fit the channel theme but explore new formats and angles not yet covered. ● Outputs structured text blocks with visual-only thumbnail descriptions separate from virality reasoning, ready for designers and strategists. ● Enforces specificity: no vague suggestions or generic explanations, only concrete visual instructions and performance predictions. ## Prompt

```
## Role

You analyze viral YouTube videos and generate new content ideas based on proven patterns from a specific channel.

## Context

- Channel theme: {{channel-theme}}
- Target audience: {{target-audience}}
- Viral videos to analyze: {{viral-videos}}

## Task

### Part 1: Analyze each viral video

For every video in the list above, output exactly this block:

**TITLE** = (title here)  
**THUMBNAIL** = (visual description: what appears in the thumbnail and how to recreate it exactly; no virality analysis in this field)  
**WHY IT WAS VIRAL** = (what made it succeed, and one way it could be sharpened)

Cover every video. Do not skip any.

### Part 2: Brainstorm 10 new video ideas

Generate 10 original ideas that fit the channel theme but push into new formats, angles, or territory the channel has not covered. For each idea, output:

**TITLE** = (title here)  
**THUMBNAIL** = (visual description: what to show and how to recreate it)  
**WHY IT WOULD BE VIRAL** = (specific reason this concept would perform)

## Output Requirements

- Thumbnail descriptions are visual-only, no virality analysis in that field
- Brainstormed ideas must be genuinely new, not remixes of the analyzed videos
- Be specific; vague descriptions and generic explanations are not useful
```

## 用法 / Usage
- 必填變數 / Variables: {{channel-theme}}、{{target-audience}}、{{viral-videos}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Viral Video Advisor for YouTube Content Strategy is a free AI prompt that analyzes successful videos from …
