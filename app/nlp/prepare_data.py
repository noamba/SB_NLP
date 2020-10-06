import numpy as np

from nlp.utils import timeit, lemmatize
from settings import TRANSLATE_TABLE


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
    """Add the lemma of each clean_category string in categories_df
    to a new column.
    
    Args:
        categories_df: {pandas DataFrame} a DataFrame with strings in 
            the clean_category column
    
    Returns: {pandas DataFrame} with the additional clean_category_lemma column
    """

    # TODO: Can try to optimize time for this function - it's quite slow

    categories_df["clean_category_lemma"] = ""

    def add_lemma_to_row(row):
        row.clean_category_lemma = lemmatize(row.clean_category)
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

    # add clean_category column
    categories_df["clean_category"] = categories_df["category"]

    # lower clean_category
    categories_df.clean_category = categories_df.clean_category.str.lower()

    # create and populate language column
    categories_df["language"] = categories_df.clean_category.apply(extract_language)

    # remove language from clean_category
    categories_df.clean_category = categories_df.clean_category.apply(remove_language)

    # remove punctuation from clean_category
    categories_df.clean_category = categories_df.clean_category.apply(remove_punct)

    # remove from clean_category spaces on left side
    categories_df.clean_category = categories_df.clean_category.str.lstrip()

    # remove from clean_category spaces on right side
    categories_df.clean_category = categories_df.clean_category.str.rstrip()

    # replace extra spaces in from clean_category
    categories_df.clean_category = categories_df.clean_category.replace(
        r"\s+", " ", regex=True
    )

    # add to the df a column of lemmatized clean_category
    categories_df = add_lemma(categories_df)

    return categories_df
