import pandas as pd
from typing import Optional, List, Dict, Union, Any

from .helpers.pandas_diagnostic_helper import PandasDiagnosticHelper
from .helpers.pandas_column_helper import PandasColumnHelper
from .helpers.pandas_type_helper import PandasTypeHelper
from .helpers.pandas_content_helper import PandasContentHelper
from .helpers.pandas_cleaning_helper import PandasCleaningHelper
from .helpers.pandas_merge_helper import PandasMergeHelper

class PandasTransformationHelper:
    """
    Main class that provides comprehensive pandas DataFrame transformation capabilities
    by delegating to specialized helper classes.
    """

    def __init__(self):
        """Initialize all helper classes."""
        self.diagnostic_helper = PandasDiagnosticHelper()
        self.column_helper = PandasColumnHelper()
        self.type_helper = PandasTypeHelper()
        self.content_helper = PandasContentHelper()
        self.cleaning_helper = PandasCleaningHelper()
        self.merge_helper = PandasMergeHelper()

    # -----------------------------
    # DIAGNOSTIC METHODS
    # -----------------------------
    def get_list_of_columns(self, dataframe: pd.DataFrame) -> Optional[List[str]]:
        """
        Get a list of all column names in the DataFrame.

        Args:
            dataframe (pd.DataFrame): The input DataFrame.

        Returns:
            Optional[List[str]]: List of column names if successful, None if an error occurs.
        """
        return self.diagnostic_helper.get_list_of_columns(dataframe)

    def print_dataframe_dimensions(self, dataframe: pd.DataFrame) -> None:
        """
        Print the dimensions (rows x columns) of the DataFrame.

        Args:
            dataframe (pd.DataFrame): The input DataFrame.
        """
        self.diagnostic_helper.print_dataframe_dimensions(dataframe)

    def print_general_info_about_dataframe(self, dataframe: pd.DataFrame) -> None:
        """
        Print general information about the DataFrame including data types and non-null counts.

        Args:
            dataframe (pd.DataFrame): The input DataFrame.
        """
        self.diagnostic_helper.print_general_info_about_dataframe(dataframe)

    def print_list_of_columns(self, dataframe: pd.DataFrame) -> None:
        """
        Print all column names in the DataFrame.

        Args:
            dataframe (pd.DataFrame): The input DataFrame.
        """
        self.diagnostic_helper.print_list_of_columns(dataframe)

    # -----------------------------
    # COLUMN METHODS
    # -----------------------------
    def keep_selected_columns(self, dataframe: pd.DataFrame, columns_to_keep_list: List[str]) -> Optional[pd.DataFrame]:
        """
        Create a new DataFrame with only the specified columns.

        Args:
            dataframe (pd.DataFrame): The input DataFrame.
            columns_to_keep_list (List[str]): List of column names to keep.

        Returns:
            Optional[pd.DataFrame]: DataFrame with only specified columns if successful, None if an error occurs.
        """
        return self.column_helper.keep_selected_columns(dataframe, columns_to_keep_list)

    def remove_specific_columns(self, dataframe: pd.DataFrame, columns_to_remove: List[str]) -> Optional[pd.DataFrame]:
        """
        Remove specified columns from the DataFrame.

        Args:
            dataframe (pd.DataFrame): The input DataFrame.
            columns_to_remove (List[str]): List of column names to remove.

        Returns:
            Optional[pd.DataFrame]: DataFrame with columns removed if successful, None if an error occurs.
        """
        return self.column_helper.remove_specific_columns(dataframe, columns_to_remove)

    def rename_columns(self, dataframe: pd.DataFrame, columns_to_rename_dict: Dict[str, str]) -> Optional[pd.DataFrame]:
        """
        Rename columns in the DataFrame using a mapping dictionary.

        Args:
            dataframe (pd.DataFrame): The input DataFrame.
            columns_to_rename_dict (Dict[str, str]): Dictionary mapping old column names to new ones.

        Returns:
            Optional[pd.DataFrame]: DataFrame with renamed columns if successful, None if an error occurs.
        """
        return self.column_helper.rename_columns(dataframe, columns_to_rename_dict)

    def rename_all_columns(self, dataframe: pd.DataFrame, list_of_columns: List[str]) -> Optional[pd.DataFrame]:
        """
        Rename all columns in the DataFrame using a list of new names.

        Args:
            dataframe (pd.DataFrame): The input DataFrame.
            list_of_columns (List[str]): List of new column names.

        Returns:
            Optional[pd.DataFrame]: DataFrame with renamed columns if successful, None if an error occurs.
        """
        return self.column_helper.rename_all_columns(dataframe, list_of_columns)

    def reorder_columns(self, dataframe: pd.DataFrame, reordered_columns: List[str]) -> Optional[pd.DataFrame]:
        """
        Reorder columns in the DataFrame.

        Args:
            dataframe (pd.DataFrame): The input DataFrame.
            reordered_columns (List[str]): List of column names in desired order.

        Returns:
            Optional[pd.DataFrame]: DataFrame with reordered columns if successful, None if an error occurs.
        """
        return self.column_helper.reorder_columns(dataframe, reordered_columns)

    # -----------------------------
    # TYPE METHODS
    # -----------------------------
    def change_field_to_datetime(
        self, 
        dataframe: pd.DataFrame, 
        field_names: List[str], 
        date_time_format: str = '%Y-%m-%d %H:%M:%S'
    ) -> Optional[pd.DataFrame]:
        """
        Convert specified columns to datetime type.

        Args:
            dataframe (pd.DataFrame): The input DataFrame.
            field_names (List[str]): List of column names to convert.
            date_time_format (str, optional): Expected datetime format. Defaults to '%Y-%m-%d %H:%M:%S'.

        Returns:
            Optional[pd.DataFrame]: DataFrame with converted datetime columns if successful, None if an error occurs.
        """
        return self.type_helper.change_field_to_datetime(dataframe, field_names, date_time_format)

    def change_field_to_date(
        self, 
        dataframe: pd.DataFrame, 
        field_names: List[str], 
        date_time_format: str = '%Y-%m-%d %H:%M:%S'
    ) -> Optional[pd.DataFrame]:
        """
        Convert specified columns to date type.

        Args:
            dataframe (pd.DataFrame): The input DataFrame.
            field_names (List[str]): List of column names to convert.
            date_time_format (str, optional): Expected datetime format. Defaults to '%Y-%m-%d %H:%M:%S'.

        Returns:
            Optional[pd.DataFrame]: DataFrame with converted date columns if successful, None if an error occurs.
        """
        return self.type_helper.change_field_to_date(dataframe, field_names, date_time_format)

    def change_field_to_number(
        self, 
        dataframe: pd.DataFrame, 
        field_names: List[str], 
        replace_errors_with_0: bool = False
    ) -> Optional[pd.DataFrame]:
        """
        Convert specified columns to numeric type.

        Args:
            dataframe (pd.DataFrame): The input DataFrame.
            field_names (List[str]): List of column names to convert.
            replace_errors_with_0 (bool, optional): Whether to replace conversion errors with 0. Defaults to False.

        Returns:
            Optional[pd.DataFrame]: DataFrame with converted numeric columns if successful, None if an error occurs.
        """
        return self.type_helper.change_field_to_number(dataframe, field_names, replace_errors_with_0)

    # -----------------------------
    # CONTENT METHODS
    # -----------------------------
    def get_values_from_row(self, dataframe_to_query: pd.DataFrame, row_to_query: int) -> Optional[Any]:
        """
        Get values from a specific row in the DataFrame.

        Args:
            dataframe_to_query (pd.DataFrame): The input DataFrame.
            row_to_query (int): Index of the row to query.

        Returns:
            Optional[Any]: Row values if successful, None if an error occurs.
        """
        return self.content_helper.get_values_from_row(dataframe_to_query, row_to_query)

    def set_first_row_as_header(self, dataframe_to_process: pd.DataFrame) -> Optional[pd.DataFrame]:
        """
        Use the first row of the DataFrame as column headers.

        Args:
            dataframe_to_process (pd.DataFrame): The input DataFrame.

        Returns:
            Optional[pd.DataFrame]: DataFrame with new headers if successful, None if an error occurs.
        """
        return self.content_helper.set_first_row_as_header(dataframe_to_process)

    def clear_nans(self, dataframe: pd.DataFrame) -> Optional[pd.DataFrame]:
        """
        Replace all NaN values with empty strings.

        Args:
            dataframe (pd.DataFrame): The input DataFrame.

        Returns:
            Optional[pd.DataFrame]: DataFrame with NaNs replaced if successful, None if an error occurs.
        """
        return self.content_helper.clear_nans(dataframe)

    def replace_nas_with_zeros(self, dataframe: pd.DataFrame, column_name_to_check: str) -> Optional[pd.DataFrame]:
        """
        Replace NaN values with zeros in a specific column.

        Args:
            dataframe (pd.DataFrame): The input DataFrame.
            column_name_to_check (str): Name of the column to process.

        Returns:
            Optional[pd.DataFrame]: DataFrame with NaNs replaced with zeros if successful, None if an error occurs.
        """
        return self.content_helper.replace_nas_with_zeros(dataframe, column_name_to_check)

    def filter_out_nas_and_blanks(self, dataframe: pd.DataFrame, column_name_to_check: str) -> Optional[pd.DataFrame]:
        """
        Remove rows where specified column contains NaN or blank values.

        Args:
            dataframe (pd.DataFrame): The input DataFrame.
            column_name_to_check (str): Name of the column to check.

        Returns:
            Optional[pd.DataFrame]: Filtered DataFrame if successful, None if an error occurs.
        """
        return self.content_helper.filter_out_nas_and_blanks(dataframe, column_name_to_check)

    def remove_duplicate_rows(self, dataframe: pd.DataFrame) -> Optional[pd.DataFrame]:
        """
        Remove duplicate rows from the DataFrame.

        Args:
            dataframe (pd.DataFrame): The input DataFrame.

        Returns:
            Optional[pd.DataFrame]: DataFrame with duplicates removed if successful, None if an error occurs.
        """
        return self.content_helper.remove_duplicate_rows(dataframe)

    # -----------------------------
    # CLEANING METHODS
    # -----------------------------
    def remove_special_characters_from_column(
        self, 
        dataframe_to_clean: pd.DataFrame, 
        column_name_to_clean: str
    ) -> Optional[pd.DataFrame]:
        """
        Remove special characters from specified column.

        Args:
            dataframe_to_clean (pd.DataFrame): The input DataFrame.
            column_name_to_clean (str): Name of the column to clean.

        Returns:
            Optional[pd.DataFrame]: DataFrame with cleaned column if successful, None if an error occurs.
        """
        return self.cleaning_helper.remove_special_characters_from_column(dataframe_to_clean, column_name_to_clean)

    def trim_values_in_columns(self, dataframe_to_clean: pd.DataFrame, field_names: List[str]) -> Optional[pd.DataFrame]:
        """
        Remove leading and trailing whitespace from specified columns.

        Args:
            dataframe_to_clean (pd.DataFrame): The input DataFrame.
            field_names (List[str]): List of column names to trim.

        Returns:
            Optional[pd.DataFrame]: DataFrame with trimmed values if successful, None if an error occurs.
        """
        return self.cleaning_helper.trim_values_in_columns(dataframe_to_clean, field_names)

    def remove_linebreaks_from_dataframe(self, dataframe_to_clean: pd.DataFrame) -> Optional[pd.DataFrame]:
        """
        Remove line breaks from all cells in the DataFrame.

        Args:
            dataframe_to_clean (pd.DataFrame): The input DataFrame.

        Returns:
            Optional[pd.DataFrame]: DataFrame with line breaks removed if successful, None if an error occurs.
        """
        return self.cleaning_helper.remove_linebreaks_from_dataframe(dataframe_to_clean)

    def remove_columns_from_start_of_dataframe(
        self, 
        dataframe_to_adjust: pd.DataFrame, 
        number_of_columns_to_remove: int
    ) -> Optional[pd.DataFrame]:
        """
        Remove specified number of columns from the start of the DataFrame.

        Args:
            dataframe_to_adjust (pd.DataFrame): The input DataFrame.
            number_of_columns_to_remove (int): Number of columns to remove from start.

        Returns:
            Optional[pd.DataFrame]: DataFrame with columns removed if successful, None if an error occurs.
        """
        return self.cleaning_helper.remove_columns_from_start_of_dataframe(dataframe_to_adjust, number_of_columns_to_remove)

    def remove_columns_from_end_of_dataframe(
        self, 
        dataframe_to_adjust: pd.DataFrame, 
        number_of_columns_to_remove: int
    ) -> Optional[pd.DataFrame]:
        """
        Remove specified number of columns from the end of the DataFrame.

        Args:
            dataframe_to_adjust (pd.DataFrame): The input DataFrame.
            number_of_columns_to_remove (int): Number of columns to remove from end.

        Returns:
            Optional[pd.DataFrame]: DataFrame with columns removed if successful, None if an error occurs.
        """
        return self.cleaning_helper.remove_columns_from_end_of_dataframe(dataframe_to_adjust, number_of_columns_to_remove)

    def remove_rows_from_start_of_dataframe(
        self, 
        dataframe_to_adjust: pd.DataFrame, 
        number_of_rows_to_remove: int
    ) -> Optional[pd.DataFrame]:
        """
        Remove specified number of rows from the start of the DataFrame.

        Args:
            dataframe_to_adjust (pd.DataFrame): The input DataFrame.
            number_of_rows_to_remove (int): Number of rows to remove from start.

        Returns:
            Optional[pd.DataFrame]: DataFrame with rows removed if successful, None if an error occurs.
        """
        return self.cleaning_helper.remove_rows_from_start_of_dataframe(dataframe_to_adjust, number_of_rows_to_remove)

    # -----------------------------
    # MERGE METHODS
    # -----------------------------
    def left_merge_dataframes(
        self, 
        left_dataframe: pd.DataFrame, 
        right_dataframe: pd.DataFrame, 
        common_field_name: str
    ) -> Optional[pd.DataFrame]:
        """
        Perform a left merge of two DataFrames on a common field.

        Args:
            left_dataframe (pd.DataFrame): The left DataFrame.
            right_dataframe (pd.DataFrame): The right DataFrame.
            common_field_name (str): The field name common to both DataFrames.

        Returns:
            Optional[pd.DataFrame]: Merged DataFrame if successful, None if an error occurs.
        """
        return self.merge_helper.left_merge_dataframes(left_dataframe, right_dataframe, common_field_name)

    def left_merge_dataframes_on_multiple_fields(
        self,
        left_dataframe: pd.DataFrame,
        right_dataframe: pd.DataFrame,
        left_field_name: Union[str, List[str]],
        right_field_name: Union[str, List[str]],
        add_indicator: bool = False
    ) -> Optional[pd.DataFrame]:
        """
        Perform a left merge of two DataFrames on multiple fields.

        Args:
            left_dataframe (pd.DataFrame): The left DataFrame.
            right_dataframe (pd.DataFrame): The right DataFrame.
            left_field_name (Union[str, List[str]]): Field(s) from left DataFrame.
            right_field_name (Union[str, List[str]]): Field(s) from right DataFrame.
            add_indicator (bool, optional): Add merge indicator column. Defaults to False.

        Returns:
            Optional[pd.DataFrame]: Merged DataFrame if successful, None if an error occurs.
        """
        return self.merge_helper.left_merge_dataframes_on_multiple_fields(
            left_dataframe, right_dataframe, left_field_name, right_field_name, add_indicator
        )

    def merge_dataframes_with_field_mapping(
        self,
        left_dataframe: pd.DataFrame,
        right_dataframe: pd.DataFrame,
        field_mapping: Dict[str, str],
        how: str = 'left',
        add_indicator: bool = False
    ) -> Optional[pd.DataFrame]:
        """
        Merge two DataFrames using a field mapping dictionary.

        Args:
            left_dataframe (pd.DataFrame): The left DataFrame.
            right_dataframe (pd.DataFrame): The right DataFrame.
            field_mapping (Dict[str, str]): Dictionary mapping left DataFrame fields to right DataFrame fields.
            how (str, optional): Type of merge to perform. Defaults to 'left'.
            add_indicator (bool, optional): Add merge indicator column. Defaults to False.

        Returns:
            Optional[pd.DataFrame]: Merged DataFrame if successful, None if an error occurs.
        """
        return self.merge_helper.merge_dataframes_with_field_mapping(
            left_dataframe, right_dataframe, field_mapping, how, add_indicator
        )

    def append_dataframes(
        self, 
        dataframe_to_append_to: pd.DataFrame, 
        dataframe_to_append: pd.DataFrame
    ) -> Optional[pd.DataFrame]:
        """
        Append one DataFrame to another.

        Args:
            dataframe_to_append_to (pd.DataFrame): The base DataFrame.
            dataframe_to_append (pd.DataFrame): The DataFrame to append.

        Returns:
            Optional[pd.DataFrame]: Combined DataFrame if successful, None if an error occurs.
        """
        return self.merge_helper.append_dataframes(dataframe_to_append_to, dataframe_to_append)





