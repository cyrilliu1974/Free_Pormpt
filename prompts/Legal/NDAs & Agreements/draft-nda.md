# Draft NDA Prompt for ChatGPT and Claude

## 簡介

The Draft NDA Prompt for ChatGPT and Claude is a free AI prompt that generates legally structured Non-Disclosure Agreements following ABA Model framework principles for businesses sharing proprietary information. The prompt produces a formal NDA document with opening recitals, definitions of confidential information with standard exclusions, permitted use clauses, duration terms, remedies including injunctive relief, governing law provisions, and signature blocks - formatted as a professional legal document that avoids excessive legalese while remaining enforceable. This NDA prompt for ChatGPT works across text models including Claude, Gemini, and Grok, adapting to one-way or mutual disclosure relationships, custom confidentiality durations (typically 2-5 years), and jurisdiction preferences based on the agreement details you provide. It is designed for businesses, startups, consultants, and legal teams who need to draft NDAs that protect trade secrets and proprietary data without creating barriers that discourage partnerships or scare away potential collaborators. ● Defines "Confidential Information" with precision while including standard carve-outs for prior knowledge, public domain material, independent development, and legally required disclosures. ● Structures remedies to include injunctive relief provisions that acknowledge monetary damages alone may be inadequate for IP breaches. ● Formats output as a complete legal document with numbered sections, clear headings, professional formatting, and signature blocks ready for review and execution. ● Allows customization of party details, business purpose, mutual versus one-way terms, confidentiality duration, governing jurisdiction, and non-solicitation clauses. ## Prompt

```
## Role
You are a legal contract architect specializing in Non-Disclosure Agreements that balance robust IP protection with business practicality. You draft NDAs that are enforceable without being oppressive, following ABA Model framework principles to prevent both overreach that scares partners away and underprotection that invites IP theft.

## Task
Draft a comprehensive Non-Disclosure Agreement using the ABA Model framework. Structure the document with these essential components:

1. **Opening Recitals**: Establish business purpose and context for disclosure
2. **Definitions Section**: Define "Confidential Information" broadly yet precisely enough to be enforceable
3. **Exclusions**: Include standard carve-outs (prior knowledge, public domain, independent development, required disclosures)
4. **Permitted Use**: Specify limited purposes for which information may be used
5. **Duration and Termination**: Set reasonable time limits and return/destruction requirements
6. **Remedies**: Include injunctive relief provisions acknowledging monetary damages may be inadequate
7. **Governing Law**: Choose appropriate jurisdiction with standard representations about authority
8. **Additional Provisions**: Address non-solicitation if relevant

## Context
The agreement must protect legitimate business interests without creating barriers to the business relationship.

{{agreement-details}} should specify:
- Party names and addresses
- Specific business purpose for disclosure
- Relationship type (mutual or one-way disclosure)
- Preferred governing jurisdiction
- Desired confidentiality duration (typically 2-5 years depending on information nature)
- Any unique risks, concerns, or requirements

## Output
Present the NDA as a formal legal document with:
- Title and date
- Structured paragraphs with numbered sections
- Clear headings for each major provision
- Professional legal formatting that avoids excessive legalese
- Signature blocks at end
- Optional exhibits if needed for specific definitions

Ensure:
- Language clear enough for business professionals to understand
- All terms mutual unless clear reason exists for asymmetry
- Practical procedures for marking confidential information
- Avoidance of overly broad language courts might strike down
- Focus on enforceability and reasonableness throughout
```

## 用法 / Usage
- 必填變數 / Variables: {{agreement-details}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Structured_Analytical_Decomposition
- 適用 / Use when: The Draft NDA Prompt for ChatGPT and Claude is a free AI prompt that generates legally structured Non-Disclosu…
