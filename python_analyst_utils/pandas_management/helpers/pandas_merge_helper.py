import pandas as pd
from typing import Optional, Dict, Union, List

class PandasMergeHelper:
    def left_merge_dataframes(
        self,
        left_dataframe: pd.DataFrame,
        right_dataframe: pd.DataFrame,
        common_field_name: str
    ) -> Optional[pd.DataFrame]:
        try:
            return pd.merge(
                left_dataframe, 
                right_dataframe, 
                on=common_field_name, 
                how='left'
            )
        except Exception as e:
            print('Exception in left_merge_dataframes', e)
            return None

    def left_merge_dataframes_on_multiple_fields(
        self,
        left_dataframe: pd.DataFrame,
        right_dataframe: pd.DataFrame,
        left_field_name: Union[str, List[str]],
        right_field_name: Union[str, List[str]],
        add_indicator: bool = False
    ) -> Optional[pd.DataFrame]:
        try:
            return pd.merge(
                left_dataframe,
                right_dataframe,
                left_on=left_field_name,
                right_on=right_field_name,
                how='left',
                indicator=add_indicator
            )
        except Exception as e:
            print('Exception in left_merge_dataframes_on_multiple_fields', e)
            return None

    def merge_dataframes_with_field_mapping(
        self,
        left_dataframe: pd.DataFrame,
        right_dataframe: pd.DataFrame,
        field_mapping: Dict[str, str],
        how: str = 'left',
        add_indicator: bool = False
    ) -> Optional[pd.DataFrame]:
        try:
            left_fields = list(field_mapping.keys())
            right_fields = list(field_mapping.values())
            return pd.merge(
                left_dataframe,
                right_dataframe,
                left_on=left_fields,
                right_on=right_fields,
                how=how,
                indicator=add_indicator
            )
        except Exception as e:
            print('Exception in merge_dataframes_with_field_mapping:', e)
            return None

    def append_dataframes(
        self,
        dataframe_to_append_to: pd.DataFrame,
        dataframe_to_append: pd.DataFrame
    ) -> Optional[pd.DataFrame]:
        try:
            if dataframe_to_append_to.empty:
                return dataframe_to_append
            return pd.concat(
                [dataframe_to_append_to, dataframe_to_append],
                ignore_index=True
            )
        except Exception as e:
            print('Exception in append_dataframes', e)
            return None