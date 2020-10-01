import re
from collections import defaultdict
from pprint import pprint

import pandas as pd
from spacy.matcher import PhraseMatcher

from prepare import prepare_data, remove_punct
from settings import (
    NLP_ENG,
    SELECT_ROWS_BY_RANGE,
    ROW_RANGE,
    LAST_ROWS_ONLY,
    REDUCE_ROWS,
    CATEGORIES_FILE,
    DEBUG,
)
from utils import timeit

PHRASES = [
    "I love concentrated apricot juice. I can also drink blueberry-juices or concentrated Blueberry juices",
    "Blueberry juices - that's my fav. But, I also love concentrated apricot juice",
    "Blueberry juice - that's my fav. But, I also love concentrated apricot juices",
    "I like Refrigerated squeezed apple juices",
    "I like lemon juice and granulated sugar on my pancakes.",
    "I like lemon juice and granulated sugars on my pancakes.",
]


def get_phrase_matcher(match_dict):
    matcher = PhraseMatcher(NLP_ENG.vocab)
    match_phrases = match_dict.keys()

    # Using make_doc to speed things up
    patterns = [NLP_ENG.make_doc(match_phrase) for match_phrase in match_phrases]
    matcher.add("Categories", None, *patterns)

    return matcher


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


def match_phrases(phrase, matcher):
    doc = NLP_ENG(phrase)
    matches = matcher(doc)

    match_strings = set()

    for match_id, start, end in matches:
        span = doc[start:end]
        match_strings.add(span.text)

    return match_strings


def output_matches(match_dict, match_strings, phrase):
    print(f"\n\n{phrase}")
    print(f"\nmatch_strings:")
    pprint(match_strings)
    print()
    for match_string in match_strings:
        print("matched category:", match_dict[match_string])


@timeit
def match_categories_in_phrases(match_dict, matcher, phrases):
    for phrase in phrases:
        phrase = re.sub(r"\s+", " ", remove_punct(phrase.lower().lstrip().rstrip()))
        match_strings = match_phrases(phrase, matcher)
        output_matches(match_dict, match_strings, phrase)


@timeit
def setup(categories_file):
    categories_file_df = pd.read_csv(categories_file, sep="\t", header=0)

    if REDUCE_ROWS:
        categories_file_df = get_reduced_df(categories_file_df)

    # create the phrase-matcher object
    categories_series = categories_file_df["category"].astype("string")
    categories_df = prepare_data(categories_series)
    match_dict = get_match_dict(categories_df)
    matcher = get_phrase_matcher(match_dict)

    return categories_df, match_dict, matcher


def main(phrases):
    categories_df, match_dict, matcher = setup(CATEGORIES_FILE)
    match_categories_in_phrases(match_dict, matcher, phrases)

    if DEBUG:
        print_df(categories_df)


if __name__ == "__main__":
    main(PHRASES)
