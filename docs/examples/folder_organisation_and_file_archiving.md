# Folder Organisation and File Archiving

**Scenario**: A user has a directory filled with unsorted files and wants to organise them by type and archive old files.

---

## Step-by-Step Example

### 1. List Files in a Directory

Use the **File Storage Manager** to get a list of all files in a directory.

```python
from python_analyst_utils.file_management.file_storage_manager import FileStorageManager
```

# Initialize the file manager

```python
file_manager = FileStorageManager()
```

# Define the directory

```python
source_directory = "data/unsorted_files"
```

# Get a list of files

```python
file_list = file_manager.get_all_files_in_folder(source_directory)
print(f"Files in the directory: {file_list}")
```

---

### 2. Organise Files by Type

Move files into subfolders based on their file types (e.g., `csv/`, `excel/`).

```python
import os
from shutil import move
```

# Organise files

```python
for file in file_list:
    if file.endswith(".csv"):
        destination = os.path.join(source_directory, "csv", file)
    elif file.endswith(".xlsx"):
        destination = os.path.join(source_directory, "excel", file)
    else:
        destination = os.path.join(source_directory, "other", file)
    
    # Create folder if it doesn't exist
    file_manager.create_folder_if_doesnt_exist(os.path.dirname(destination))
    move(os.path.join(source_directory, file), destination)

print("Files have been organised.")
```

---

### 3. Archive Old Files

Move files older than a specified date to an archive directory.

```python
import shutil
from datetime import datetime

archive_directory = "data/archive"

for file in os.listdir(source_directory):
    full_path = os.path.join(source_directory, file)
    if os.path.isfile(full_path):
        modified_time = os.path.getmtime(full_path)
        file_date = datetime.fromtimestamp(modified_time)
        if file_date < datetime(2024, 1, 1):  # Example: Archive files before 2024
            archive_path = os.path.join(archive_directory, file)
            file_manager.create_folder_if_doesnt_exist(archive_directory)
            shutil.move(full_path, archive_path)

print("Old files have been archived.")
```

---

## Summary

This example demonstrated:
1. Listing all files in a directory.
2. Organising files into subfolders based on type.
3. Archiving old files to maintain a clean directory structure.
