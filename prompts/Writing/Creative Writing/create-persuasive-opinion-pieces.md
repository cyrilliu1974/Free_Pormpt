# Opinion Piece Generator With Dependency Grammar

## 簡介

The Opinion Piece Generator With Dependency Grammar is a free AI prompt that produces well-structured, persuasive opinion articles on any topic using linguistic principles and rhetorical techniques. This opinion piece prompt for ChatGPT guides AI models through a rigorous writing process that combines dependency grammar analysis with classical rhetoric. The prompt outputs a complete opinion article formatted in XML with distinct sections: a thesis statement, an introduction with hook and background, three body paragraphs with topic sentences, supporting evidence, analysis, and transitions, plus a conclusion that reinforces the argument. It runs on ChatGPT, Claude, Gemini, and Grok, and explicitly documents which dependency grammar principles and rhetorical devices were applied throughout the piece. Writers can simply specify their topic and receive a publication-ready opinion article that balances syntactic precision with persuasive power. Reach for this prompt when you need to articulate a clear position on a controversial or complex topic with linguistic rigor and rhetorical impact. ● Produces a complete opinion piece with thesis, three supporting arguments, introduction, and conclusion in structured XML format ● Applies dependency grammar principles to ensure syntactic clarity and semantic richness in every sentence ● Incorporates classical rhetorical devices and explicitly documents which techniques were used and where ● Maintains logical coherence with deliberate transitions and evidence-backed analysis in each body paragraph ## Prompt

```
## Role
You are an AI writing assistant with expertise in linguistics, rhetoric, and dependency grammar.

## Task
Generate a persuasive opinion piece on {{topic}} that employs dependency grammar principles and rhetorical devices to craft a well-structured, compelling argument.

## Output Structure
Deliver the opinion piece in the following XML format:

```xml
<topic>{{topic}}</topic>

<thesis_statement>$thesis_statement</thesis_statement>

<introduction>
$hook
$background
$thesis_restatement
</introduction>

<body_paragraph1>
<topic_sentence>$topic_sentence</topic_sentence>
<supporting_evidence>$supporting_evidence</supporting_evidence>
<analysis>$analysis</analysis>
<transition>$transition</transition>
</body_paragraph1>

<body_paragraph2>
<topic_sentence>$topic_sentence</topic_sentence>
<supporting_evidence>$supporting_evidence</supporting_evidence>
<analysis>$analysis</analysis>
<transition>$transition</transition>
</body_paragraph2>

<body_paragraph3>
<topic_sentence>$topic_sentence</topic_sentence>
<supporting_evidence>$supporting_evidence</supporting_evidence>
<analysis>$analysis</analysis>
<transition>$transition</transition>
</body_paragraph3>

<conclusion>
$thesis_restatement
$key_points_summary
$final_thought
</conclusion>

<dependency_grammar_principles_applied>
• $principle1
• $principle2
• $principle3
</dependency_grammar_principles_applied>

<rhetorical_devices_used>
• $device1
• $device2
• $device3
</rhetorical_devices_used>
```

## Requirements
- Craft syntactically sound and semantically rich sentences using dependency grammar principles
- Articulate a clear thesis and develop three supporting arguments using rhetorical devices
- Ensure logical structure with coherent transitions between paragraphs
- Support all claims with evidence and analysis
- Include a compelling introduction with hook and background
- Conclude with a thought-provoking final statement
```

## 用法 / Usage
- 必填變數 / Variables: {{topic}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Opinion Piece Generator With Dependency Grammar is a free AI prompt that produces well-structured, persuas…
