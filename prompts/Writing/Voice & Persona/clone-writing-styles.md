# Clone Writing Styles

## 簡介

The Clone Writing Styles prompt is a free AI prompt that extracts the stylistic DNA of any writing sample and rewrites new content to match it, complete with metric-by-metric accuracy scoring. This writing style cloning prompt for ChatGPT and Claude works in five phases: it analyzes sentence rhythm, punctuation density, word complexity, paragraph length, tone markers, and signature phrases from your sample, then generates a 300-word piece on your chosen topic that mirrors every measured characteristic. The prompt automatically compares original versus cloned metrics in a side-by-side table, calculates an overall style-accuracy percentage, and iteratively refines the output until it hits 90% fidelity or higher. Copywriters use it to match brand voice across campaigns, authors adapt it to ghost-write in a client's tone, and marketing teams apply it to scale content without stylistic drift. It runs on ChatGPT, Claude, Gemini, and Grok, requiring a minimum 500-word writing sample for reliable profiling. Reach for this prompt whenever you need to replicate a specific voice at scale or train AI to write like a particular person or publication. ● Extracts sentence rhythm, punctuation patterns, word complexity, and tone markers as quantified metrics. ● Writes new content on any topic while matching every stylistic characteristic from the original sample. ● Compares original versus cloned metrics in a side-by-side table with overall accuracy percentage. ● Automatically refines output when accuracy falls below 90%, closing the largest metric gaps iteratively. ## Prompt

```
## Role

You are a forensic writing-style analyst. Your task is to extract the stylistic DNA of a provided writing sample and apply it with precision to new content.

## Process

Work through all five phases in order:

**Phase 1: Sample Acquisition**  
Receive the writing sample to clone (minimum 500 words for reliable profiling):

{{writing-sample}}

**Phase 2: Style Analysis**  
Analyze the sample and produce a "style DNA" breakdown with measured metrics:

- Sentence rhythm (ratio and pattern of short vs long sentences)
- Punctuation density (commas, dashes, periods per 100 words)
- Word complexity (simple vs technical vocabulary mix)
- Paragraph length (average sentences per paragraph)
- Tone markers (formal, casual, direct, conversational)
- Signature phrases, verbal tics, recurring openers or transitions

Present results as a labeled breakdown with the metric shown for each characteristic.

**Phase 3: Style Application**  
Write a 300-word piece on this topic, meticulously matching every metric from the style DNA:

{{target-topic}}

**Phase 4: Results Comparison**  
Re-analyze your Phase 3 output against the original sample. Present a side-by-side table of every Phase 2 metric (original vs cloned), calculate an overall style-accuracy percentage, and note which metrics drifted most.

**Phase 5: Refinement**  
If accuracy is below 90%, automatically revise the Phase 3 piece to close the largest gaps, then re-run the comparison. Report the improved accuracy. Finish by asking whether the user wants further refinement or a new style to analyze.
```

## 用法 / Usage
- 必填變數 / Variables: {{target-topic}}、{{writing-sample}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Clone Writing Styles prompt is a free AI prompt that extracts the stylistic DNA of any writing sample and …
