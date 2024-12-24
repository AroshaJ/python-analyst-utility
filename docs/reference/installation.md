# Installation

Learn how to install and set up **Python Analyst Utilities** for your project.

---

## Requirements

Before installing, ensure the following dependencies are met:
- **Python**: Version 3.7 or later.
- **pip**: The Python package manager (included with Python installations).
- **Optional**: Jupyter Notebook or JupyterLab for interactive workflows.

---

## Installing the Library

Install the latest version of **Python Analyst Utilities** from PyPI using pip:

```bash
pip install python-analyst-utility
```

You can also find the library on [PyPI here](https://pypi.org/project/python-analyst-utility/).

---

## Verifying the Installation

After installation, verify that the library is available:

```bash
python -c "import python_analyst_utils; print('Python Analyst Utilities installed successfully!')"
```

---

## Optional: Setting Up for Development

If you want to modify or contribute to the library, clone the repository and install the dependencies:

```bash
git clone https://github.com/AroshaJ/python-analyst-utility.git
cd python-analyst-utility
pip install -e .
```

The `-e` flag installs the library in editable mode, allowing you to test changes without reinstalling.

---

## Upgrading to the Latest Version

To upgrade to the latest version, run:

```bash
pip install --upgrade python-analyst-utility
```

---

## Troubleshooting Installation Issues

If you encounter issues during installation:
- **Check Python and pip versions**: Ensure they meet the minimum requirements.
- **Upgrade pip**: Sometimes older versions of pip may not install the package correctly. Run:

```bash
pip install --upgrade pip
```

- **Missing dependencies**: Ensure required dependencies like `pandas`, `xlwings`, and `openpyxl` are installed.

Feel free to raise an issue on our [GitHub repository](https://github.com/AroshaJ/python-analyst-utility/issues) if you need further assistance.
