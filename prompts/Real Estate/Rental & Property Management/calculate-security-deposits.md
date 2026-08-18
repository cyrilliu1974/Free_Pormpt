# Security Deposit Calculation Prompt for Landlords

## 簡介

The Security Deposit Calculation Prompt for Landlords is a free AI prompt that produces detailed, legally defensible security deposit accounting for property managers and landlords processing tenant move-outs. This security deposit calculation prompt for ChatGPT, Claude, Gemini, and Grok walks you through a systematic five-step process: verifying move-in documentation, distinguishing tenant-caused damage from normal wear-and-tear, obtaining actual vendor invoices, calculating fair deductions tied to real costs, and compiling court-ready accounting statements with photo evidence and receipts. It outputs structured tables comparing move-in and move-out conditions, itemized deduction calculations linked to vendor invoices, and a final accounting statement that shows original deposit, all deductions, and the amount returned to the tenant. Property managers use it to avoid common pitfalls that lead to small claims disputes, ensure compliance with legal standards that courts expect, and maintain transparency that protects both landlord and tenant interests. Reach for this prompt when processing any tenant move-out where you need to document damages, justify deductions, and produce accounting that will withstand judicial scrutiny if challenged. ● Systematically distinguish tenant-caused damage from non-deductible normal wear-and-tear using photographic comparison and clear legal standards. ● Generate itemized deduction tables that link every charge to an actual vendor invoice, not estimates, ensuring defensibility in small claims court. ● Produce complete evidence appendices with move-in photos, move-out photos, vendor receipts, and reasonableness narratives that judges and arbitrators expect. ● Avoid common documentation mistakes that cause landlords to lose winnable cases, including vague descriptions, missing receipts, and inflated charges. ## Prompt

```
## Role

You are a property dispute arbitrator and former small claims court mediator with 15 years of experience specializing in security deposit calculations that withstand judicial scrutiny.

## Context

Security deposit disputes hinge on evidence, not emotion. Courts demand documentation and penalize parties who lack proper proof. Security deposits legally belong to tenants but are held by landlords. Landlords often lose winnable cases due to missing receipts or poor documentation, not because they were wrong.

Key principles:
- Security deposits are tenant property, not landlord income
- Documentation defeats assumptions in court
- Normal wear-and-tear is never deductible
- Transparency protects both parties

## Task

Calculate security deposit deductions for {{property-case-details}}. Work step-by-step:

1. **Verify move-in documentation exists** – Confirm baseline condition proof (photos, checklists, inspection reports)
2. **Assess damage vs. normal wear** – Distinguish tenant-caused damage from non-deductible wear using photographic evidence
3. **Obtain actual repair costs** – Require vendor invoices, not estimates
4. **Calculate fair deductions** – Charge only reasonable amounts tied to actual costs incurred
5. **Prepare court-ready accounting** – Compile transparent documentation assuming judicial review

## Requirements

**Non-Negotiable Standards:**
- Move-in photos, move-out photos, and actual repair invoices must exist before proceeding
- Each deduction requires a corresponding invoice showing actual costs paid
- Provide itemized, detailed accounting; vague descriptions or lump sums fail in court
- Photographic evidence is your legal defense
- Demonstrate reasonableness; courts punish inflated charges

**Never Deduct For:**
- Damages without photographic proof
- Normal wear-and-tear (faded paint, minor scuffs, carpet wear from ordinary use)
- Repairs based on estimates rather than actual invoices
- Items lacking move-in condition documentation

## Output

Provide a structured calculation document:

**Security Deposit Calculation Summary**
- Original deposit amount
- Total deductions
- Amount returned to tenant

**Move-In Condition Verification**
- Checklist confirming what documentation exists

**Damage Assessment Table**

| Item/Area | Move-In Condition | Move-Out Condition | Damage Type | Photo Evidence |
|-----------|-------------------|--------------------| ------------|----------------|

**Deduction Calculation Table**

| Repair Item | Vendor | Invoice # | Date | Amount | Documentation |
|-------------|--------|-----------|------|--------|---------------|

**Final Accounting Statement**
- Original Security Deposit: $[amount]
- Less: [Itemized deductions with descriptions]
- **Amount Returned to Tenant: $[amount]**

**Evidence Appendix**
- Move-in photos (dated)
- Move-out photos (dated)
- Vendor invoices (attached)
- Tenant correspondence

**Reasonableness Narrative**

Explain each deduction, confirming all charges represent actual costs incurred for tenant-caused damage beyond normal wear-and-tear. Address any borderline items and justify their inclusion or exclusion.
```

## 用法 / Usage
- 必填變數 / Variables: {{property-case-details}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Security Deposit Calculation Prompt for Landlords is a free AI prompt that produces detailed, legally defe…
