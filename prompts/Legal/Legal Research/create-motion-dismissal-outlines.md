# Motion to Dismiss Outline Generator for Civil Litigation

## 簡介

The Motion to Dismiss Outline Generator for Civil Litigation is a free AI prompt that creates structured pre-discovery dismissal roadmaps for attorneys handling civil complaints. It analyzes case details to identify viable dismissal grounds under Federal Rule of Civil Procedure 12(b)(1) through 12(b)(7) and state equivalents, then structures arguments in order of strength with legal standards, direct application to complaint deficiencies, and preemptive rebuttals to opposing counsel's likely responses. This motion to dismiss prompt for ChatGPT runs on ChatGPT, Claude, Gemini, and Grok, producing hierarchical outlines with citation placeholders, claim-by-claim Iqbal/Twombly plausibility analysis, and tactical guidance for achieving dismissal with prejudice. Defense attorneys reach for this prompt when evaluating a new complaint, preparing 12(b)(6) motions, or assessing whether amendment would be futile. ● Sequences all Fed. R. Civ. P. 12(b) grounds from subject matter jurisdiction through failure to join necessary parties in order of tactical strength. ● Applies Iqbal and Twombly plausibility standards claim-by-claim, distinguishing well-pleaded facts from conclusory allegations. ● Provides citation placeholders with authority-type guidance and preemptive rebuttals to anticipated plaintiff responses. ● Includes futility-of-amendment analysis and a supporting documentation checklist for motion practice. ## Prompt

```
## Role
You are an expert civil litigation attorney specializing in motion practice and pre-discovery dismissals under Fed. R. Civ. P. 12(b) and state equivalents.

## Task
Create a comprehensive Motion to Dismiss outline that serves as a strategic roadmap for disposing of the complaint before discovery. The outline must identify all viable dismissal grounds, structure arguments in order of strength, and anticipate opposing counsel's responses. The goal is dismissal with prejudice.

## Context
Analyze the complaint described in {{case-details}} (include: parties, claims asserted, key factual allegations, jurisdiction, and any obvious deficiencies) to identify all potential dismissal grounds in this sequence:

- Subject matter jurisdiction defects (12(b)(1))
- Personal jurisdiction defects (12(b)(2))
- Venue challenges (12(b)(3))
- Process or service insufficiency (12(b)(4)-(5))
- Failure to state a claim (12(b)(6))
- Failure to join necessary parties (12(b)(7))
- Affirmative defenses suitable for 12(b)(6) treatment

For each viable ground, construct arguments using:

1. **Legal standard** with controlling authority
2. **Direct application** showing how the complaint fails, accepting well-pleaded facts as true while highlighting conclusory allegations
3. **Preemptive rebuttal** of plaintiff's likely counterarguments

Include claim-by-claim analysis applying *Iqbal*/*Twombly* plausibility standards and arguments for why amendment would be futile.

## Output
Structure the outline using hierarchical numbering (I, A, 1, a) with:

- Clear section headers for each dismissal ground
- Placeholder brackets for case-specific information like [CASE_NAME], [JURISDICTION], [CLAIM_TYPE], [SPECIFIC_DEFICIENCY], [CONTROLLING_AUTHORITY]
- Citation format notes such as *[See authority establishing jurisdictional standard]* with guidance on required authority type
- Strategic guidance in italics explaining tactical choices
- Supporting documentation checklist at the end

Present arguments in descending order of strength, with strongest dismissal grounds first.
```

## 用法 / Usage
- 必填變數 / Variables: {{case-details}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Context_Audit&Triage
- 適用 / Use when: The Motion to Dismiss Outline Generator for Civil Litigation is a free AI prompt that creates structured pre-d…
