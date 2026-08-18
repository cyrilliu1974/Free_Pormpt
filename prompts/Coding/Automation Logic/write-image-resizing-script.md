# Image Resizing Script Generator

## 簡介

The Image Resizing Script Generator is a free AI prompt that creates production-ready batch image processing scripts for developers and automation engineers. This image resizing script prompt for ChatGPT, Claude, and Cursor produces complete, commented code in your chosen language (Python, JavaScript/Node.js, or Bash with ImageMagick) that processes thousands of images while maintaining quality, preserving aspect ratios, and organizing outputs with timestamped folders. The generated script supports JPEG, PNG, WebP, GIF, and TIFF formats, applies content-aware compression (different algorithms for photographs versus graphics), handles corrupted files gracefully, and never overwrites source files unless explicitly instructed. Real-world applications include preparing image assets for responsive websites, batch-processing client photography, optimizing e-commerce product images, and converting print materials for web delivery. Reach for this prompt when you need a reliable, memory-safe image processing pipeline that balances web performance with print-quality standards across diverse projects. ● Produces scripts with intelligent compression selection based on content type, preserving quality for photographs while minimizing file size for graphics ● Includes input validation, aspect ratio calculations, queue management, and memory-safe batch processing for large image volumes ● Generates timestamped output folders, clear file naming conventions, and detailed logging that tracks progress and errors without halting operations ● Provides usage examples, configuration variables, and troubleshooting sections that make the script immediately deployable in production environments ## Prompt

```
## Role

You are an automation architect specializing in image processing workflows, combining batch automation with expertise in image quality preservation, compression algorithms, and responsive design principles.

## Task

Create a production-ready image resizing script that handles batch processing while maintaining quality, preserving aspect ratios, and organizing outputs efficiently. The script must support multiple formats, intelligent compression, error recovery, and clear progress feedback.

## Context

The script will process large volumes of images across different formats for multiple projects with varying requirements. It must balance web performance optimization with print-quality standards, handle diverse source materials consistently, and work within storage constraints.

Key requirements:
- Process thousands of images without memory overflow
- Maintain aspect ratios by default (override only when explicitly requested)
- Apply intelligent compression based on content type (photographs vs. graphics)
- Support JPEG, PNG, WebP, GIF, and TIFF with format-specific handling
- Gracefully handle corrupted files and permission errors without stopping batch operations
- Never overwrite source files unless explicitly requested
- Preserve metadata when appropriate
- Create timestamped output folders with clear naming conventions

{{image-processing-requirements}} should specify: source folder paths or file paths, target dimensions (e.g., 1920×1080) or scaling percentage (e.g., 50%), preferred output format (or "same as source"), quality preference (maximum quality / balanced / minimum file size), and output folder location.

{{preferred-language}} specifies the programming language to use (e.g., Python, JavaScript/Node.js, Bash with ImageMagick).

## Output

Provide a complete, commented script structured in these sections:

**1. Installation Requirements**
List all dependencies and installation commands.

**2. Configuration Variables**
Define user-configurable settings at the top of the script.

**3. Input Validation**
Verify source locations, validate dimensions/scaling factors, check format compatibility.

**4. Processing Logic**
Implement aspect ratio calculations, content-based compression selection, quality preservation algorithms. Support both percentage-based scaling and fixed dimensions.

**5. Batch Processing Engine**
Handle multiple images efficiently with queue management, progress tracking, and memory-safe operations.

**6. Output Organization**
Create folders named by timestamp and operation (e.g., "2024-01-15_resize_1920x1080"), implement clear file naming conventions.

**7. Error Handling**
Catch and log issues (corrupted files, unsupported formats, permissions) while continuing batch processing.

**8. Usage Examples**
Provide basic usage commands and advanced customization examples.

**9. Troubleshooting Guide**
Address common issues and their solutions.

Use code blocks with syntax highlighting. Add detailed inline comments explaining logic, especially for compression algorithm selection and aspect ratio preservation.
```

## 用法 / Usage
- 必填變數 / Variables: {{image-processing-requirements}}、{{preferred-language}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Skill_Prompt_Spec_Extractor
- 適用 / Use when: The Image Resizing Script Generator is a free AI prompt that creates production-ready batch image processing s…
