# Combining CSV and Excel Data

**Scenario**: Combine sales data from multiple CSV files and an Excel file containing metadata for a comprehensive report.

---

## Step-by-Step Example

### 1. Load CSV Files

Use the **CSV Helper** to load multiple CSV files into pandas DataFrames.

```python
from python_analyst_utils.csv_management.csv_helper import CsvSourceHelper

# Initialize the helper
csv_helper = CsvSourceHelper()

# Load CSV files
sales_data_file1 = csv_helper.get_dataframe_from_csv("data/sales_data1.csv")
sales_data_file2 = csv_helper.get_dataframe_from_csv("data/sales_data2.csv")

# Combine the datasets
combined_sales_data = sales_data_file1.append(sales_data_file2, ignore_index=True)
print(combined_sales_data.head())
```

---

### 2. Load Excel Metadata

Use the **Excel Helper** to extract metadata from the Excel file.

```python
from python_analyst_utils.excel_management.excel_manager import ExcelSourceHelper

# Initialize the helper
excel_helper = ExcelSourceHelper()

# Load the metadata file
metadata = excel_helper.get_excel_data_as_dataframe("data/metadata.xlsx", sheet_name="Metadata")
print(metadata.head())
```

---

### 3. Merge the Datasets

Merge the sales data with the metadata using the **Pandas Transformation Helper**.

```python
from python_analyst_utils.pandas_management.pandas_transformation_helper import PandasTransformationHelper

# Initialize the helper
transformation_helper = PandasTransformationHelper()

# Merge the datasets on a common field
merged_data = transformation_helper.left_merge_dataframes(
    left_dataframe=combined_sales_data,
    right_dataframe=metadata,
    common_field_name="ProductID"
)

print(merged_data.head())
```

---

### 4. Save the Final Dataset

Save the final merged dataset to a new CSV file.

```python
csv_helper.store_dataframe_as_csv("data/final_sales_report.csv", merged_data)
```

---

## Summary

This example demonstrated:
1. Loading multiple CSV files into a single pandas DataFrame.
2. Extracting metadata from an Excel file.
3. Merging datasets using a common field.
4. Saving the final dataset for further use.
