import pytest
import pandas as pd
import openpyxl
from pathlib import Path
from python_analyst_utils.excel_management.excel_manager import ExcelCell, ExcelSourceHelper



@pytest.fixture
def temp_excel_file(tmp_path):
    """Fixture to create a temporary Excel file for testing."""
    temp_file = tmp_path / "test_file.xlsx"
    df = pd.DataFrame({"col1": [1, 2, 3], "col2": ["A", "B", "C"]})
    df.to_excel(temp_file, index=False, engine='openpyxl')
    return temp_file


@pytest.fixture
def temp_folder_with_excel_files(tmp_path):
    """Fixture to create a temporary folder with multiple Excel files."""
    folder = tmp_path / "excel_files"
    folder.mkdir()
    for i in range(3):
        file_path = folder / f"file_{i + 1}.xlsx"
        df = pd.DataFrame({"col1": [1, 2, 3], "col2": ["A", "B", "C"]})
        df.to_excel(file_path, index=False, engine='openpyxl')
    return folder


@pytest.fixture
def sample_cells():
    """Fixture to provide sample ExcelCell objects."""
    return [
        ExcelCell(column="A", row=1, sheet_name="Sheet1"),
        ExcelCell(column="B", row=2, sheet_name="Sheet1"),
    ]


# TESTS FOR FILE MANAGEMENT METHODS

def test_return_full_path_of_first_excel_file(temp_folder_with_excel_files):
    """Test getting the first Excel file in a folder."""
    helper = ExcelSourceHelper()
    first_file = helper.return_full_path_of_first_excel_file(temp_folder_with_excel_files)
    assert first_file is not None
    assert first_file.name == "file_1.xlsx"


def test_return_list_of_excel_files_in_folder(temp_folder_with_excel_files):
    """Test getting a list of all Excel files in a folder."""
    helper = ExcelSourceHelper()
    files = helper.return_list_of_excel_files_in_folder(temp_folder_with_excel_files)
    assert len(files) == 3
    assert all(file.suffix == ".xlsx" for file in files)


def test_open_excel_workbook(temp_excel_file):
    """Test opening an Excel workbook."""
    helper = ExcelSourceHelper()
    workbook = helper.open_excel_workbook(temp_excel_file, show_sheet=False)
    assert workbook is not None
    assert workbook.name == temp_excel_file.name
    helper.close_workbook()


def test_save_workbook_in_place(temp_excel_file):
    """Test saving an Excel workbook in place."""
    helper = ExcelSourceHelper()
    workbook = helper.open_excel_workbook(temp_excel_file, show_sheet=False)
    helper.save_workbook_in_place()
    helper.close_workbook()
    assert temp_excel_file.exists()  # Verify file is still present


# TESTS FOR DATA EXTRACTION METHODS

def test_get_excel_data_as_dataframe(temp_excel_file):
    """Test reading Excel data as a DataFrame."""
    helper = ExcelSourceHelper()
    df = helper.get_excel_data_as_dataframe(temp_excel_file)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 2)  # Verify rows and columns


def test_get_excel_data_from_fixed_row(temp_excel_file):
    """Test reading Excel data from a specific row."""
    helper = ExcelSourceHelper()
    df = helper.get_excel_data_from_fixed_row(temp_excel_file, sheet_name="Sheet1", start_row=2)
    assert isinstance(df, pd.DataFrame)
    assert df.shape[0] == 2  # Only 2 rows should remain


def test_extract_data_from_fixed_range(temp_excel_file):
    """Test extracting data from a specific range."""
    helper = ExcelSourceHelper()
    df = helper.extract_data_from_fixed_range(
        file_path=temp_excel_file,
        sheet_name="Sheet1",
        column_range="A:B",
        first_row=1,
        rows_to_extract=2,
    )
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 2)  # Verify extracted rows and columns


def test_get_excel_cell_values(temp_excel_file, sample_cells):
    """Test reading specific cell values."""
    helper = ExcelSourceHelper()

    # Adjust sample_cells to reflect the actual data in temp_excel_file
    updated_cells = [
        ExcelCell(column="A", row=1, sheet_name="Sheet1"),  # Header of column A
        ExcelCell(column="B", row=1, sheet_name="Sheet1"),  # Header of column B
    ]
    cells_with_values = helper.get_excel_cell_values(temp_excel_file, sheet_name="Sheet1", cells=updated_cells)

    # Verify the values match the header data
    assert len(cells_with_values) == 2
    assert cells_with_values[0].cell_value == "col1"  # Header of column A
    assert cells_with_values[1].cell_value == "col2"  # Header of column B


# TESTS FOR WORKBOOK REFRESHING

def test_refresh_workbook(mocker, temp_excel_file):
    """Test refreshing an Excel workbook."""
    helper = ExcelSourceHelper()
    mock_app = mocker.patch("xlwings.Book.app", autospec=True)
    workbook = helper.open_excel_workbook(temp_excel_file, show_sheet=False)
    helper.refresh_workbook(workbook)
    mock_app.api.ActiveWorkbook.RefreshAll.assert_called_once()
    helper.close_workbook()
