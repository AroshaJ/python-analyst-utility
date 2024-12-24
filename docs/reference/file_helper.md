# File Storage Manager

The **File Storage Manager** utility simplifies common file system operations, including managing file paths, creating folders, clearing directories, and more. It is an essential tool for handling file-related operations in Python projects with robust error handling and flexibility.

---

## Key Features

### 📂 Folder and File Management
- Create folders if they don't already exist.
- Check if files or folders exist at a given path.
- Clear all contents of a folder with a single command.

### 📁 Directory Exploration
- Retrieve all files in a specified directory.
- Print the folder structure recursively, with options to ignore certain directories.

### 🛠️ Path Handling and Normalisation
- Convert relative paths to absolute paths, compatible with `PyInstaller` bundling.
- Normalise file paths for cross-platform compatibility.

### 🔤 String Utilities
- Convert strings to `camelCase` for consistent naming conventions.

---

## Getting Started

### Installation

Make sure the **Python Analyst Utilities** package is installed:

```bash
pip install python-analyst-utility
```

---

## Quick Start

Here’s how you can get started with the **File Storage Manager** utility:

#### 1. Create a Folder if it Doesn't Exist

```python
from python_analyst_utils.file_management.file_storage_manager import FileStorageManager

# Initialize the manager
storage_manager = FileStorageManager()

# Create a folder
storage_manager.create_folder_if_doesnt_exist("path/to/new/folder")
```

#### 2. Check if a File Exists

```python
from python_analyst_utils.file_management.file_storage_manager import FileStorageManager

# Initialize the manager
storage_manager = FileStorageManager()

# Check if a file exists
file_exists = storage_manager.does_file_exist("path/to/file.txt")
print(f"File exists: {file_exists}")
```

#### 3. Clear All Files in a Folder

```python
from python_analyst_utils.file_management.file_storage_manager import FileStorageManager

# Initialize the manager
storage_manager = FileStorageManager()

# Clear the contents of a folder
storage_manager.clear_all_contents_of_folder("path/to/folder")
```

#### 4. Print Folder Structure

```python
from python_analyst_utils.file_management.file_storage_manager import FileStorageManager

# Initialize the manager
storage_manager = FileStorageManager()

# Print the folder structure, ignoring certain directories
storage_manager.print_folder_structure("path/to/root", ignore_dirs=[".git", "__pycache__"])
```

#### 5. Get the Path to Downloads or Documents Folder

```python
from python_analyst_utils.file_management.file_storage_manager import FileStorageManager

# Initialize the manager
storage_manager = FileStorageManager()

# Get the downloads directory
downloads_dir = storage_manager.get_downloads_directory()
print(f"Downloads folder: {downloads_dir}")
```

---

## How It Works

### Path and Folder Management
- **Path Conversion**: The `resource_path` method handles conversion of relative paths to absolute paths, making it suitable for use in standalone executables created with `PyInstaller`.
- **Folder Creation**: Ensures a folder exists before performing operations, automatically creating it if necessary.

### File Operations
- **Clear Contents**: Removes all files from a specified directory while maintaining the folder structure.
- **File Existence**: Provides a safe way to check if a file exists, with optional creation of parent directories.

### Directory Exploration
- **List Files**: Retrieves all files in a folder, returning them as a list of file names.
- **Print Structure**: Recursively prints the folder and file structure for easy visualisation.

### Utility Functions
- **Path Normalisation**: Converts file paths to use OS-specific separators for compatibility.
- **Camel Case Conversion**: Transforms strings into `camelCase` for consistent naming conventions.

---

## API Reference

Below is the API reference for the **File Storage Manager** utility.

::: python_analyst_utils.file_management.file_storage_manager