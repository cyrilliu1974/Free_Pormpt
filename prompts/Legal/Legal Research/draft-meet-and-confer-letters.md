# Draft Meet-And-Confer Letters

## 簡介

The Draft Meet-And-Confer Letters prompt is a free AI prompt that produces complete litigation correspondence for attorneys navigating discovery disputes in civil cases. This meet-and-confer letter prompt for ChatGPT, Claude, Gemini, and Grok walks you through crafting professional legal correspondence that satisfies Federal Rules of Civil Procedure 26(b)(1), 26(f), and 37(a)(1) while documenting every prior resolution attempt. The prompt structures each dispute with quoted request language, opposing counsel's objections, applicable case law, proposed compromises, and clear consequences if cooperation fails. Litigation attorneys use it to create letters that simultaneously pursue genuine settlement and build the record for a motion to compel, complete with proper case captions, chronological effort timelines, and references to Sedona Conference Principles or local standing orders. Reach for this prompt when you need formal discovery correspondence that demonstrates procedural compliance and positions your client favorably for motion practice. ● Documents all prior resolution attempts chronologically to prove compliance with meet-and-confer obligations. ● Structures each dispute with request quotes, response quotes, legal citations, proposed compromises, and stated consequences. ● Incorporates Federal Rules, relevant case law, jurisdiction-specific standing orders, and discovery standards into every section. ● Produces letters that function both as genuine settlement tools and as exhibits ready to attach to motions to compel. ## Prompt

```
## Role

You are an experienced litigation attorney specializing in complex commercial disputes and discovery practice. Your meet-and-confer letters consistently resolve discovery disputes, demonstrate good-faith compliance with court rules, and position clients favorably if motion practice becomes necessary.

## Task

Draft a complete, court-ready meet-and-confer letter that satisfies judicial requirements for good-faith dispute resolution while firmly establishing the legal basis for a motion to compel if opposing counsel does not cooperate.

## Context

{{discovery-disputes}}

The letter must serve dual purposes: genuine attempt at resolution with opposing counsel and potential exhibit for a discovery motion. It must comply with Federal Rules of Civil Procedure 26(b)(1), 26(f), and 37(a)(1), reference applicable case law and Sedona Conference Principles where relevant, and follow any local rules or standing orders in {{jurisdiction-and-rules}}.

Document all prior resolution attempts from {{prior-efforts}} to demonstrate procedural compliance. Work toward the deadlines specified in {{case-timeline}}.

## Output

Structure the letter with:

**Header**: Proper legal letterhead format with case caption from {{case-details}}, case number, date, and recipient information

**Opening**: Professional tone establishing purpose, relevant rule citations, and summary of good-faith efforts to date

**Prior Efforts**: Chronological documentation of all previous correspondence, calls, and resolution attempts

**Dispute Breakdown**: For each discovery dispute, provide:
- **Our Request**: Quote exact language and request number
- **Your Response**: Quote objections or deficiencies
- **Legal Basis**: Cite specific Federal Rules, relevant case law, and discovery standards
- **Proposed Resolution**: Offer reasonable compromise that preserves core discovery needs
- **Consequences**: State intention to seek motion to compel, attorney's fees, and sanctions if unresolved

**Additional Disputes**: Separate sections for deposition scheduling or interrogatory issues if applicable

**Summary of Requested Actions**: Numbered list of all specific actions requested with deadline for response

**Closing**: Professional tone proposing follow-up call while clearly stating next steps if resolution is not reached

Format with clear section headings, numbered disputes, bullet points for lists, and professional legal correspondence style ready for immediate use.
```

## 用法 / Usage
- 必填變數 / Variables: {{case-details}}、{{case-timeline}}、{{discovery-disputes}}、{{jurisdiction-and-rules}}、{{prior-efforts}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Draft Meet-And-Confer Letters prompt is a free AI prompt that produces complete litigation correspondence …
