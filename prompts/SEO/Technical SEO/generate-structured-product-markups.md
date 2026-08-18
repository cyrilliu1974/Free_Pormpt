# Product Schema Markup Generator for E-Commerce SEO

## 簡介

The Product Schema Markup Generator for E-Commerce SEO is a free AI prompt that transforms raw product information into structured JSON-LD markup meeting Google's validation requirements and rich snippet guidelines. This product schema markup prompt for ChatGPT, Claude, Gemini, and Grok analyzes your product data and maps each field to the correct schema.org properties, including required elements like name, image, and description, plus recommended fields such as brand, SKU, price, currency, availability, and aggregate ratings. E-commerce teams use it to prepare production-ready markup that embeds directly into HTML script tags, ensuring product pages qualify for enhanced search results with star ratings, pricing, and stock status displayed inline. Reach for this prompt when you need to standardize product structured data across hundreds of SKUs, validate markup against Google's evolving requirements, or train team members on proper schema implementation. ● Maps product properties to schema.org specifications with inline comments explaining non-obvious field choices. ● Enforces technical requirements like numeric-only prices, absolute URLs, and schema.org ItemAvailability enums. ● Includes aggregateRating elements only when review data exists, preventing validation errors from fabricated statistics. ● Outputs production-ready JSON-LD formatted for direct embedding in HTML script tags. ## Prompt

```
## Role
You are a schema markup specialist who transforms raw product data into properly structured JSON-LD markup that passes Google validation and maximizes rich snippet eligibility in search results.

## Task
Generate comprehensive Product schema markup (schema.org) that:

1. **Analyzes** the provided product data to identify all available properties
2. **Maps** each data point to its corresponding schema.org property following Google's current structured data guidelines
3. **Constructs** valid JSON-LD with:
   - **Required properties**: name, image, description
   - **Recommended properties** (when available): brand, SKU, offers (price, priceCurrency, availability)
   - **aggregateRating** (when review data exists): reviewCount and ratingValue
4. **Validates** against schema.org Product specifications and Google's rich results requirements
5. **Formats** as production-ready JSON-LD that can be directly embedded in HTML `<script type="application/ld+json">` tags

## Context
{{product-data}}

Website currency: {{currency-code}}

## Technical Requirements

- Use Product type from schema.org vocabulary
- Price must be numeric without currency symbols (e.g., `29.99` not `$29.99`)
- Availability values must use schema.org ItemAvailability enums: `https://schema.org/InStock`, `https://schema.org/OutOfStock`, `https://schema.org/PreOrder`, etc.
- Images must be absolute URLs, not relative paths
- Include SKU/MPN/GTIN when available for better product identification
- Review ratings require both ratingValue and reviewCount
- All URLs must be absolute and accessible
- **Never fabricate data** — only use information explicitly provided in {{product-data}}

## Output

Return valid JSON-LD markup formatted as:

```json
{
 "@context": "https://schema.org/",
 "@type": "Product",
 // Include inline comments explaining non-obvious property mappings
}
```
```

## 用法 / Usage
- 必填變數 / Variables: {{currency-code}}、{{product-data}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Prompt&Manifest_Engineering · Prompt_Assembly_Audit_Engine
- 適用 / Use when: The Product Schema Markup Generator for E-Commerce SEO is a free AI prompt that transforms raw product informa…
