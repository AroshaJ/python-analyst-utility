# CSV Source Helper

The **CSV Source Helper** utility simplifies reading and writing CSV files for data analysis workflows. It provides methods for loading CSV data into pandas DataFrames and saving DataFrames back to CSV files, including functionality for storing files in the user's downloads directory.

---

## Key Features

### 📥 Reading CSV Files
- Load CSV files into pandas DataFrames with automatic handling of data types.
- Ensures robust error handling and clear error messages if the file is missing or invalid.

### 📤 Writing CSV Files
- Save pandas DataFrames to CSV files in a specified location.
- Includes functionality to directly save files into the user's downloads folder.

### 🛠️ Seamless Integration
- Integrates with the **File Storage Manager** to dynamically determine the user's downloads directory.

---

## Getting Started

### Installation

Make sure the **Python Analyst Utilities** package is installed:

```bash
pip install python-analyst-utility
```

---

## Quick Start

Here’s how you can get started with the **CSV Source Helper** utility:

#### 1. Load a CSV File into a DataFrame

```python
from python_analyst_utils.csv_management.csv_helper import CsvSourceHelper

# Initialize the helper
csv_helper = CsvSourceHelper()

# Read a CSV file into a pandas DataFrame
df = csv_helper.get_dataframe_from_csv("path/to/data.csv")
print(df)
```

#### 2. Save a DataFrame to a CSV File

```python
from python_analyst_utils.csv_management.csv_helper import CsvSourceHelper
import pandas as pd

# Initialize the helper
csv_helper = CsvSourceHelper()

# Example DataFrame
data = {"Name": ["Alice", "Bob"], "Age": [30, 25]}
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
csv_helper.store_dataframe_as_csv("path/to/output.csv", df)
```

#### 3. Save a DataFrame to the Downloads Folder

```python
from python_analyst_utils.csv_management.csv_helper import CsvSourceHelper
import pandas as pd

# Initialize the helper
csv_helper = CsvSourceHelper()

# Example DataFrame
data = {"Name": ["Alice", "Bob"], "Age": [30, 25]}
df = pd.DataFrame(data)

# Save the DataFrame to the Downloads folder
csv_helper.store_dataframe_as_csv_in_downloads_folder("output.csv", df)
```

---

## How It Works

### CSV File Reading
- The `get_dataframe_from_csv` method:
  - Loads a CSV file into a pandas DataFrame.
  - Ensures the file exists before attempting to read it.
  - Handles errors gracefully, providing clear feedback if the operation fails.

### CSV File Writing
- The `store_dataframe_as_csv` method:
  - Saves a pandas DataFrame to the specified file path.
  - Validates that the input is a DataFrame before proceeding.
  - Handles errors during the save operation and provides informative error messages.

### Downloads Folder Integration
- The `store_dataframe_as_csv_in_downloads_folder` method:
  - Uses the **File Storage Manager** to determine the user's downloads directory.
  - Saves the DataFrame with the specified name in the downloads folder for easy access.

---

## API Reference

Below is the API reference for the **CSV Source Helper** utility.

::: python_analyst_utils.csv_management.csv_manager