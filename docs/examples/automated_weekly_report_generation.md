# Automating Weekly Report Generation

**Scenario**: Generate a summary report of sales data every week, save it as an Excel file, and clean up old reports from the directory.

---

## Step-by-Step Example

### 1. Load the Weekly Sales Data

Use the **CSV Helper** to load the latest weekly sales data into a pandas DataFrame.

```python
from python_analyst_utils.csv_management.csv_helper import CsvSourceHelper

# Initialize the helper
csv_helper = CsvSourceHelper()
```

# Load the weekly sales data

```python
weekly_sales = csv_helper.get_dataframe_from_csv("data/weekly_sales.csv")
print(weekly_sales.head())
```

---

### 2. Clean and Transform the Data

Use the **Pandas Transformation Helper** to clean and prepare the data for reporting.

```python
from python_analyst_utils.pandas_management.pandas_transformation_helper import PandasTransformationHelper

# Initialize the helper
transformation_helper = PandasTransformationHelper()

# Clean data: trim whitespace and handle NaNs
weekly_sales = transformation_helper.trim_values_in_columns(weekly_sales, ["ProductName", "Region"])
weekly_sales = transformation_helper.replace_nas_with_zeros(weekly_sales, "Sales")

print(weekly_sales.head())
```

---

### 3. Save the Report

Use the **Excel Helper** to save the cleaned data as an Excel file.

```python
from python_analyst_utils.excel_management.excel_manager import ExcelSourceHelper

# Initialize the helper
excel_helper = ExcelSourceHelper()
```

# Save the data to an Excel file

```python
excel_helper.store_dataframe_as_csv_in_downloads_folder("weekly_sales_report.xlsx", weekly_sales)
```

---

### 4. Clean Up Old Reports

Use the **File Storage Manager** to remove outdated reports from the folder.

```python
from python_analyst_utils.file_management.file_storage_manager import FileStorageManager
```

# Initialize the file manager

```python
file_manager = FileStorageManager()

# Define the reports directory
reports_directory = "data/reports"


# Clear all contents of the folder
file_manager.clear_all_contents_of_folder(reports_directory)
```

---

## Summary

This example demonstrated:
1. Loading weekly sales data from a CSV file.
2. Cleaning and transforming the data.
3. Saving the report as an Excel file in the downloads directory.
4. Removing outdated reports to maintain a clean directory.
