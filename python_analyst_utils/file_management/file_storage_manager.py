from pathlib import Path
from typing import List, Optional
import os
import sys
import glob
import logging
from typing import Union

class FileStorageManager:
    """Manages file system operations including path resolution, folder creation, and file management."""
    
    def __init__(self, logger: Optional[logging.Logger] = None):
        """Initialize the FileStorageManager.
        
        Args:
            logger: Optional logger instance for operation logging
        """
        self.logger = logger or logging.getLogger(__name__)

    @staticmethod
    def resource_path(relative_path: str) -> str:
        """Convert relative path to absolute path, handling PyInstaller bundling.
        
        Args:
            relative_path: The relative path to convert
            
        Returns:
            The absolute path
        """
        try:
            base_path = sys._MEIPASS
        except AttributeError:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    @staticmethod
    def get_current_documents_folder() -> Path:
        """Get the path to the current user's Documents folder.
        
        Returns:
            Path to the Documents folder
        """
        return Path.home() / 'Documents'

    @staticmethod
    def get_downloads_directory() -> Path:
        """Get the path to the current user's Downloads folder.
        
        Returns:
            Path to the Downloads folder
        """
        return Path.home() / 'Downloads'

    def create_folder_if_doesnt_exist(self, folder_path: Union[str, Path]) -> None:
        """Create a folder if it doesn't already exist.
        
        Args:
            folder_path: Path where the folder should be created
        """
        Path(folder_path).mkdir(parents=True, exist_ok=True)
        self.logger.info(f'Folder created or verified: {folder_path}')

    def clear_all_contents_of_folder(self, filepath: Union[str, Path]) -> None:
        """Remove all files in the specified folder.
        
        Args:
            filepath: Path to the folder to clear
        """
        try:
            for file in Path(filepath).glob('*'):
                if file.is_file():
                    file.unlink()
            self.logger.info(f'Cleared contents of folder: {filepath}')
        except OSError as e:
            self.logger.error(f'Error clearing contents of {filepath}: {e}')

    @staticmethod
    def normalise_filepath(filepath: Union[str, Path]) -> str:
        """Normalize file path separators for the current operating system.
        
        Args:
            filepath: Path to normalize
            
        Returns:
            Normalized path string
        """
        return os.path.normpath(str(filepath))

    def get_all_files_in_folder(self, folderpath: Union[str, Path]) -> List[str]:
        """Get a list of all files in the specified folder.
        
        Args:
            folderpath: Path to the folder to scan
            
        Returns:
            List of filenames in the folder
        """
        try:
            folder = Path(folderpath)
            return [f.name for f in folder.iterdir() if f.is_file()]
        except OSError as e:
            self.logger.error(f'Error listing files in {folderpath}: {e}')
            return []

    @staticmethod
    def to_camel_case(full_string: str) -> str:
        """Convert a space-separated string to camelCase.
        
        Args:
            full_string: String to convert
            
        Returns:
            camelCase version of the string
        """
        words = full_string.split()
        return words[0].lower() + ''.join(word.capitalize() for word in words[1:])

    @staticmethod
    def does_folder_exist(folder_path: Union[str, Path]) -> bool:
        """Check if a folder exists at the specified path.
        
        Args:
            folder_path: Path to check
            
        Returns:
            True if folder exists, False otherwise
        """
        return Path(folder_path).is_dir()

    def create_folder_in_path(self, folder_path: Union[str, Path]) -> None:
        """Create a folder at the specified path.
        
        Args:
            folder_path: Path where the folder should be created
        """
        Path(folder_path).mkdir(parents=True, exist_ok=True)
        self.logger.info(f'Created folder: {folder_path}')

    def does_file_exist(self, filepath: Union[str, Path], create_parent_if_missing: bool = False) -> bool:
        """Check if a file exists at the specified path.
        
        Args:
            filepath: Path to check
            create_parent_if_missing: If True, create the parent directory if it doesn't exist
            
        Returns:
            True if file exists, False otherwise
        """
        try:
            path = Path(filepath)
            if create_parent_if_missing:
                path.parent.mkdir(parents=True, exist_ok=True)
            return path.is_file()
        except OSError as e:
            self.logger.error(f'Error checking file existence at {filepath}: {e}')
            return False
        
        
    def print_folder_structure(
        self, 
        root_dir: str, 
        indent: str = "", 
        ignore_dirs: Optional[List[str]] = None
    ) -> None:
        """
        Prints the folder structure of a given directory.

        Args:
            root_dir (str): The root directory to scan.
            indent (str): The indentation for nested directories (used internally).
            ignore_dirs (Optional[List[str]]): List of directory names to ignore.
        """
        if ignore_dirs is None:
            ignore_dirs = []

        try:
            # Print the current folder
            print(indent + os.path.basename(root_dir) + "/")
            # List all files and subdirectories
            for item in sorted(os.listdir(root_dir)):
                item_path = os.path.join(root_dir, item)
                if os.path.isdir(item_path):
                    # Skip ignored directories
                    if os.path.basename(item_path) in ignore_dirs:
                        continue
                    # Recursively print subdirectories
                    self.print_folder_structure(item_path, indent + "    ", ignore_dirs)
                else:
                    # Print files
                    print(indent + "    " + item)
        except PermissionError:
            print(indent + "[Access Denied]")
            


if __name__ == "__main__":
    # Create an instance of FileStorageManager
    fsm = FileStorageManager()

    # Define the project root directory
    project_root = r"C:\Users\Arosh\Documents\GitHub\python-analyst-utility"

    # Print the folder structure while ignoring the 'venv' folder
    print("Project Folder Structure:")
    fsm.print_folder_structure(root_dir=project_root, ignore_dirs=["venv", ".pytest_cache", ".git"])
        