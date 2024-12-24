# Python Analyst Utilities

**Python Analyst Utilities** is a comprehensive toolkit designed to simplify and enhance data analysis workflows in Python. It provides a collection of specialised utilities that abstract common, repetitive tasks, enabling you to focus on deriving insights and building robust solutions. Whether you're working with files, Excel sheets, CSVs, or pandas DataFrames, these tools streamline your processes and increase productivity.

---

## Key Features

### 📊 Excel and CSV Utilities

- **Excel Helper**: Simplify reading, writing, and manipulating Excel files.
- **CSV Helper**: Effortlessly load and store pandas DataFrames in CSV format, with support for storing directly in user-defined directories like the Downloads folder.

### 📂 File Management

- **File Storage Manager**: Manage file paths, create directories, and clear folder contents. Includes utilities to normalise paths, explore directory structures, and dynamically retrieve system folders like Documents and Downloads.

### 🔄 Data Transformation

- **Pandas Transformation Helper**: A powerful suite of tools for DataFrame transformations, including:
  - Column renaming, reordering, and type conversions.
  - Advanced cleaning utilities for removing duplicates, handling NaNs, and standardising content.
  - Sophisticated merging and appending methods for integrating multiple datasets.

### 📆 Date Format Detection

- **Date Format Detector**: Automatically identify date formats in strings or lists, making it easy to validate and standardise date data.

---

## Why Use Python Analyst Utilities?

- **Streamline Common Tasks**: Prebuilt functions eliminate boilerplate code for file management, data processing, and more.
- **Increase Productivity**: Focus on insights and solutions while the utilities handle repetitive operations.
- **Robust and Reliable**: Designed with error handling and flexibility for real-world scenarios.
- **Integrated**: Seamlessly integrates with pandas and other Python libraries to fit into your existing workflows.

---

## Getting Started

### Installation

Install the package with pip:

```bash
pip install python-analyst-utility
```

You can also find the library on [PyPI here](https://pypi.org/project/python-analyst-utility/).

---

## Utilities Overview

### 1. **Excel Helper**
Effortlessly manage Excel files with utilities to:

- Open, save, and refresh workbooks.
- Extract data into pandas DataFrames or from specific cells/ranges.

### 2. **CSV Helper**
Simplify operations on CSV files:

- Load CSVs into pandas DataFrames with robust error handling.
- Store DataFrames to user-defined paths or the Downloads folder.

### 3. **File Storage Manager**
Comprehensive file management utilities:

- Create folders and clear their contents.
- Dynamically locate system folders like Documents and Downloads.
- Print directory structures and normalise file paths for cross-platform compatibility.

### 4. **Pandas Transformation Helper**
A versatile utility for pandas DataFrame transformations:

- Perform diagnostic operations like retrieving column lists and printing metadata.
- Transform DataFrames by renaming, reordering, and converting column types.
- Clean and prepare data with methods to handle NaNs, duplicates, and formatting inconsistencies.
- Merge and append DataFrames with advanced options for field mappings.

### 5. **Date Format Detector**
Validate and standardise date strings:

- Automatically detect date formats in individual strings or lists.
- Support for a wide range of common date and time patterns.

---

## Quick Start Examples

#### Example 1: Working with Excel Files

```python
from python_analyst_utils.excel_management.excel_manager import ExcelSourceHelper

# Initialize the helper and open an Excel file
helper = ExcelSourceHelper()
data = helper.get_excel_data_as_dataframe("path/to/file.xlsx", sheet_name="Sheet1")
print(data)
```

#### Example 2: Cleaning Data with Pandas Helper

```python
from python_analyst_utils.pandas_management.pandas_transformation_helper import PandasTransformationHelper
import pandas as pd

# Initialize the helper
helper = PandasTransformationHelper()

# Example DataFrame
df = pd.DataFrame({"Name": [" Alice ", "Bob"], "Age": [30, None]})

# Clean the data
df_cleaned = helper.trim_values_in_columns(df, ["Name"])
df_cleaned = helper.replace_nas_with_zeros(df_cleaned, "Age")
print(df_cleaned)
```

#### Example 3: File Management

```python
from python_analyst_utils.file_management.file_storage_manager import FileStorageManager

# Initialize the manager and create a folder
manager = FileStorageManager()
manager.create_folder_if_doesnt_exist("path/to/new/folder")
```

#### Example 4: Detecting Date Formats

```python
from python_analyst_utils.date_format.date_detector import DateFormatDetector

# Detect format for a single date string
format_detected = DateFormatDetector.detect_format("2023-12-25")
print(f"Detected format: {format_detected}")
```

---

## Comprehensive Documentation

Explore the full functionality of **Python Analyst Utilities**:

- [Installation and Setup](reference/installation.md)
- [API Reference](reference/index.md)
- [Examples and Tutorials](examples/index.md)

---

## Get in Touch

Have questions, feedback, or suggestions? Feel free to reach out:

- [GitHub Repository](https://github.com/AroshaJ/python-analyst-utility)
- [Submit an Issue](https://github.com/AroshaJ/python-analyst-utility/issues)
- [PyPI package](https://pypi.org/project/python-analyst-utility/).

