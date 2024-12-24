# Date Format Detector

The **Date Format Detector** utility simplifies the process of identifying date format patterns from a string or a list of strings. It is especially useful for validating and standardising date inputs in data processing workflows.

---

## Key Features

### 🕒 Detect Common Date Formats
- Automatically detects a wide range of common date formats, including:
  - `YYYY-MM-DD`, `DD/MM/YYYY`, `MM/DD/YYYY`
  - `DD MMM YYYY`, `MMM DD YYYY`, `YYYY MMM DD`
  - Formats with time components like `YYYY-MM-DD HH:MM:SS`

### 🔍 Handles Single and Multiple Inputs
- Analyse a single date string to determine its format.
- Evaluate a list of date samples and find the most common matching pattern.

### 🛠️ Flexible and Easy-to-Use
- Works seamlessly with standard Python `datetime` format strings.
- Can handle mixed input cases with robust error handling.

---

## Getting Started

### Installation

Make sure the **Python Analyst Utilities** package is installed:

```bash
pip install python-analyst-utility
```

---

## Quick Start

Here’s how you can get started with the **Date Format Detector** utility:

#### 1. Detect the Format of a Single Date String

```python
from python_analyst_utils.date_format.date_detector import DateFormatDetector

# Detect the format of a single date string
date_format = DateFormatDetector.detect_format("2023-12-25")
print(f"Detected format: {date_format}")  # Output: "%Y-%m-%d"
```

#### 2. Detect the Most Common Format in a List of Dates

```python
from python_analyst_utils.date_format.date_detector import DateFormatDetector

# Detect the common format from a list of date strings
sample_dates = ["25/12/2023", "26/12/2023", "27/12/2023"]
common_format = DateFormatDetector.detect_format(sample_dates)
print(f"Most common format: {common_format}")  # Output: "%d/%m/%Y"
```

---

## How It Works

### Supported Formats
The utility checks against a predefined set of commonly used date formats, including:
- `%Y-%m-%d`, `%d/%m/%Y`, `%m/%d/%Y`
- `%d-%m-%Y`, `%d %b %Y`, `%d %B %Y`
- Formats with time components, such as `%Y-%m-%d %H:%M:%S`

### Handling Single and Multiple Inputs
1. **Single Input**: A single date string is checked against each format sequentially until a match is found.
2. **Multiple Inputs**: A list of date strings is validated against all formats. The format that matches all strings is returned, prioritising specificity.

---

## API Reference

Below is the API reference for the **Date Format Detector** utility.

::: python_analyst_utils.date_management.date_manager