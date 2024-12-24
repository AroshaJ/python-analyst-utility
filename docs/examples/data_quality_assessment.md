# Data Quality Assessment

**Scenario**: Assess the quality of a dataset by identifying missing values, invalid types, and duplicates.

---

## Step-by-Step Example

### 1. Load the Dataset

Use the **CSV Helper** to load the dataset into a pandas DataFrame.

```python
from python_analyst_utils.csv_management.csv_helper import CsvSourceHelper

# Initialize the helper
csv_helper = CsvSourceHelper()

# Load the dataset
data = csv_helper.get_dataframe_from_csv("data/quality_check_dataset.csv")
print(data.head())
```

---

### 2. Identify Missing Values

Use the **Pandas Transformation Helper** to identify columns with missing values.

```python
from python_analyst_utils.pandas_management.pandas_transformation_helper import PandasTransformationHelper

# Initialize the helper
transformation_helper = PandasTransformationHelper()

# Identify missing values
missing_values_report = data.isnull().sum()
print("Missing Values Report:")
print(missing_values_report)
```

---

### 3. Verify and Convert Data Types

Use the **Pandas Transformation Helper** to verify and convert columns to the correct data types.

```python
# Change specific columns to numeric type
data = transformation_helper.change_field_to_number(data, ["Sales", "Profit"], replace_errors_with_0=True)

# Convert date columns to datetime
data = transformation_helper.change_field_to_datetime(data, ["TransactionDate"], date_time_format="%Y-%m-%d")

print(data.dtypes)
```

---

### 4. Remove Duplicates

Use the **Pandas Transformation Helper** to remove duplicate rows from the dataset.

```python
data = transformation_helper.remove_duplicate_rows(data)
print(f"Dataset after removing duplicates: {data.shape}")
```

---

### 5. Save the Cleaned Data

Use the **CSV Helper** to save the cleaned dataset to a new CSV file.

```python
csv_helper.store_dataframe_as_csv("data/cleaned_quality_check_dataset.csv", data)
```

---

## Summary

This example demonstrated:
1. Loading a dataset into a pandas DataFrame.
2. Identifying missing values.
3. Verifying and converting data types to ensure consistency.
4. Removing duplicate rows.
5. Saving the cleaned data to a new file.

