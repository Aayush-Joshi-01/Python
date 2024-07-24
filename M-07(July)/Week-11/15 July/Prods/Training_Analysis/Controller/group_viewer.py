import pandas as pd
from time import sleep
from Decorators.Logger_Analysis import analysis_logger

@analysis_logger
def show_data(grouped_data: pd.DataFrame, type_name: str, columns: list[str]=[]) -> None:
    print(f"Showing Data Grouped by {type_name}: .... ")
    print(grouped_data.head().set_index('S.No')[columns])