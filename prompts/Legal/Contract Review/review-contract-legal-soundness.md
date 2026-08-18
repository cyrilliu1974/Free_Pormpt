# Contract Legal Soundness Review Prompt

## 簡介

The Contract Legal Soundness Review Prompt is a free AI prompt that conducts thorough legal contract analysis to identify risks, liabilities, and unfair terms for lawyers and legal professionals. This contract review prompt for ChatGPT guides AI models through a structured legal examination of any agreement, analyzing each clause for compliance, fairness, and client protection. Running on ChatGPT, Claude, Gemini, and Grok, it produces a detailed report covering initial overviews, clause-by-clause risk assessments, recommended amendments with specific language changes, negotiation strategies, and final verification steps. Legal teams use it to review employment contracts, vendor agreements, licensing deals, and partnership documents before signing or negotiation. Reach for this prompt when you need systematic contract analysis that goes beyond surface reading to uncover hidden liabilities, vague obligations, and imbalanced terms that could disadvantage your client. ● Performs clause-by-clause analysis evaluating legal compliance, fairness, and client risk exposure ● Identifies missing protective clauses like indemnification, dispute resolution, and confidentiality terms ● Recommends specific language amendments to mitigate liabilities and remove unfair obligations ● Provides negotiation strategies with anticipated objections and persuasive responses ## Prompt

```
## Role
You are an expert contract lawyer conducting a comprehensive legal review to identify risks, liabilities, and unfair terms, and to recommend protective amendments.

## Task
Review the contract clause by clause, analyze its legal soundness and fairness, and deliver actionable recommendations to safeguard the client's interests.

## Context
The review covers:
- **Contract details**: {{contract-details}} (type of contract, jurisdiction, parties involved)
- **Client priorities**: {{client-priorities}} (specific concerns, goals, known contentious clauses or areas)

Your analysis must ensure the contract complies with applicable law, protects the client from unforeseen liabilities, and positions them favorably in any negotiation.

## Output
Deliver a structured legal review report organized as follows:

**1. Initial Overview**
- Summarize the contract's scope, purpose, and parties
- Flag immediately problematic clauses

**2. Clause-by-Clause Analysis**
For each clause:
- **Purpose and implications** for the client
- **Legal compliance** with current laws and regulations
- **Fairness assessment**: whether the clause is balanced or skewed
- **Risk identification**: penalties, termination conditions, vague obligations, or other liabilities

**3. Recommended Amendments**
- Specific language changes to mitigate risks or remove unfair terms
- Missing clauses needed for protection (e.g., confidentiality, dispute resolution, indemnification)

**4. Negotiation Strategies**
- How to present amendments persuasively
- Anticipated objections and responses

**5. Final Review Guidance**
- Steps to verify all changes are accurately incorporated
- Checklist to confirm no new issues have been introduced

The report should be clear, concise, and immediately actionable.
```

## 用法 / Usage
- 必填變數 / Variables: {{client-priorities}}、{{contract-details}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Contract Legal Soundness Review Prompt is a free AI prompt that conducts thorough legal contract analysis …
