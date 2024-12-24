import pandas as pd
from typing import Optional, List

class PandasDiagnosticHelper:
    def get_list_of_columns(self, dataframe: pd.DataFrame) -> Optional[List[str]]:
        try:
            return dataframe.columns.tolist()
        except Exception as e:
            print('Exception in get_list_of_columns', e)
            return None

    def print_dataframe_dimensions(self, dataframe: pd.DataFrame) -> None:
        try:
            num_rows, num_cols = dataframe.shape
            print(f"The DataFrame has {num_rows} rows and {num_cols} columns.")
        except Exception as e:
            print('Exception in print_dataframe_dimensions', e)

    def print_general_info_about_dataframe(self, dataframe: pd.DataFrame) -> None:
        try:
            print(dataframe.info())
        except Exception as e:
            print('Exception in print_general_info_about_dataframe', e)

    def print_list_of_columns(self, dataframe: pd.DataFrame) -> None:
        try:
            for column in dataframe.columns:
                print(column)
        except Exception as e:
            print('Exception in print_list_of_columns', e)