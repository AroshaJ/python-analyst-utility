# Appending New Data to an Existing Dataset

**Scenario**: A user receives daily transaction files and wants to append them to an existing master dataset while ensuring no duplicates.

---

## Step-by-Step Example

### 1. Load the Existing Dataset

Use the **CSV Helper** to load the existing master dataset.

```python
from python_analyst_utils.csv_management.csv_helper import CsvSourceHelper

# Initialize the helper
csv_helper = CsvSourceHelper()

# Load the existing master dataset
master_data = csv_helper.get_dataframe_from_csv("data/master_dataset.csv")
print(master_data.head())
```

---

### 2. Load the New Data

Load the new daily transaction data.

# Load the new daily transaction data

```python
new_data = csv_helper.get_dataframe_from_csv("data/new_daily_transactions.csv")
print(new_data.head())
```

---

### 3. Append and Remove Duplicates

Use the **Pandas Transformation Helper** to append the new data to the master dataset and remove duplicates.

```python
from python_analyst_utils.pandas_management.pandas_transformation_helper import PandasTransformationHelper

# Initialize the helper
transformation_helper = PandasTransformationHelper()

# Append the new data
updated_data = transformation_helper.append_dataframes(master_data, new_data)

# Remove duplicates
updated_data = transformation_helper.remove_duplicate_rows(updated_data)
print(updated_data.head())
```

---

### 4. Save the Updated Dataset

Save the updated master dataset back to a CSV file.

```python
csv_helper.store_dataframe_as_csv("data/updated_master_dataset.csv", updated_data)
```

---

## Summary

This example demonstrated:
1. Loading an existing master dataset.
2. Loading new transaction data.
3. Appending the new data while ensuring no duplicates.
4. Saving the updated dataset.
