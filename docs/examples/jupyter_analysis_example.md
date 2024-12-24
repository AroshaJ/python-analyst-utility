# Full Example: Data Cleaning and Analytics in Jupyter Notebook

This page demonstrates how to use **Python Analyst Utilities** in a Jupyter Notebook to load a large dataset from a CSV file, clean it using the **Pandas Transformation Helper**, and perform basic analytics. The example assumes the dataset contains missing values, improperly formatted columns, and redundant data that needs to be cleaned before analysis.

---

## Prerequisites

Ensure the **Python Analyst Utilities** package is installed:

```bash
pip install python-analyst-utility
```

You also need to install the following dependencies if they are not already available:

```bash
pip install pandas jupyter
```

---

## Step-by-Step Example

### 1. Load the CSV File into a pandas DataFrame

First, we load the dataset into a pandas DataFrame using the **CSV Helper** utility.

```python
from python_analyst_utils.csv_management.csv_helper import CsvSourceHelper

# Initialize the helper
csv_helper = CsvSourceHelper()

# Load the CSV file
file_path = \"data/large_dataset.csv\"
data = csv_helper.get_dataframe_from_csv(file_path)

# Preview the data
print(data.head())
```

---

### 2. Inspect the Data

Use the **Pandas Transformation Helper** to inspect the DataFrame’s structure and metadata.

```python
from python_analyst_utils.pandas_management.pandas_transformation_helper import PandasTransformationHelper

# Initialize the helper
transformation_helper = PandasTransformationHelper()

# Print general information about the DataFrame
transformation_helper.print_general_info_about_dataframe(data)

# Print a list of columns
transformation_helper.print_list_of_columns(data)
```

---

### 3. Clean the Data

#### a. Trim Whitespace and Remove Special Characters

Clean up the column values by trimming leading/trailing whitespace and removing special characters.

```python
# Clean specific columns
columns_to_clean = [\"Name\", \"Address\"]
data = transformation_helper.trim_values_in_columns(data, columns_to_clean)
data = transformation_helper.remove_special_characters_from_column(data, \"Name\")
```

#### b. Handle Missing Values

Replace missing values (NaNs) with appropriate defaults.

```python
# Replace NaN values in numeric columns with zeros
data = transformation_helper.replace_nas_with_zeros(data, \"Salary\")

# Remove rows where critical columns are empty
data = transformation_helper.filter_out_nas_and_blanks(data, \"EmployeeID\")
```

#### c. Remove Duplicate Rows

Eliminate duplicate rows to ensure clean data for analysis.

```python
data = transformation_helper.remove_duplicate_rows(data)
```

---

### 4. Transform Data

#### a. Rename and Reorder Columns

Rename columns for clarity and reorder them for consistency.

```python
# Rename columns
data = transformation_helper.rename_columns(data, {\"EmpID\": \"EmployeeID\", \"Dept\": \"Department\"})

# Reorder columns
columns_in_order = [\"EmployeeID\", \"Name\", \"Department\", \"Salary\", \"JoiningDate\"]
data = transformation_helper.reorder_columns(data, columns_in_order)
```

#### b. Convert Columns to Appropriate Types

Ensure numeric and date columns are properly typed.

```python
# Convert salary to numeric
data = transformation_helper.change_field_to_number(data, [\"Salary\"])

# Convert joining date to datetime
data = transformation_helper.change_field_to_datetime(data, [\"JoiningDate\"])
```

---

### 5. Perform Basic Analytics

Once the data is cleaned, perform some basic analytics.

#### a. Aggregate Data

Calculate the average salary by department.

```python
average_salary = data.groupby(\"Department\")[\"Salary\"].mean()
print(average_salary)
```

#### b. Filter Data

Find employees with salaries above a certain threshold.

```python
high_earners = data[data[\"Salary\"] > 100000]
print(high_earners)
```

#### c. Export Results

Save the filtered data to a new CSV file.

```python
csv_helper.store_dataframe_as_csv(\"data/high_earners.csv\", high_earners)
```

---

## Full Example Notebook

Below is a complete example notebook that combines all the steps above:

```python
# Import necessary utilities
from python_analyst_utils.csv_management.csv_helper import CsvSourceHelper
from python_analyst_utils.pandas_management.pandas_transformation_helper import PandasTransformationHelper

# Initialize helpers
csv_helper = CsvSourceHelper()
transformation_helper = PandasTransformationHelper()

# Step 1: Load the data
data = csv_helper.get_dataframe_from_csv(\"data/large_dataset.csv\")

# Step 2: Inspect the data
transformation_helper.print_general_info_about_dataframe(data)
transformation_helper.print_list_of_columns(data)

# Step 3: Clean the data
data = transformation_helper.trim_values_in_columns(data, [\"Name\", \"Address\"])
data = transformation_helper.remove_special_characters_from_column(data, \"Name\")
data = transformation_helper.replace_nas_with_zeros(data, \"Salary\")
data = transformation_helper.filter_out_nas_and_blanks(data, \"EmployeeID\")
data = transformation_helper.remove_duplicate_rows(data)

# Step 4: Transform the data
data = transformation_helper.rename_columns(data, {\"EmpID\": \"EmployeeID\", \"Dept\": \"Department\"})
data = transformation_helper.reorder_columns(data, [\"EmployeeID\", \"Name\", \"Department\", \"Salary\", \"JoiningDate\"])
data = transformation_helper.change_field_to_number(data, [\"Salary\"])
data = transformation_helper.change_field_to_datetime(data, [\"JoiningDate\"])

# Step 5: Perform analytics
average_salary = data.groupby(\"Department\")[\"Salary\"].mean()
print(\"Average Salary by Department:\")
print(average_salary)

high_earners = data[data[\"Salary\"] > 100000]
print(\"High Earners:\")
print(high_earners)

# Step 6: Export results
csv_helper.store_dataframe_as_csv(\"data/high_earners.csv\", high_earners)
```

---

## Additional Resources

Explore more examples and in-depth tutorials:
- [API Reference for CSV Helper](csv_helper.md)
- [API Reference for Pandas Transformation Helper](pandas_transformation_helper.md)
- [Detailed Cleaning and Transformation Tutorials](examples.md)

