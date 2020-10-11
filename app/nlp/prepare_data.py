import re

from nlp.utils import timeit
from settings import NLP_ENG, TRANSLATE_TABLE

MULTI_WHITE_SPACE_PATTERN = re.compile(r"\s\s+")  # two or more whitespace chars


def remove_punct(text):
    return text.translate(TRANSLATE_TABLE)


@timeit
def prepare_data_set(categories_series):
    """Remove na and duplicate cells from categories_series.

    Args:
        categories_series: {pandas Series} a series of strings

    Returns: {pandas Series} The cleaned Series
    """
    # TODO: check and combine
    categories_series = categories_series.dropna()
    categories_series = categories_series.drop_duplicates()

    return categories_series


def lemmatize(phrase):
    """Lemmatize words in the phrase.
    Note: The Spacy large English model includes some foreign words.
    """
    doc = NLP_ENG(phrase)

    lemmatized_list = []
    for token in doc:
        lemmatized_list.append(token.lemma_)

    return " ".join(lemmatized_list)


def clean_string(phrase):
    """Clean string:
    - Lower case
    - Remove spaces on left and right
    - Remove punctuation
    - Remove extra spaces within the string

    Args:
        phrase: {str} the string to be cleaned

    Returns: {str} the cleaned string
    """
    return MULTI_WHITE_SPACE_PATTERN.sub(
        " ", remove_punct(phrase.lower().lstrip().rstrip())
    )


def get_language(text):
    """Return the letters signifying language in lower case, that is the letters
    before the ':' character in given text, if it exists. Else return the
    empty string.
    For example, if text is "Fr:blah" "fr" will be returned.
    """
    if ":" in text:
        return text.split(":")[0].lower()
    else:
        return ""


def remove_language(text):
    """Return text without the letters and colon signifying language.
    For example, if text is "Fr:blah" "blah" will be returned.
    """
    return text.split(":")[1]
