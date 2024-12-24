import pandas as pd
from typing import Optional, Any

class PandasContentHelper:
    def get_values_from_row(
        self,
        dataframe_to_query: pd.DataFrame,
        row_to_query: int
    ) -> Optional[Any]:
        try:
            return dataframe_to_query.iloc[0, row_to_query:]
        except Exception as e:
            print('Exception in get_values_from_row', e)
            return None

    def set_first_row_as_header(
        self,
        dataframe_to_process: pd.DataFrame
    ) -> Optional[pd.DataFrame]:
        try:
            new_header = dataframe_to_process.iloc[0]
            dataframe_to_process = dataframe_to_process.iloc[1:].reset_index(drop=True)
            dataframe_to_process.columns = new_header
            return dataframe_to_process
        except Exception as e:
            print('Exception in set_first_row_as_header', e)
            return None

    def clear_nans(
        self,
        dataframe: pd.DataFrame
    ) -> Optional[pd.DataFrame]:
        # Create a copy to avoid modifying the original
        df = dataframe.copy()
        
        # Fill numeric columns with 0
        numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns
        df[numeric_columns] = df[numeric_columns].fillna(0)
        
        # Fill non-numeric columns with empty string
        non_numeric_columns = df.select_dtypes(exclude=['int64', 'float64']).columns
        df[non_numeric_columns] = df[non_numeric_columns].fillna('')
        
        return df

    def replace_nas_with_zeros(
        self,
        dataframe: pd.DataFrame,
        column_name_to_check: str
    ) -> Optional[pd.DataFrame]:
        try:
            dataframe[column_name_to_check].fillna(0.0, inplace=True)
            return dataframe
        except Exception as e:
            print('Exception in replace_nas_with_zeros', e)
            return None

    def filter_out_nas_and_blanks(
        self,
        dataframe: pd.DataFrame,
        column_name_to_check: str
    ) -> Optional[pd.DataFrame]:
        try:
            dataframe[column_name_to_check] = dataframe[column_name_to_check].str.strip()
            return dataframe[dataframe[column_name_to_check].notna() & 
                           (dataframe[column_name_to_check] != '')]
        except Exception as e:
            print('Exception in filter_out_nas_and_blanks', e)
            return None

    def remove_duplicate_rows(
        self,
        dataframe: pd.DataFrame
    ) -> Optional[pd.DataFrame]:
        try:
            return dataframe.drop_duplicates().reset_index(drop=True)
        except Exception as e:
            print('Exception in remove_duplicate_rows', e)
            return None