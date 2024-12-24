import pandas as pd
from typing import Optional, List

class PandasCleaningHelper:
    def remove_special_characters_from_column(
        self,
        dataframe_to_clean: pd.DataFrame,
        column_name_to_clean: str
    ) -> Optional[pd.DataFrame]:
        try:
            dataframe_to_clean[column_name_to_clean] = dataframe_to_clean[column_name_to_clean].str.replace(";", "-")
            return dataframe_to_clean
        except Exception as e:
            print('Exception in remove_special_characters_from_column', e)
            return None

    def trim_values_in_columns(
        self,
        dataframe_to_clean: pd.DataFrame,
        field_names: List[str]
    ) -> Optional[pd.DataFrame]:
        try:
            for field_name in field_names:
                dataframe_to_clean[field_name] = dataframe_to_clean[field_name].str.strip()
            return dataframe_to_clean
        except Exception as e:
            print('Exception in trim_values_in_columns', e)
            return None

    def remove_linebreaks_from_dataframe(
        self,
        dataframe_to_clean: pd.DataFrame
    ) -> Optional[pd.DataFrame]:
        try:
            dataframe_to_clean.replace(
                to_replace=[r"\n", r"\r"], 
                value=[" ", " "], 
                regex=True, 
                inplace=True
            )
            return dataframe_to_clean
        except Exception as e:
            print('Exception in remove_linebreaks_from_dataframe', e)
            return None

    def remove_columns_from_start_of_dataframe(
        self,
        dataframe_to_adjust: pd.DataFrame,
        number_of_columns_to_remove: int
    ) -> Optional[pd.DataFrame]:
        try:
            return dataframe_to_adjust.iloc[:, number_of_columns_to_remove:]
        except Exception as e:
            print('Exception in remove_columns_from_start_of_dataframe', e)
            return None

    def remove_columns_from_end_of_dataframe(
        self,
        dataframe_to_adjust: pd.DataFrame,
        number_of_columns_to_remove: int
    ) -> Optional[pd.DataFrame]:
        try:
            return dataframe_to_adjust.drop(
                columns=dataframe_to_adjust.columns[(-1 * number_of_columns_to_remove):])
        except Exception as e:
            print('Exception in remove_columns_from_end_of_dataframe', e)
            return None

    def remove_rows_from_start_of_dataframe(
        self,
        dataframe_to_adjust: pd.DataFrame,
        number_of_rows_to_remove: int
    ) -> Optional[pd.DataFrame]:
        try:
            return dataframe_to_adjust.iloc[number_of_rows_to_remove:].reset_index(drop=True)
        except Exception as e:
            print('Exception in remove_rows_from_start_of_dataframe', e)
            return None