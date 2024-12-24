# Building a Summary Table from Multiple Excel Sheets

**Scenario**: A single Excel workbook contains sales data for multiple regions, each in a separate sheet. The user wants a consolidated summary.

---

## Step-by-Step Example

### 1. Load Data from All Sheets

Use the **Excel Helper** to load data from all sheets in the workbook.

```python
from python_analyst_utils.excel_management.excel_manager import ExcelSourceHelper

# Initialize the helper
excel_helper = ExcelSourceHelper()

# Load data from each sheet into a pandas DataFrame
file_path = "data/sales_data.xlsx"
sheet_names = ["North", "South", "East", "West"]

dataframes = []
for sheet in sheet_names:
    df = excel_helper.get_excel_data_as_dataframe(file_path, sheet_name=sheet)
    df["Region"] = sheet  # Add a column to identify the region
    dataframes.append(df)
```

---

### 2. Combine Data into a Single DataFrame

Use pandas to concatenate the DataFrames into a single table.

```python
import pandas as pd
```

# Combine all regional DataFrames

```python
consolidated_data = pd.concat(dataframes, ignore_index=True)
print(consolidated_data.head())
```

---

### 3. Save the Consolidated Data

Save the consolidated table to a new Excel file.

```python
from python_analyst_utils.csv_management.csv_helper import CsvSourceHelper

# Initialize the CSV Helper
csv_helper = CsvSourceHelper()

# Save the consolidated data
csv_helper.store_dataframe_as_csv("data/consolidated_sales_data.csv", consolidated_data)
```

---

## Summary

This example demonstrated:
1. Loading data from multiple sheets in an Excel file.
2. Combining the data into a single consolidated table.
3. Saving the final dataset for further use.
