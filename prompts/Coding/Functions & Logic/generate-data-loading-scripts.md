# Data Loading Script Generator for Python

## 簡介

The Data Loading Script Generator for Python is a free AI prompt that creates production-ready data ingestion scripts for data engineers and Python developers working with large datasets. This data loading prompt for ChatGPT produces complete, executable Python code that handles CSV, JSON, Parquet, and Excel files with memory-efficient chunking, explicit dtype specification, and lazy loading strategies. The generated scripts include automatic file type detection through extension and content sniffing, comprehensive error handling for encoding issues and malformed data, real-time progress bars, detailed logging, and data quality checks with summary statistics. It runs on ChatGPT, Claude, and Cursor to deliver modular, maintainable code with clear function separation and inline documentation. Use this prompt when you need scalable data pipeline architecture that goes beyond toy datasets and handles real-world data challenges like corrupt files, memory constraints, and encoding problems. ● Automatic file format detection with support for CSV, JSON, Parquet, and Excel through extension matching and content validation ● Memory optimization through pandas chunking, strategic column selection, dtype specification, lazy evaluation, and garbage collection ● Production-grade error handling for encoding problems, malformed records, missing files, and corrupt data with graceful fallbacks ● Real-time feedback via progress bars and structured logging, plus data quality checks and summary statistics after successful load ## Prompt

```
## Role
You are an expert data engineer and Python developer specializing in scalable data pipeline architecture and production-grade data ingestion.

## Task
Generate a complete, executable Python script that loads data with production-level robustness: memory-efficient chunking for large files, explicit dtype specification, lazy loading strategies, graceful encoding and missing-value handling, automatic file type detection, comprehensive error handling for corrupt data, and real-time progress feedback via logging and progress bars.

## Context
Modern data ingestion must scale beyond toy datasets. The script should be modular and maintainable, support multiple formats (CSV, JSON, Parquet, Excel), optimize memory through strategic column selection and garbage collection, and provide data quality checks and summary statistics upon successful loading.

{{data-specification}}

## Output
Deliver a complete, executable Python script with:
- Automatic file type detection (extension + content sniffing)
- Memory-efficient loading functions using pandas chunking, appropriate dtypes, and lazy evaluation
- Comprehensive error handling for encoding problems, malformed data, and missing files
- Progress bars and detailed logging for large file processing
- Data type optimization and garbage collection
- Data quality checks and summary statistics
- Detailed inline comments and modular functions that can be easily customized

Structure the script with clear function separation and include usage examples in comments.
```

## 用法 / Usage
- 必填變數 / Variables: {{data-specification}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Prompt&Manifest_Engineering · Manifest_Driven_Code_Skeleton_Generator
- 適用 / Use when: The Data Loading Script Generator for Python is a free AI prompt that creates production-ready data ingestion …
