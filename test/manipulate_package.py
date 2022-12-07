import htfidf
import pandas as pd


help(htfidf)
help(htfidf.h_tfidf_highest_scores)

# download the dataset: https://dataverse.cirad.fr/dataset.xhtml?persistentId=doi:10.18167/DVN1/JZM34U
df = pd.read_excel(r"data/PADI-web_dataset_manuallyEvaluated_20112017.xls", sheet_name="PADI-web AI")
df["text"] = df["cases"]
df["geo"] = df["country"]
df["datetime"] = df["dates"]
df = df[["text", "geo", "datetime"]]

htfidf_results = htfidf.h_tfidf_highest_scores(data=df, spatial_level="country", temporal_level="month", top_n="10")