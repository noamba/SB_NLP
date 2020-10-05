import numpy as np

from settings import NON_ENGLISH_LANGUAGES, NLP_ENG, TRANSLATE_TABLE
from nlp.utils import timeit


def extract_language(text):
    """Return the letters signifying language, that is the letters
    before the ':' character text, if it exists. Else return the
    empty string.
    For example, if text is "fr:blah" "fr" will be returned.
    """
    if text is not np.nan and ":" in text:
        return text.split(":")[0]
    else:
        return ""


def remove_language(text):
    """Return text without the letters and colon signifying language.
    For example, if text is "fr:blah" "blah" will be returned.
    """
    if text is not np.nan and ":" in text:
        return text.split(":")[1]
    else:
        return text


def remove_punct(text):
    return text.translate(TRANSLATE_TABLE)


@timeit
def add_lemma(categories_df):
    """Add the lemma of a each match_phrase string in categories_df if 
    it is in English. Add the lemma in a new column.
    
    Args:
        categories_df: {pandas DataFrame} a DataFrame with strings in 
            the match_phrase column
    
    Returns: {pandas DataFrame} with the additional match_phrase_lemma column
    """

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
    """Clean the strings in categories_series and add lemma for english sentences.

    Args:
        categories_series: {pandas Series} a series of strings

    Returns: {pandas DataFrame} the cleaned strings with an additional 
            column for the english lemmatized strings
    """
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
