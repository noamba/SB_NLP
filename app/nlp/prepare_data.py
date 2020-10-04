import numpy as np

from app.settings import NON_ENGLISH_LANGUAGES, NLP_ENG, TRANSLATE_TABLE
from app.nlp.utils import timeit


def extract_language(x):
    if x is not np.nan and ":" in x:
        return x.split(":")[0]
    else:
        return ""


def remove_language(x):
    if x is not np.nan and ":" in x:
        return x.split(":")[1]
    else:
        return x


def remove_punct(x):
    return x.translate(TRANSLATE_TABLE)

@timeit
def add_lemma(categories_df):

    # TODO: Can try to optimize time for this function - it's quite slow

    categories_df["match_phrase_lemma"] = ""

    def add_lemma_to_row(row):
        if row.language in NON_ENGLISH_LANGUAGES:  # currently lemmatize only english
            return row

        doc = NLP_ENG(row.match_phrase)
        row.match_phrase_lemma = " ".join([token.lemma_ for token in doc])

        return row

    return categories_df.apply(add_lemma_to_row, axis=1)

@timeit
def prepare_data(categories_series):
    # drop missing values
    categories_series = categories_series.dropna()

    # remove duplicates
    categories_series = categories_series.drop_duplicates()

    # create df
    categories_df = categories_series.to_frame()

    # add match_phrase column
    categories_df["match_phrase"] = categories_df["category"]

    # lower match_phrase
    categories_df["match_phrase"] = categories_df["match_phrase"].str.lower()

    # create and populate language column
    categories_df["language"] = categories_df.match_phrase.apply(extract_language)

    # remove language from match phrase
    categories_df.match_phrase = categories_df.match_phrase.apply(remove_language)

    # remove punctuation from match phrase
    categories_df.match_phrase = categories_df.match_phrase.apply(remove_punct)

    # remove spaces on left side
    categories_df.match_phrase = categories_df.match_phrase.str.lstrip()

    # remove spaces on left side
    categories_df.match_phrase = categories_df.match_phrase.str.rstrip()

    # replace extra spaces
    categories_df.match_phrase = categories_df.match_phrase.replace(
        r"\s+", " ", regex=True
    )

    # add a column of lemmatized strings
    categories_df = add_lemma(categories_df)

    return categories_df
