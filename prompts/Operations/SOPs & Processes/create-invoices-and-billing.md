# Invoice and Billing Statement Generator

## 簡介

The Invoice and Billing Statement Generator is a free AI prompt that creates accurate, client-ready invoices and billing statements for businesses of any size. This invoice prompt for ChatGPT produces a complete, professionally formatted billing document with a header containing business and client information, a structured line-items table showing dates, service descriptions, quantities, rates, and totals, and a financial summary with subtotals, applicable taxes by jurisdiction, and the final amount due. It runs on ChatGPT, Claude, Gemini, and Grok, and outputs markdown-formatted invoices that are immediately ready to send or convert to PDF. Common use cases include freelance billing, consulting engagements, service businesses, and any scenario where you need a structured, error-free invoice with consistent number formatting and clear payment terms. ● Builds a complete header with unique invoice number, date, business details, and client name ● Generates a formatted table for services rendered, with columns for date, description, quantity, rate, and line-item totals ● Calculates subtotals, applies tax rates with jurisdiction labels, and computes the final amount due with transparent math ● Includes payment terms, accepted methods, and due dates in a clear footer section ## Prompt

```
## Role
You are a financial administrator creating professional invoices and billing statements.

## Task
Generate an accurate, detailed invoice for the client specified below. The invoice must include:

- **Header**: Business name, contact information, invoice number, date, and client name
- **Line items table** with columns: Date | Service Description | Quantity | Rate | Total Amount
- **Financial summary**: Subtotal, applicable taxes (specify rate and jurisdiction), and final total
- **Footer**: Payment terms, accepted payment methods, and due date

## Requirements
- All calculations must be accurate and clearly shown
- Use consistent formatting throughout (align currency, use proper number formatting)
- Present the output as a professional invoice layout using markdown tables and formatting
- Ensure the document is ready to send to the client

## Context
**Business**: {{business-name-and-type}}
**Client**: {{client-name}}
**Services rendered**: {{services-with-dates-quantities-rates}}
**Payment terms**: {{payment-terms-and-methods}}
```

## 用法 / Usage
- 必填變數 / Variables: {{business-name-and-type}}、{{client-name}}、{{payment-terms-and-methods}}、{{services-with-dates-quantities-rates}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Human_In_Loop_Workflow_Engineering · Prompt_Assembly_Integrity_Protocol
- 適用 / Use when: The Invoice and Billing Statement Generator is a free AI prompt that creates accurate, client-ready invoices a…
