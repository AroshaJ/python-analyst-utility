import os
import pandas as pd
import pytest
from python_analyst_utils.csv_management.csv_manager import CsvSourceHelper



@pytest.fixture
def sample_dataframe():
    """Fixture to provide a sample pandas DataFrame."""
    return pd.DataFrame({"col1": [1, 2, 3], "col2": ["A", "B", "C"]})


@pytest.fixture
def temp_csv_file(tmp_path):
    """Fixture to provide a temporary CSV file path."""
    temp_file = tmp_path / "temp_file.csv"
    return temp_file


def test_get_dataframe_from_csv_valid_file(sample_dataframe, temp_csv_file):
    """Test reading a valid CSV file into a DataFrame."""
    # Write sample data to temp CSV file
    sample_dataframe.to_csv(temp_csv_file, index=False)

    # Read back the data using CsvSourceHelper
    csv_helper = CsvSourceHelper()
    df = csv_helper.get_dataframe_from_csv(str(temp_csv_file))

    # Cast the column data types to match the original DataFrame
    df = df.astype(sample_dataframe.dtypes.to_dict())

    # Verify the DataFrame matches the sample
    pd.testing.assert_frame_equal(df, sample_dataframe)


def test_get_dataframe_from_csv_missing_file():
    """Test attempting to read a missing CSV file."""
    csv_helper = CsvSourceHelper()
    invalid_path = "non_existent_file.csv"
    with pytest.raises(FileNotFoundError, match=f"CSV file not found at: {invalid_path}"):
        csv_helper.get_dataframe_from_csv(invalid_path)


def test_store_dataframe_as_csv_valid_file(sample_dataframe, temp_csv_file):
    """Test storing a valid DataFrame to a CSV file."""
    csv_helper = CsvSourceHelper()
    csv_helper.store_dataframe_as_csv(str(temp_csv_file), sample_dataframe)

    # Verify the file contents match the DataFrame
    stored_df = pd.read_csv(temp_csv_file)
    pd.testing.assert_frame_equal(stored_df, sample_dataframe)


def test_store_dataframe_as_csv_invalid_input(temp_csv_file):
    """Test storing a non-DataFrame input."""
    csv_helper = CsvSourceHelper()
    invalid_input = {"col1": [1, 2, 3], "col2": ["A", "B", "C"]}  # Not a DataFrame

    with pytest.raises(TypeError, match="Input must be a pandas DataFrame"):
        csv_helper.store_dataframe_as_csv(str(temp_csv_file), invalid_input)


def test_store_dataframe_as_csv_in_downloads_folder(mocker, sample_dataframe, tmp_path):
    """Test storing a DataFrame to the downloads folder."""
    # Use a temporary directory for the mock downloads folder
    mock_downloads_directory = tmp_path / "mock_downloads"
    mock_downloads_directory.mkdir()  # Create the directory

    # Mock only the get_downloads_directory method
    mocker.patch(
        "python_analyst_utils.file_management.file_storage_manager.FileStorageManager.get_downloads_directory",
        return_value=str(mock_downloads_directory),
    )

    csv_helper = CsvSourceHelper()
    document_name = "test_document.csv"
    expected_filepath = mock_downloads_directory / document_name

    # Store the DataFrame
    csv_helper.store_dataframe_as_csv_in_downloads_folder(document_name, sample_dataframe)

    # Verify the file was written to the mock downloads directory
    stored_df = pd.read_csv(expected_filepath)
    pd.testing.assert_frame_equal(stored_df, sample_dataframe)
