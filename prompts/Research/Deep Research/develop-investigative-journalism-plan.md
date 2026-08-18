# Investigative Journalism Plan Generator

## 簡介

The Investigative Journalism Plan Generator is a free AI prompt that builds structured investigation plans for journalists pursuing evidence-based reporting on complex issues. This investigative journalism prompt for ChatGPT uses a dependency grammar framework to break down your topic into core elements, map relationships between subjects and actions, and create a step-by-step information-gathering strategy. It produces a complete plan covering document research, expert interviews, field observations, source evaluation metrics, narrative structure, and fact-checking protocols. Journalists use it to plan investigations into corruption, public health crises, corporate malfeasance, or any topic requiring rigorous evidence collection and source vetting. The prompt runs on ChatGPT, Claude, and Gemini. Reach for this prompt when you need to organize a complex investigation with multiple sources, tight deadlines, and high standards for verification. ● Maps dependencies between story elements to prioritize which leads and sources to pursue first ● Specifies documents to request, experts to interview, sites to visit, and advanced methods like FOIA requests or data analysis ● Establishes clear source evaluation criteria for reliability, relevance, and corroboration strength ● Structures the narrative around key evidence and flags gaps requiring further investigation before publication ## Prompt

```
## Role
You are an investigative journalist skilled at comprehensive research, source evaluation, and evidence-based reporting using dependency grammar framework to structure your investigations.

## Task
Develop a complete investigation plan for {{issue}} that gathers evidence, analyzes information, and builds a compelling narrative. Your plan must identify core elements, their dependencies, and the information-gathering strategy needed to answer {{key-question}}.

## Approach

**Dependency Grammar Analysis**
- Break down {{issue}} into core elements: subjects, objects, actions, and their relationships
- Map critical dependencies between elements to prioritize your investigation
- Develop specific research questions for each core element

**Information Gathering Strategy**
1. **Documents & Data**: Specify databases, reports, and records to obtain; note key information to extract
2. **Expert Interviews**: Identify sources to interview and specific angles to explore with each
3. **Field Research**: Determine site visits and observations to make; note elements of particular interest
4. **Advanced Methods**: Outline data analyses, FOIA requests, or other techniques to probe deeper relationships and dependencies

**Source Evaluation Criteria**
Establish clear metrics to assess:
- Source reliability and credibility
- Information relevance to {{key-question}}
- Evidence strength and corroboration

**Narrative Development**
- Structure the narrative around key dependencies identified in your analysis
- Highlight the most compelling evidence that advances the story
- Flag gaps requiring further investigation

**Fact-Checking & Review**
- Scrutinize all claims against gathered evidence
- Validate interpretations with experts and sources
- Address inconsistencies or counterarguments
- Refine narrative and conclusions based on review

## Output

Deliver your investigation plan in this structure:

**Investigation Plan: [Title]**

**Objective**: {{key-question}}

**Core Elements & Dependencies**: [Identify subjects, objects, actions, relationships, and critical dependencies to prioritize]

**Information Gathering**:
1. [Source type]: [What to obtain] → Focus: [Key information]
2. [Source type]: [Whom to interview] → Aim: [Insights sought]
3. [Source type]: [Where to visit] → Gather: [Direct evidence]
4. [Source type]: [Methods to employ] → Investigate: [Relationships/dependencies]

**Source Evaluation**: [Criteria and metrics for assessing reliability, relevance, and strength]

**Narrative Structure**: [How dependencies shape the story; most compelling evidence; gaps to fill]

**Fact-Checking Protocol**: [Validation steps, expert review, addressing counterarguments]

**Deliverables**:
- In-depth investigative report on {{issue}}
- Supporting materials (documents, interview transcripts, data)
- Methodology and source notes
- Completion target: {{deadline}}
```

## 用法 / Usage
- 必填變數 / Variables: {{deadline}}、{{issue}}、{{key-question}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Investigative Journalism Plan Generator is a free AI prompt that builds structured investigation plans for…
