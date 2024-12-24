import pytest
import pandas as pd
import numpy as np
from python_analyst_utils.pandas_management.pandas_transformation_helper import PandasTransformationHelper


@pytest.fixture
def transformation_helper():
    # Creates a fresh instance of PandasTransformationHelper for each test
    return PandasTransformationHelper()

@pytest.fixture
def sample_df():
    # Creates a sample DataFrame with different data types and edge cases:
    # - Numeric values with NaN
    # - String values with empty string
    # - DateTime range
    # - Float values with NaN
    return pd.DataFrame({
        'A': [1, 2, 3, np.nan],
        'B': ['foo', 'bar', 'baz', ''],
        'C': pd.date_range('2021-01-01', periods=4),
        'D': [1.1, 2.2, np.nan, 4.4]
    })

class TestPandasTransformationHelper:
    # Diagnostic Methods Tests
    def test_get_list_of_columns(self, transformation_helper, sample_df):
        # Verifies that all column names are correctly retrieved from the DataFrame
        columns = transformation_helper.get_list_of_columns(sample_df)
        assert columns == ['A', 'B', 'C', 'D']

    def test_print_dataframe_dimensions(self, transformation_helper, sample_df, capsys):
        # Tests if DataFrame dimensions are correctly printed to stdout
        transformation_helper.print_dataframe_dimensions(sample_df)
        captured = capsys.readouterr()
        assert "The DataFrame has 4 rows and 4 columns" in captured.out

    # Column Methods Tests
    def test_keep_selected_columns(self, transformation_helper, sample_df):
        # Ensures only specified columns are kept while others are dropped
        result = transformation_helper.keep_selected_columns(sample_df, ['A', 'B'])
        assert list(result.columns) == ['A', 'B']
        assert len(result.columns) == 2

    def test_remove_specific_columns(self, transformation_helper, sample_df):
        # Verifies specified columns are removed while others remain
        result = transformation_helper.remove_specific_columns(sample_df, ['A'])
        assert 'A' not in result.columns
        assert len(result.columns) == 3

    def test_rename_columns(self, transformation_helper, sample_df):
        # Tests column renaming functionality using a mapping dictionary
        result = transformation_helper.rename_columns(sample_df, {'A': 'Alpha'})
        assert 'Alpha' in result.columns
        assert 'A' not in result.columns

    # Type Methods Tests
    def test_change_field_to_datetime(self, transformation_helper):
        # Validates conversion of string dates to datetime objects
        df = pd.DataFrame({'date_col': ['2021-01-01', '2021-01-02']})
        result = transformation_helper.change_field_to_datetime(df, ['date_col'])
        assert pd.api.types.is_datetime64_any_dtype(result['date_col'])

    def test_change_field_to_number(self, transformation_helper):
        # Checks conversion of string numbers to numeric dtype
        df = pd.DataFrame({'num_col': ['1.1', '2.2']})
        result = transformation_helper.change_field_to_number(df, ['num_col'])
        assert pd.api.types.is_numeric_dtype(result['num_col'])

    # Content Methods Tests
    def test_clear_nans(self, transformation_helper, sample_df):
        # Ensures NaN values are removed from the DataFrame appropriately based on dtype
        # Store the indices where NaN values exist before filling
        a_nan_idx = sample_df[sample_df['A'].isna()].index
        d_nan_idx = sample_df[sample_df['D'].isna()].index
        
        result = transformation_helper.clear_nans(sample_df)
        
        # Check numeric columns are filled with 0
        assert result['A'].isna().sum() == 0
        assert result['D'].isna().sum() == 0
        
        # Verify the values were filled correctly at the original NaN positions
        assert result.loc[a_nan_idx, 'A'].iloc[0] == 0
        assert result.loc[d_nan_idx, 'D'].iloc[0] == 0

    def test_remove_duplicate_rows(self, transformation_helper):
        # Verifies duplicate rows are removed from the DataFrame
        df = pd.DataFrame({'A': [1, 1, 2], 'B': [1, 1, 2]})
        result = transformation_helper.remove_duplicate_rows(df)
        assert len(result) == 2

    # Cleaning Methods Tests
    def test_trim_values_in_columns(self, transformation_helper):
        # Tests removal of leading/trailing whitespace in string columns
        df = pd.DataFrame({'A': [' test ', 'hello ']})
        result = transformation_helper.trim_values_in_columns(df, ['A'])
        assert result['A'].iloc[0] == 'test'
        assert result['A'].iloc[1] == 'hello'

    # Merge Methods Tests
    def test_append_dataframes(self, transformation_helper):
        # Validates vertical concatenation of two DataFrames
        df1 = pd.DataFrame({'A': [1, 2]})
        df2 = pd.DataFrame({'A': [3, 4]})
        result = transformation_helper.append_dataframes(df1, df2)
        assert len(result) == 4

    def test_left_merge_dataframes(self, transformation_helper):
        # Tests left join operation between two DataFrames on a single key
        df1 = pd.DataFrame({'key': [1, 2], 'value': ['a', 'b']})
        df2 = pd.DataFrame({'key': [1, 3], 'other': ['x', 'y']})
        result = transformation_helper.left_merge_dataframes(df1, df2, 'key')
        assert len(result) == 2
        assert 'other' in result.columns

    def test_left_merge_dataframes_on_multiple_fields(self, transformation_helper):
        # Verifies left join operation on multiple keys
        df1 = pd.DataFrame({'key1': [1, 2], 'key2': ['a', 'b'], 'value': [1, 2]})
        df2 = pd.DataFrame({'key1': [1, 3], 'key2': ['a', 'c'], 'other': [3, 4]})
        result = transformation_helper.left_merge_dataframes_on_multiple_fields(
            df1, df2, 
            ['key1', 'key2'], 
            ['key1', 'key2']
        )
        assert len(result) == 2
        assert 'other' in result.columns

    def test_merge_dataframes_with_field_mapping(self, transformation_helper):
        # Tests merge operation using different column names through field mapping
        df1 = pd.DataFrame({'key_a': [1, 2], 'value': ['a', 'b']})
        df2 = pd.DataFrame({'key_b': [1, 3], 'other': ['x', 'y']})
        field_mapping = {'key_a': 'key_b'}
        result = transformation_helper.merge_dataframes_with_field_mapping(
            df1, df2, 
            field_mapping
        )
        assert len(result) == 2
        assert 'other' in result.columns