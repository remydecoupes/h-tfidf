import pandas as pd

def h_tfidf_higgest_scores(data: pd.DataFrame,
                           spatial_level: str,
                           temporal_level: str,
                           top_n: int) -> pd.DataFrame:
    """

    :param data: A pandas dataframe containing at least 3 columns :
        - text: raw textual data
        - geo: spatial information
        - period: temporal information
    :param spatial_level: at which spatial level H-TFIDF will be computed
    :param temporal_level: at which temporal level H-TFIDF will be computed
    :param top_n: The N top number of higgest H-TFIDF scores per space and time windows
    :return: a pandas dataframe with 3 columns:
        - geo-period: space and time windows
        - list_ranked_terms: list of ranked terms for the geo-period window
        - list_rannked_scores: list of H-TFIDF scores
    """
    # Check args
    list_spatial_level = ["city", "state", "country"]
    list_temporal_level = ["day", "week", "month", "year"]
    if spatial_level not in list_spatial_level:
        raise ValueError(f"Wrong spatial level, please select a value from: {list_spatial_level}")
    if temporal_level not in list_temporal_level:
        raise ValueError(f"Wrong temporal level, please select value from list: {list_temporal_level}")
    if "text" or "geo" or "period" not in data:
        raise ValueError(f"Data are badly formatted. Column names needed: text, geo and period ")


