# Standardising Date Formats Across Datasets

**Scenario**: A user needs to standardise inconsistent date formats in a large dataset.

---

## Step-by-Step Example

### 1. Load the Dataset

Use the **CSV Helper** to load the dataset into a pandas DataFrame.

```python
from python_analyst_utils.csv_management.csv_helper import CsvSourceHelper

# Initialize the helper
csv_helper = CsvSourceHelper()
```

# Load the dataset

```python
data = csv_helper.get_dataframe_from_csv("data/mixed_date_formats.csv")
print(data.head())
```

---

### 2. Detect Date Formats

Use the **Date Helper** to detect the date format of each column with inconsistent dates.

```python
from python_analyst_utils.date_management.date_manager import DateFormatDetector

# Initialize the detector
detector = DateFormatDetector()

# Detect format for a sample column
date_column = data["TransactionDate"].dropna().tolist()
detected_format = detector.detect_format(date_column)

print(f"Detected Format: {detected_format}")
```

---

### 3. Standardise the Date Format

Use the **Pandas Transformation Helper** to convert the detected formats into a standard format (`YYYY-MM-DD`).

```python
from python_analyst_utils.pandas_management.pandas_transformation_helper import PandasTransformationHelper

# Initialize the helper
transformation_helper = PandasTransformationHelper()

# Convert dates to a standard format
data = transformation_helper.change_field_to_datetime(data, ["TransactionDate"], date_time_format="%Y-%m-%d")
print(data.head())
```

---

### 4. Save the Standardised Dataset

Use the **CSV Helper** to save the updated dataset to a new CSV file.

```python
csv_helper.store_dataframe_as_csv("data/standardised_date_formats.csv", data)
```

---

## Summary

This example demonstrated:
1. Detecting date formats from a column with mixed date formats.
2. Standardising the dates into a uniform format.
3. Saving the updated dataset for further use.
