from collections import defaultdict

import pandas as pd
from spacy.matcher import PhraseMatcher

from nlp.utils import timeit
from settings import NLP_ENG, NON_ENGLISH_LANGUAGES


@timeit
def get_phrase_matcher(match_dict):
    """Create a Spacy PhraseMatcher object and add match-phrases to it.
    The values in match_dict are the cleaned and lemmatized categories from
    which to create the phrase-matcher.

    Args:
        match_dict: {dict} the keys of this dict to be added to
            the phrase-matcher

    Returns: {PhraseMatcher} PhraseMatcher object
    """
    matcher = PhraseMatcher(NLP_ENG.vocab, validate=True)
    texts_to_match = match_dict.keys()

    # Using make_doc to speed things up
    patterns = (NLP_ENG.make_doc(text) for text in texts_to_match)
    matcher.add("Categories", patterns)

    return matcher


@timeit
def get_match_dict(categories_df):
    """Create a dictionary with keys:
        - The cleaned and lemmatized data and
        - If the category is non-English: The cleaned category as well
    and values: The matching original categories for each key. Some keys
    will have more than one category.

    The structure of the dict will be:
        {match-phrase : {category_A, category_B, ...}, ...}

    The result will look something like this:
        {"bluberry juice": {"Blueberry juices"},
         "juice": {"ar:juice", "juices",...},
         "pandoros" : {"it:pandoros", "fr:pandoros",...}
         "pandoro" : {"it:pandoro", "fr:pandoro",...}
         ...}

    Args:
        categories_df: {pandas DataFrame} includes cleaned + lemmatized strings

    Returns: {dict}
    """
    match_dict = defaultdict(set)

    for index, row in categories_df.iterrows():
        match_dict[row.clean_category_lemma].add(row.category)
        if row.language in NON_ENGLISH_LANGUAGES:
            match_dict[row.clean_category].add(row.category)

    return match_dict


def output_categories_df(categories_df):
    """Output contents of dataframe"""
    for index, row in categories_df.iterrows():
        print(
            row.category,
            row.clean_category,
            row.language or "No language",
            row.clean_category_lemma,
            sep=",",
        )


@timeit
def get_categories(categories_file):
    """Extract OFF categories from categories_file into a pandas dataframe

    Args:
        categories_file: {str} path to OFF categories file

    Returns: {pandas DataFrame} dataframe of the data in categories_file
    """
    categories_file_df = pd.read_csv(categories_file, sep="\t", header=0)

    return categories_file_df["category"].astype("string")
