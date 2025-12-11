# Standard Notebook Template

This document defines the standard structure and formatting for all training notebooks in this project. All new notebooks should follow this template to ensure consistency.

## File Naming Convention
- Format: `XX_topic_name.ipynb`
- Example: `11_bi_analytics.ipynb`, `07_streaming_incremental.ipynb`

## Notebook Structure

Every notebook must contain the following sections in this specific order:

### 1. Header Cell (Markdown)
Contains the title, objective, and list of topics.

```markdown
# <Number>. <Title>

**Training Objective:** <Concise description of what the student will learn>

**Topics Covered:**
- <Topic 1>
- <Topic 2>
- <Topic 3>
```

### 2. Setup Section Header (Markdown)
Standard header for the setup block.

```markdown
## <Number>.1. Setup and Configuration
```

### 3. Theoretical Introduction (Markdown)
Brief introduction to the concepts covered.

```markdown
## <Number>.2. Theoretical Introduction

**Section Objective:** <What conceptual understanding will be gained>

**Basic Concepts:**
- **<Concept 1>**: <Definition>
- **<Concept 2>**: <Definition>
```

### 4. User Isolation (Markdown + Python)
Loads the global setup script to handle user-specific paths and variables.

**Markdown:**
```markdown
## <Number>.3. User Isolation
```

**Python:**
```python
%run ../00_setup
```

### 5. Environment Configuration (Markdown + Python)
Sets the current catalog and schema, and imports necessary libraries.

**Markdown:**
```markdown
## <Number>.4. Environment Configuration
```

**Python:**
```python
import <library>
from pyspark.sql import functions as F

# Set catalog and schema
spark.sql(f"USE CATALOG {CATALOG}")
spark.sql(f"USE SCHEMA {TARGET_SCHEMA}") # e.g., GOLD_SCHEMA, SILVER_SCHEMA

display(spark.createDataFrame([
    ("Catalog", CATALOG),
    ("Schema", TARGET_SCHEMA)
], ["Parameter", "Value"]))
```

### 6. Content Sections (Markdown + Code)
The main body of the notebook. Divide content into logical sections.

**Markdown:**
```markdown
## Section 1: <Topic Name>

<Introductory text explaining the concept or step>
```

**Python/SQL:**
```python
# Code implementation
```

### 7. Summary (Markdown)
Recap of what was achieved in the notebook.

```markdown
## Summary

1. <Recap point 1>
2. <Recap point 2>
3. <Recap point 3>
```

### 8. Cleanup (Markdown + Python)
Instructions or code to clean up resources created during the session.

**Markdown:**
```markdown
## Clean up resources
```

**Python:**
```python
# spark.sql(f"DROP TABLE IF EXISTS ...")
display(spark.createDataFrame([("Status", "Resources kept for further exercises")], ["Info", "Value"]))
```

## Best Practices
- **Cell Granularity**: Keep cells focused on a single task or concept.
- **Comments**: Use comments in code to explain *why*, not just *what*.
- **Display**: Use `display()` for DataFrames instead of `show()`.
- **Variables**: Use variables from `00_setup` (e.g., `CATALOG`, `username`) instead of hardcoding paths.
