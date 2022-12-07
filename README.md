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