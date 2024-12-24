# python-analyst-utility

A Python package providing streamlined tools for analysts, including Pandas wrappers, Excel and CSV helpers, and file management utilities. Simplify common tasks and boost productivity with this all-in-one utility package.

## Features

- 📊 Enhanced Pandas functionality with intuitive wrappers
- 📑 Simplified Excel and CSV file handling
- 🗂️ File management utilities for common analyst tasks
- ⚡ Performance-optimized data operations
- 🔧 Easy-to-use API for common data analysis tasks

## Installation

Install using pip:

```bash
pip install python-analyst-utility
```

## Quick Start

```python
from analyst_utility import excel, pandas_helper

# Example: Reading an Excel file with enhanced features
df = excel.read_excel("data.xlsx", sheet_name="Sheet1")

# Example: Using pandas helper functions
cleaned_df = pandas_helper.clean_column_names(df)
```

## Documentation

### Excel Module

```python
# Read Excel files with additional options
excel.read_excel(filename, sheet_name="Sheet1", headers=True)
# Write to Excel with formatting
excel.write_excel(df, filename, sheet_name="Output")
```

### Pandas Helper Module

```python
# Clean column names
pandas_helper.clean_column_names(df)
# Quick data quality check
pandas_helper.check_data_quality(df)
```

## Building The Package

Build the package using:

```bash
python setup.py sdist bdist_wheel
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For support, please open an issue in the GitHub repository.

## Changelog

### Version 1.0.0
- Initial release
- Basic Excel and CSV functionality
- Pandas helper functions
- File management utilities

---