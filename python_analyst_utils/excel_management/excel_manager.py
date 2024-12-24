from typing import List, Optional, Union, Any
import xlwings as xw
import openpyxl
import pandas as pd
import logging
from pathlib import Path
from dataclasses import dataclass

@dataclass
class ExcelCell:
    """Represents a cell in an Excel worksheet.

    Attributes:
        column (str): The column identifier (e.g., 'A', 'B', etc.)
        row (str): The row number as a string
        sheet_name (str): Name of the worksheet containing the cell
        cell_value (Any): The value contained in the cell
        cell_identifier (str): Optional identifier for reference purposes
    """
    column: str
    row: Union[str, int]
    sheet_name: str
    cell_value: Optional[Any] = None
    cell_identifier: Optional[str] = None

    def __post_init__(self):
        self.row = str(self.row)


class ExcelSourceHelper:
    """A utility class for managing Excel workbooks and performing various operations.

    This class provides methods for:
    - File management (opening, closing, saving workbooks)
    - Data extraction (reading cells, ranges, and sheets)
    - Data manipulation (refreshing workbooks)

    The class supports context manager protocol for safe resource management.
    """

    def __init__(self):
        """Initialize the ExcelSourceHelper with empty application and workbook references."""
        self.application: Optional[xw.App] = None
        self.workbook: Optional[xw.Book] = None
        self._logger = logging.getLogger(__name__)

    def __enter__(self):
        """Context manager entry point."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit point, ensures proper cleanup of resources."""
        self.close_workbook()

    # FILE MANAGEMENT METHODS

    def return_full_path_of_first_excel_file(
        self,
        folder_path: Union[str, Path]
    ) -> Optional[Path]:
        """Return the full path of the first Excel file in the specified folder.

        Args:
            folder_path: Directory path to search for Excel files

        Returns:
            Path object of the first Excel file found, or None if no files exist
        """
        try:
            folder = Path(folder_path)
            excel_files = sorted(folder.glob('*.xls*'))
            return excel_files[0] if excel_files else None
        except Exception as e:
            self._logger.error(f'Failed to get first Excel file: {e}')
            return None

    def return_list_of_excel_files_in_folder(
        self,
        folder_path: Union[str, Path]
    ) -> List[Path]:
        """Return a sorted list of all Excel files in the specified folder.

        Args:
            folder_path: Directory path to search for Excel files

        Returns:
            List of Path objects for all Excel files in the folder
        """
        try:
            folder = Path(folder_path)
            return sorted(folder.glob('*.xls*'))
        except Exception as e:
            self._logger.error(f'Failed to list Excel files: {e}')
            return []

    def open_excel_workbook(
        self,
        file_path: Union[str, Path],
        show_sheet: bool = False
    ) -> Optional[xw.Book]:
        """Open an Excel workbook and store its reference.

        Args:
            file_path: Path to the Excel file
            show_sheet: Whether to make Excel visible during operations

        Returns:
            xlwings Book object if successful, None otherwise
        """
        try:
            if self.application:
                self.close_workbook()
            
            self.application = xw.App(visible=show_sheet)
            self.workbook = self.application.books.open(str(file_path))
            return self.workbook
        except Exception as e:
            self._logger.error(f'Failed to open workbook: {e}')
            if self.application:
                self.application.quit()
            return None

    def save_workbook_in_place(self, workbook: Optional[xw.Book] = None) -> None:
        """Save the workbook in its current location.

        Args:
            workbook: Optional workbook reference. If None, uses the stored workbook
        """
        try:
            wb = workbook or self.workbook
            if wb:
                wb.save()
            else:
                self._logger.warning("No workbook available to save")
        except Exception as e:
            self._logger.error(f'Failed to save workbook: {e}')

    def close_workbook(
        self,
        workbook: Optional[xw.Book] = None,
        application: Optional[xw.App] = None
    ) -> None:
        """Close the workbook and Excel application.

        Args:
            workbook: Optional workbook reference. If None, uses the stored workbook
            application: Optional application reference. If None, uses the stored application
        """
        try:
            wb = workbook or self.workbook
            app = application or self.application

            if wb:
                wb.close()
            if app:
                app.quit()
            
            if not workbook:
                self.workbook = None
            if not application:
                self.application = None
        except Exception as e:
            self._logger.error(f'Failed to close workbook: {e}')

    # DATA EXTRACTION METHODS

    def get_excel_data_as_dataframe(
        self,
        file_path: Union[str, Path],
        sheet_name: Optional[str] = None
    ) -> Optional[pd.DataFrame]:
        """Read Excel data into a pandas DataFrame.

        Args:
            file_path: Path to the Excel file
            sheet_name: Optional sheet name to read from

        Returns:
            DataFrame containing the Excel data, or None if operation fails
        """
        try:
            kwargs = {'dtype': str}
            if sheet_name:
                kwargs['sheet_name'] = sheet_name
            return pd.read_excel(file_path, **kwargs)
        except Exception as e:
            self._logger.error(f'Failed to read Excel data: {e}')
            return None

    def get_excel_data_from_fixed_row(
        self,
        file_path: Union[str, Path],
        sheet_name: str,
        start_row: int
    ) -> Optional[pd.DataFrame]:
        """Read Excel data starting from a specific row.

        Args:
            file_path: Path to the Excel file
            sheet_name: Name of the sheet to read from
            start_row: First row to include in the data (1-based)

        Returns:
            DataFrame containing the Excel data, or None if operation fails
        """
        try:
            return pd.read_excel(
                file_path,
                dtype=str,
                sheet_name=sheet_name,
                skiprows=start_row - 1
            )
        except Exception as e:
            self._logger.error(f'Failed to read Excel data from row {start_row}: {e}')
            return None

    def extract_data_from_fixed_range(
        self,
        file_path: Union[str, Path],
        sheet_name: str,
        column_range: str,
        first_row: int,
        rows_to_extract: int
    ) -> Optional[pd.DataFrame]:
        """Extract data from a specific range in an Excel sheet.

        Args:
            file_path: Path to the Excel file
            sheet_name: Name of the sheet to read from
            column_range: Range of columns (e.g., 'A:Z')
            first_row: First row to include (1-based)
            rows_to_extract: Number of rows to extract

        Returns:
            DataFrame containing the extracted data, or None if operation fails
        """
        try:
            return pd.read_excel(
                file_path,
                sheet_name=sheet_name,
                usecols=column_range,
                skiprows=range(first_row - 1),
                nrows=rows_to_extract,
                engine='openpyxl'
            )
        except Exception as e:
            self._logger.error(f'Failed to extract data from range: {e}')
            return None

    def get_excel_cell_values(
        self,
        file_path: Union[str, Path],
        sheet_name: str,
        cells: List[ExcelCell]
    ) -> Optional[List[ExcelCell]]:
        """Read values for specified cells from an Excel sheet.

        Args:
            file_path: Path to the Excel file
            sheet_name: Name of the sheet to read from
            cells: List of ExcelCell objects to populate with values

        Returns:
            List of ExcelCell objects with populated values, or None if operation fails
        """
        try:
            workbook = openpyxl.load_workbook(file_path, data_only=True)
            sheet = workbook[sheet_name]

            for cell in cells:
                try:
                    cell_location = f"{cell.column}{cell.row}"
                    cell.cell_value = sheet[cell_location].value
                except Exception as cell_e:
                    self._logger.warning(f'Failed to read cell {cell_location}: {cell_e}')

            return cells
        except Exception as e:
            self._logger.error(f'Failed to get cell values: {e}')
            return None

    def refresh_workbook(self, workbook: Optional[xw.Book] = None) -> None:
        """Refresh all data connections in the workbook.

        Args:
            workbook: Optional workbook reference. If None, uses the stored workbook
        """
        try:
            wb = workbook or self.workbook
            if wb:
                wb.app.api.ActiveWorkbook.RefreshAll()
            else:
                self._logger.warning("No workbook available to refresh")
        except Exception as e:
            self._logger.error(f'Failed to refresh workbook: {e}')