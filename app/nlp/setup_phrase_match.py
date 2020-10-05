from collections import defaultdict

import pandas as pd
from spacy.matcher import PhraseMatcher

from nlp.utils import timeit
from settings import NLP_ENG


@timeit
def get_phrase_matcher(match_dict):
    """Create a Spacy PhraseMatcher object and add match-phrases to it.
    The values in match_dict are the cleaned and lemmatized categories from
    which to create the phrase-matcher.

    Args:
        match_dict: {dict} the keys of this dict to be used to create
            the phrase-matcher

    Returns: {PhraseMatcher} PhraseMatcher object
    """
    matcher = PhraseMatcher(NLP_ENG.vocab, validate=True)
    match_phrases = match_dict.keys()

    # Using make_doc to speed things up
    patterns = [NLP_ENG.make_doc(match_phrase) for match_phrase in match_phrases]
    matcher.add("Categories", None, *patterns)

    return matcher


@timeit
def get_match_dict(categories_df):
    """Create a dictionary from the
    cleaned and lemmatized data in categories_df dataframe.

    The structure of the dict will be:
        {match-phrase : {category_A, category_B, ...}, ...}
    The result will look something like this:
        {"bluberry juice": {"Blueberry juices"},
         "juice": {"ar:juice", "juices",...},
         ...}

    Args:
        categories_df: {pandas DataFrame} includes cleaned + lemmatized strings

    Returns: {dict}
    """
    match_dict = defaultdict(set)
    # create dict like so:
    # keys: cleaned + lemmatized categories,
    # values: original categories
    # Note: some keys will have more than one category, e.g.:
    # "pandoros" : {[}"it:pandoros", "fr:pandoros"}
    for index, row in categories_df.iterrows():
        match_dict[row.match_phrase].add(row.category)
        if row.match_phrase_lemma:
            match_dict[row.match_phrase_lemma].add(row.category)

    return match_dict


def output_categories_df(categories_df):
    """Output contents of dataframe"""
    for index, row in categories_df.iterrows():
        print(
            row.category,
            row.match_phrase,
            row.language or "No language",
            row.match_phrase_lemma,
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
