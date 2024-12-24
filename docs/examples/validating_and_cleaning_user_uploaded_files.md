# Validating and Cleaning User-Uploaded Files

**Scenario**: Validate user-uploaded CSV files for a web application, ensuring they meet schema requirements.

---

## Step-by-Step Example

### 1. Validate File Existence

Use the **File Storage Manager** to check if the uploaded file exists.

```python
from python_analyst_utils.file_management.file_storage_manager import FileStorageManager
```

# Initialize the file manager

```python
file_manager = FileStorageManager()
```

# Check if the file exists
```python
uploaded_file_path = "uploads/user_file.csv"
if not file_manager.does_file_exist(uploaded_file_path):
    raise FileNotFoundError(f"Uploaded file not found: {uploaded_file_path}")
```
---

### 2. Load and Validate the File

Use the **CSV Helper** to load the uploaded file and validate its schema.

```python
from python_analyst_utils.csv_management.csv_helper import CsvSourceHelper

# Initialize the helper
csv_helper = CsvSourceHelper()

# Load the file
uploaded_data = csv_helper.get_dataframe_from_csv(uploaded_file_path)

# Validate schema
expected_columns = ["Name", "Email", "Age", "SignupDate"]
if not set(expected_columns).issubset(uploaded_data.columns):
    raise ValueError("Uploaded file is missing required columns.")

print(uploaded_data.head())
```

---

### 3. Clean the Data

Use the **Pandas Transformation Helper** to clean the uploaded data.

```python
from python_analyst_utils.pandas_management.pandas_transformation_helper import PandasTransformationHelper

# Initialize the helper
transformation_helper = PandasTransformationHelper()

# Clean and validate data
cleaned_data = transformation_helper.clear_nans(uploaded_data)
cleaned_data = transformation_helper.change_field_to_number(cleaned_data, ["Age"])
cleaned_data = transformation_helper.change_field_to_datetime(cleaned_data, ["SignupDate"], date_time_format="%Y-%m-%d")

print(cleaned_data.head())

```

---

## Summary

This example demonstrated:
1. Validating the existence of an uploaded file.
2. Ensuring the file meets schema requirements.
3. Cleaning and transforming the uploaded data for further processing.
