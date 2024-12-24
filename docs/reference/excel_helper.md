# Excel Helper

The **Excel Helper Utility** is a powerful and user-friendly tool designed to simplify the process of working with Excel files in Python. It provides a robust set of methods for performing common operations, such as reading and writing data, managing workbooks, refreshing connections, and extracting data into pandas DataFrames.

Whether you're handling complex Excel operations or just need a quick way to automate repetitive tasks, the Excel Helper Utility streamlines your workflow and integrates seamlessly with existing analytics pipelines.

---

## Key Features

### 🧰 File Management
- Open, close, and save Excel workbooks programmatically.
- Retrieve lists of Excel files from a specified directory.
- Automatically identify the first Excel file in a folder.

### 📊 Data Extraction
- Load data from entire sheets or specific ranges into pandas DataFrames.
- Extract values from specific cells or ranges within a sheet.
- Handle large Excel datasets efficiently with built-in support for **openpyxl** and **xlwings**.

### 🔄 Data Refreshing
- Refresh all connections in a workbook programmatically to ensure your data is up-to-date.

---

## Getting Started

### Installation

Ensure you have the required dependencies installed. Install the **Python Analyst Utilities** package using pip:

```bash
pip install python-analyst-utility
```

## Quick Start
Here’s how to use the Excel Helper Utility:

### 1. Open and Save an Excel Workbook

```python
from python_analyst_utils.excel_management.excel_manager import ExcelSourceHelper

# Initialize the helper
excel_helper = ExcelSourceHelper()

# Open an Excel workbook
workbook = excel_helper.open_excel_workbook("path/to/excel/file.xlsx", show_sheet=True)

# Perform operations...

# Save changes
excel_helper.save_workbook_in_place()

# Close the workbook
excel_helper.close_workbook()
```

### 2. Load Data into a DataFrame

```python
from python_analyst_utils.excel_management.excel_manager import ExcelSourceHelper

# Initialize the helper
excel_helper = ExcelSourceHelper()

# Load data from a sheet into a pandas DataFrame
data = excel_helper.get_excel_data_as_dataframe("path/to/excel/file.xlsx", sheet_name="Sheet1")
print(data)
```

### 3. Extract Data from a Specific Range

```python
from python_analyst_utils.excel_management.excel_manager import ExcelSourceHelper

# Initialize the helper
excel_helper = ExcelSourceHelper()

# Extract data from a fixed range
data = excel_helper.extract_data_from_fixed_range(
    "path/to/excel/file.xlsx",
    sheet_name="Sheet1",
    column_range="A:C",
    first_row=2,
    rows_to_extract=10
)
print(data)
```

## API Reference
Below is the complete API reference for the Excel Helper Utility, including all methods and their documentation.

---

::: python_analyst_utils.excel_management.excel_manager

