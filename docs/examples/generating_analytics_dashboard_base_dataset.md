# Generating an Analytics Dashboard Base Dataset

**Scenario**: A user wants to create a clean, ready-to-use dataset for a Power BI dashboard.

---

## Step-by-Step Example

### 1. Load the Raw Data

Use the **CSV Helper** to load the raw data into a pandas DataFrame.

```python
from python_analyst_utils.csv_management.csv_helper import CsvSourceHelper

# Initialize the helper
csv_helper = CsvSourceHelper()

# Load the raw dataset
raw_data = csv_helper.get_dataframe_from_csv("data/raw_dashboard_data.csv")
print(raw_data.head())
```

---

### 2. Clean and Transform the Data

Use the **Pandas Transformation Helper** to clean and prepare the data for the dashboard.

```python
from python_analyst_utils.pandas_management.pandas_transformation_helper import PandasTransformationHelper

# Initialize the helper
transformation_helper = PandasTransformationHelper()

# Clean the data
cleaned_data = transformation_helper.trim_values_in_columns(raw_data, ["ProductName", "Region"])
cleaned_data = transformation_helper.replace_nas_with_zeros(cleaned_data, "Sales")
cleaned_data = transformation_helper.clear_nans(cleaned_data)

# Add calculated fields if necessary (e.g., Total Sales)
cleaned_data["TotalSales"] = cleaned_data["Sales"].astype(float) * cleaned_data["Quantity"].astype(float)

print(cleaned_data.head())
```

---

### 3. Save the Prepared Data

Save the cleaned and transformed dataset to a file for Power BI import.

```python
csv_helper.store_dataframe_as_csv("data/cleaned_dashboard_data.csv", cleaned_data)
```

---

## Summary

This example demonstrated:
1. Loading raw data for an analytics dashboard.
2. Cleaning and transforming the data for analysis.
3. Saving the prepared dataset for Power BI or other tools.
