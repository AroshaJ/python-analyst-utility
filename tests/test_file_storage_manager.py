import os
import tempfile
from pathlib import Path
from python_analyst_utils.file_management.file_storage_manager import FileStorageManager


def test_resource_path():
    fsm = FileStorageManager()
    relative_path = "test_folder/test_file.txt"
    absolute_path = fsm.resource_path(relative_path)
    assert os.path.isabs(absolute_path), "resource_path should return an absolute path."


def test_get_current_documents_folder():
    fsm = FileStorageManager()
    documents_folder = fsm.get_current_documents_folder()
    assert documents_folder.is_dir(), "Documents folder path should be a directory."


def test_get_downloads_directory():
    fsm = FileStorageManager()
    downloads_folder = fsm.get_downloads_directory()
    assert downloads_folder.is_dir(), "Downloads folder path should be a directory."


def test_create_folder_if_doesnt_exist():
    fsm = FileStorageManager()
    with tempfile.TemporaryDirectory() as temp_dir:
        new_folder = Path(temp_dir) / "new_folder"
        fsm.create_folder_if_doesnt_exist(new_folder)
        assert new_folder.is_dir(), "Folder should have been created."


def test_clear_all_contents_of_folder():
    fsm = FileStorageManager()
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_file = Path(temp_dir) / "temp_file.txt"
        temp_file.touch()
        assert temp_file.is_file(), "Temporary file should exist."
        fsm.clear_all_contents_of_folder(temp_dir)
        assert not any(Path(temp_dir).iterdir()), "Folder should be empty after clearing."


def test_normalise_filepath():
    fsm = FileStorageManager()
    path = "folder\\subfolder/file.txt"
    normalised_path = fsm.normalise_filepath(path)
    assert "\\" not in normalised_path if os.name != "nt" else "/" not in normalised_path, \
        "Path should be normalised for the current OS."


def test_get_all_files_in_folder():
    fsm = FileStorageManager()
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_file = Path(temp_dir) / "temp_file.txt"
        temp_file.touch()
        files = fsm.get_all_files_in_folder(temp_dir)
        assert len(files) == 1 and "temp_file.txt" in files, "Should list the correct files."


def test_does_folder_exist():
    fsm = FileStorageManager()
    with tempfile.TemporaryDirectory() as temp_dir:
        assert fsm.does_folder_exist(temp_dir), "Folder should exist."


def test_does_file_exist():
    fsm = FileStorageManager()
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_file = Path(temp_dir) / "temp_file.txt"
        temp_file.touch()
        assert fsm.does_file_exist(temp_file), "File should exist."
        missing_file = Path(temp_dir) / "missing_file.txt"
        assert not fsm.does_file_exist(missing_file), "Missing file should not exist."
