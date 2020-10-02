from collections import defaultdict

import pandas as pd
from spacy.matcher import PhraseMatcher

from prepare import prepare_data
from settings import (
    NLP_ENG,
    SELECT_ROWS_BY_RANGE,
    ROW_RANGE,
    LAST_ROWS_ONLY,
    REDUCE_CATEGORY_SET_SIZE,
    CATEGORIES_FILE,
    DEBUG,
)
from utils import timeit


@timeit
def get_phrase_matcher(match_dict):
    matcher = PhraseMatcher(NLP_ENG.vocab)
    match_phrases = match_dict.keys()

    # Using make_doc to speed things up
    patterns = [NLP_ENG.make_doc(match_phrase) for match_phrase in match_phrases]
    matcher.add("Categories", None, *patterns)

    return matcher


@timeit
def get_match_dict(categories_df):
    match_dict = defaultdict(str)
    # create dict from keys: cleaned + lemmatized, values: original categories
    for index, row in categories_df.iterrows():
        match_dict[row.match_phrase] = row.category
        if row.match_phrase_lemma:
            match_dict[row.match_phrase_lemma] = row.category

    return match_dict


def get_reduced_df(df):
    if SELECT_ROWS_BY_RANGE:
        df = df[ROW_RANGE.first : ROW_RANGE.last]
    elif LAST_ROWS_ONLY:
        df = df[-LAST_ROWS_ONLY:]

    return df


def print_df(categories_df):
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
    categories_file_df = pd.read_csv(categories_file, sep="\t", header=0)

    if REDUCE_CATEGORY_SET_SIZE:
        categories_file_df = get_reduced_df(categories_file_df)

    return categories_file_df["category"].astype("string")


@timeit
def setup():
    categories = get_categories(CATEGORIES_FILE)
    prepared_data = prepare_data(categories)

    if DEBUG == "Full":
        print_df(prepared_data)

    match_dict = get_match_dict(prepared_data)

    return match_dict, get_phrase_matcher(match_dict)


if __name__ == "__main__":
    match_dict, phrase_matcher = setup()
