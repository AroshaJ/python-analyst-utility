# Pandas Transformation Helper

The **Pandas Transformation Helper** utility provides a comprehensive set of methods for transforming and analysing pandas DataFrames. It consolidates various functionalities into a single utility, delegating specific tasks to specialised helper classes. This makes it a one-stop solution for working with DataFrames in Python.

---

## Key Features

### 🕵️‍♂️ Diagnostic Tools
- Retrieve and print detailed information about DataFrame dimensions and columns.
- Quickly inspect the structure and metadata of a DataFrame.

### 📋 Column Management
- Add, remove, rename, and reorder columns with ease.
- Flexible tools for renaming all columns or selectively modifying specific ones.

### 📆 Type Conversions
- Convert columns to datetime, date, or numeric types with error handling.
- Support for custom date formats and default replacements for invalid conversions.

### 🧹 Data Cleaning
- Remove special characters, line breaks, and unnecessary rows or columns.
- Handle missing data by replacing NaNs with specific values or filtering them out entirely.

### 🔄 Merging and Appending
- Perform advanced merges, including left joins, multi-field joins, and custom field mappings.
- Easily append one DataFrame to another.

---

## Getting Started

### Installation

Make sure the **Python Analyst Utilities** package is installed:

```bash
pip install python-analyst-utility
```

---

## Quick Start

Here’s how you can get started with the **Pandas Transformation Helper** utility:

#### 1. Retrieve DataFrame Information

```python
from python_analyst_utils.pandas_management.pandas_transformation_helper import PandasTransformationHelper
import pandas as pd

# Initialize the helper
helper = PandasTransformationHelper()

# Example DataFrame
data = {"Name": ["Alice", "Bob"], "Age": [30, 25]}
df = pd.DataFrame(data)

# Print dimensions and general information
helper.print_dataframe_dimensions(df)
helper.print_general_info_about_dataframe(df)
```

#### 2. Rename Columns

```python
# Rename specific columns
renamed_df = helper.rename_columns(df, {"Name": "Full Name", "Age": "Years"})
print(renamed_df)
```

#### 3. Convert Column Types

```python
# Convert columns to numeric or datetime
df_with_dates = pd.DataFrame({"Date": ["2023-12-01", "2023-12-02"]})
converted_df = helper.change_field_to_datetime(df_with_dates, ["Date"])
print(converted_df)
```

#### 4. Clean Data

```python
# Replace NaN values with zeros
cleaned_df = helper.replace_nas_with_zeros(df, "Age")
print(cleaned_df)
```

#### 5. Merge Two DataFrames

```python
# Merge two DataFrames using a common field
df1 = pd.DataFrame({"ID": [1, 2], "Value": [10, 20]})
df2 = pd.DataFrame({"ID": [1, 2], "Description": ["A", "B"]})
merged_df = helper.left_merge_dataframes(df1, df2, "ID")
print(merged_df)
```

---

## How It Works

### Modular Design
The utility leverages specialised helper classes for different functionalities:
- **Diagnostic Helper**: Methods for inspecting DataFrame structure and metadata.
- **Column Helper**: Tools for managing columns (e.g., renaming, reordering).
- **Type Helper**: Handles type conversions for DataFrame fields.
- **Content Helper**: Deals with content-specific tasks like handling NaNs and replacing values.
- **Cleaning Helper**: Includes methods for cleaning data, such as trimming whitespace or removing line breaks.
- **Merge Helper**: Advanced tools for merging and appending DataFrames.

### Flexible Error Handling
- Most methods return a transformed DataFrame or `None` if an error occurs.
- Clear error messages help in debugging issues during transformations.

### Advanced Merging
- Support for multi-field merges and custom field mappings.
- Option to add indicators for merge operations.

---

## API Reference

Below is the API reference for the **Pandas Transformation Helper** utility.

::: python_analyst_utils.pandas_management.pandas_transformation_helper
