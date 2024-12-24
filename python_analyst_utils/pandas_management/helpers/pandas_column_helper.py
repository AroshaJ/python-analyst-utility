import pandas as pd
from typing import Optional, List, Dict

class PandasColumnHelper:
    def keep_selected_columns(
        self, 
        dataframe: pd.DataFrame, 
        columns_to_keep_list: List[str]
    ) -> Optional[pd.DataFrame]:
        try:
            return dataframe[[col for col in columns_to_keep_list if col in dataframe.columns]]
        except Exception as e:
            print('Exception in keep_selected_columns', e)
            return None

    def remove_specific_columns(
        self, 
        dataframe: pd.DataFrame, 
        columns_to_remove: List[str]
    ) -> Optional[pd.DataFrame]:
        try:
            columns_to_remove = [col for col in columns_to_remove if col in dataframe.columns]
            dataframe.drop(columns=columns_to_remove, inplace=True)
            return dataframe
        except Exception as e:
            print('Exception in remove_specific_columns', e)
            return None

    def rename_columns(
        self, 
        dataframe: pd.DataFrame, 
        columns_to_rename_dict: Dict[str, str]
    ) -> Optional[pd.DataFrame]:
        try:
            return dataframe.rename(columns=columns_to_rename_dict)
        except Exception as e:
            print('Exception in rename_columns', e)
            return None

    def rename_all_columns(
        self, 
        dataframe: pd.DataFrame, 
        list_of_columns: List[str]
    ) -> Optional[pd.DataFrame]:
        try:
            dataframe.columns = list_of_columns
            return dataframe
        except Exception as e:
            print('Exception in rename_all_columns', e)
            return None

    def reorder_columns(
        self, 
        dataframe: pd.DataFrame, 
        reordered_columns: List[str]
    ) -> Optional[pd.DataFrame]:
        try:
            remaining_columns = [col for col in dataframe.columns if col not in reordered_columns]
            new_order = reordered_columns + remaining_columns
            return dataframe[new_order]
        except Exception as e:
            print('Exception in reorder_columns', e)
            return None