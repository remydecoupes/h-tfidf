import pandas as pd

def h_tfidf_higgest_scores(data: pd.DataFrame,
                           spatial_level: str,
                           temporal_level: str,
                           top_n: int) -> pd.DataFrame:
    list_spatial_level = ["city", "state", "country"]
    list_temporal_level = ["day", "week", "month", "year"]
    if spatial_level not in list_spatial_level:
        raise ValueError(f"Wrong spatial level, please select a value from: {list_spatial_level}")
    if temporal_level not in list_temporal_level:
        raise ValueError(f"Wrong temporal level, please select value from list: {list_temporal_level}")

