import os
import pandas as pd
from python_analyst_utils.file_management.file_storage_manager import FileStorageManager


class CsvSourceHelper:
    """Helper class for CSV file operations including reading and writing DataFrames."""

    def get_dataframe_from_csv(
        self,
        filepath: str
    ) -> pd.DataFrame | None:
        """
        Read a CSV file and return it as a pandas DataFrame.
        
        Args:
            filepath: Path to the CSV file
            
        Returns:
            DataFrame if successful, None if failed
        """
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"CSV file not found at: {filepath}")
            
        try:
            return pd.read_csv(filepath, dtype=str)
        except Exception as e:
            raise RuntimeError(f"Failed to read CSV file: {str(e)}")

    def store_dataframe_as_csv(
        self,
        filepath: str,
        dataframe_to_store: pd.DataFrame
    ) -> None:
        """
        Store a DataFrame as a CSV file.
        
        Args:
            filepath: Destination path for the CSV file
            dataframe_to_store: DataFrame to save
        """
        if not isinstance(dataframe_to_store, pd.DataFrame):
            raise TypeError("Input must be a pandas DataFrame")
            
        try:
            dataframe_to_store.to_csv(filepath, index=False)
        except Exception as e:
            raise RuntimeError(f"Failed to store CSV file: {str(e)}")

    def store_dataframe_as_csv_in_downloads_folder(
        self,
        document_name: str,
        dataframe_to_store: pd.DataFrame
    ) -> None:
        """
        Store a DataFrame as a CSV file in the downloads directory.
        
        Args:
            document_name: Name of the output CSV file
            dataframe_to_store: DataFrame to save
        """
        home_drive_info = FileStorageManager()
        downloads_directory = home_drive_info.get_downloads_directory()
        filepath = os.path.join(downloads_directory, document_name)

        self.store_dataframe_as_csv(filepath, dataframe_to_store)