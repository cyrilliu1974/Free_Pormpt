# Product Catalog CSV Generator for SEO & Batch Processing

## 簡介

The Product Catalog CSV Generator for SEO & Batch Processing is a free AI prompt that transforms product catalog information into a properly formatted CSV file with SEO-optimized fields for e-commerce professionals and data engineers. This product catalog prompt for ChatGPT takes raw product information and outputs a complete CSV file with eleven structured columns: product identifiers, names, descriptions, categories, features, pricing, images, meta titles, meta descriptions, and SEO-friendly URL slugs. It runs on ChatGPT, Claude, Gemini, and Grok, automatically formatting data with proper delimiters and character escaping while generating optimized metadata for each product entry. The prompt also delivers step-by-step batch processing instructions so teams can efficiently update hundreds or thousands of product listings at once. Reach for this prompt when you need to standardize product data for import into e-commerce platforms, content management systems, or when preparing catalog updates that require consistent SEO optimization across multiple products. ● Outputs a complete CSV schema with 11 essential columns covering product data, categorization, and SEO metadata ● Automatically generates optimized meta titles, meta descriptions, and URL slugs for each product entry ● Includes proper CSV formatting with correct delimiters and character escaping for error-free imports ● Provides batch processing instructions for efficiently updating large product catalogs across e-commerce platforms ## Prompt

```
## Role
You are an expert data engineer specializing in structured data formats, e-commerce product catalogs, and efficient batch processing workflows.

## Task
Generate a well-structured CSV file for the provided product catalog, optimized for batch processing of meta tags, descriptions, and URL slugs.

## Input
{{product-catalog}}

## CSV Schema
Create a CSV with these columns:
- `product_id`: Unique identifier
- `product_name`: Product name
- `product_description`: Detailed description
- `product_category`: Primary category
- `product_subcategory`: Subcategory (if applicable)
- `product_features`: Key features (semicolon-separated)
- `product_price`: Price
- `product_image_url`: Main image URL
- `meta_title`: SEO meta title
- `meta_description`: SEO meta description
- `url_slug`: SEO-friendly URL slug

## Output Requirements
- Use proper CSV formatting with appropriate delimiters and character escaping
- Validate data consistency and accuracy across all fields
- Include clear processing instructions for efficient batch updates of meta tags, descriptions, and URL slugs
- Focus on essential product features and categories without redundancy

## Format
Deliver the complete CSV file followed by step-by-step batch processing instructions.
```

## 用法 / Usage
- 必填變數 / Variables: {{product-catalog}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Product Catalog CSV Generator for SEO & Batch Processing is a free AI prompt that transforms product catal…
