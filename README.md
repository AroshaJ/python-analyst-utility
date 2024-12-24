# Python Analyst Utilities

[![PyPI version](https://badge.fury.io/py/python-analyst-utility.svg)](https://badge.fury.io/py/python-analyst-utility)  
**Python Analyst Utilities** is a powerful and user-friendly Python library designed to streamline data workflows for analysts, data scientists, and developers. It offers utilities for working with Excel, CSV files, file management, pandas DataFrames, and more. 

---

## Key Features

1. **Excel Helper**: Simplifies reading, writing, and managing Excel files.
2. **CSV Helper**: Provides robust tools for handling CSV data with pandas integration.
3. **File Storage Manager**: Dynamic file and folder management with system directory detection.
4. **Date Format Detector**: Automatically detects date formats in strings or lists.
5. **Pandas Transformation Helper**: A comprehensive utility for cleaning, transforming, and merging pandas DataFrames.

---

## Documentation

Comprehensive documentation, including detailed examples and API references, is available at:

[Python Analyst Utilities Documentation](https://aroshaj.github.io/python-analyst-utility)

---

## Installation

Install the package directly from PyPI:

```bash
pip install python-analyst-utility
```

---

## Quick Start

Here are a few examples to help you get started:

### Example 1: Loading and Cleaning a CSV File

```python
from python_analyst_utils.csv_management.csv_helper import CsvSourceHelper
from python_analyst_utils.pandas_management.pandas_transformation_helper import PandasTransformationHelper
import pandas as pd

# Initialize helpers
csv_helper = CsvSourceHelper()
transformation_helper = PandasTransformationHelper()

# Load a CSV file into a pandas DataFrame
file_path = "data/sample.csv"
data = csv_helper.get_dataframe_from_csv(file_path)

# Clean the data: trim whitespace and handle NaNs
data = transformation_helper.trim_values_in_columns(data, ["Name", "Address"])
data = transformation_helper.replace_nas_with_zeros(data, "Salary")

# Print cleaned data
print(data.head())
```

### Example 2: Managing Files and Directories

```python
from python_analyst_utils.file_management.file_storage_manager import FileStorageManager

# Initialize the file manager
manager = FileStorageManager()

# Create a folder and check if it exists
folder_path = "data/new_folder"
manager.create_folder_if_doesnt_exist(folder_path)
folder_exists = manager.does_folder_exist(folder_path)
print(f"Folder exists: {folder_exists}")
```

---

## Contributing

We welcome contributions! Whether it’s fixing a bug, adding a new feature, or improving documentation, your input is valuable.  

- **Repository**: [GitHub](https://github.com/AroshaJ/python-analyst-utility)  
- **Issues**: [Report or Suggest](https://github.com/AroshaJ/python-analyst-utility/issues)

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

Special thanks to all contributors and users who have helped shape **Python Analyst Utilities**. Your support and feedback are instrumental to its success.

