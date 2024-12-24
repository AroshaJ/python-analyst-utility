import pandas as pd
from typing import Optional, List

class PandasTypeHelper:
    def change_field_to_datetime(
        self,
        dataframe: pd.DataFrame,
        field_names: List[str],
        date_time_format: str = '%Y-%m-%d %H:%M:%S'
    ) -> Optional[pd.DataFrame]:
        try:
            for field_name in field_names:
                dataframe[field_name] = pd.to_datetime(
                    dataframe[field_name], 
                    format=date_time_format, 
                    errors='coerce'
                )
            return dataframe
        except Exception as e:
            print('Exception in change_field_to_datetime', e)
            return None

    def change_field_to_date(
        self,
        dataframe: pd.DataFrame,
        field_names: List[str],
        date_time_format: str = '%Y-%m-%d %H:%M:%S'
    ) -> Optional[pd.DataFrame]:
        try:
            for field_name in field_names:
                dataframe[field_name] = pd.to_datetime(
                    dataframe[field_name], 
                    format=date_time_format, 
                    errors='coerce'
                )
                dataframe[field_name] = dataframe[field_name].dt.date
            return dataframe
        except Exception as e:
            print('Exception in change_field_to_date', e)
            return None

    def change_field_to_number(
        self,
        dataframe: pd.DataFrame,
        field_names: List[str],
        replace_errors_with_0: bool = False
    ) -> Optional[pd.DataFrame]:
        try:
            for field_name in field_names:
                if replace_errors_with_0:
                    dataframe[field_name] = pd.to_numeric(
                        dataframe[field_name], 
                        errors='coerce'
                    ).fillna(0.0).astype(float)
                else:
                    dataframe[field_name] = pd.to_numeric(
                        dataframe[field_name], 
                        errors='coerce'
                    ).astype(float)
            return dataframe
        except Exception as e:
            print('Exception in change_field_to_number', e)
            return None