<h1 align="center"> H-TFIDF
:mag: :book:
</h1>

A NLP library for discriminant terms extraction in space and time

## Usage
```python
# Load H-TFIDF package
from htfidf import htfidfBestTerms
# Load scikit-learn package
from sklearn.feature_extraction.text import CountVectorizer


# Extract occurence of words in dataset
wordCount = countVectorizer.fit_transform(dataset)

# Extract the top_100 H-TFIDF at a country & month level
H-TFIDF-results = htfidfBestTerms(
    wordCount, 
    spatial_information=dataset.geo,
    spatial_level = "Country",
    temporal_level = "month",
    top_n = 100
    )
```

## Installation :construction:
```bash
pip install htfidf
```

## Scientific publication

| Conference                                      |                            paper                             |                                                                                                                             description                                                                                                                             |
|-------------------------------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| [AGILE'2021](https://agile-giss.copernicus.org/articles/2/index.html) | [Full paper](https://dx.doi.org/10.5194/agile-giss-2-2-2021) | H-TFIDF application to COVID-19 tweets. [For more information, visit the study's repository](https://gitlab.irstea.fr/remy.decoupes/covid19-tweets-mood-tetis). The workflow is fully reproducible, see the [related report](https://doi.org/10.17605/osf.io/rdnyu) |
| [IJID'2022](https://www.sciencedirect.com/journal/international-journal-of-infectious-diseases/vol/116/suppl/S) | [Poster](https://doi.org/10.1016/j.ijid.2021.12.065) |                                                                                                Using H-TFIDF feature for a spatial opinion mining on COVID-19 tweets                                                                                                |