import re
from collections import namedtuple, defaultdict
from pprint import pprint
from time import perf_counter

import pandas as pd
from spacy.matcher import PhraseMatcher

from prepare import prepare_data, remove_punct
from settings import NLP_ENG

CATEGORIES_FILE = "/home/n/code/streetbees/SB_NLP/off_categories.tsv"

# Reduce rows
REDUCE_ROWS = True
SELECT_ROWS_BY_RANGE = True

select_rows = namedtuple("rows", ["first", "last"])
ROWS = select_rows(10, 20)

LAST_ROWS_ONLY = -300

DEBUG = True

PHRASES = [
    "I love concentrated apricot juice but not just that, I can also drink blueberry-juices or concentrated Blueberry juices"
]
# PHRASES = [
#     "Blueberry juices - that's my fav. But, I also love concentrated apricot juice"
# ]
# PHRASES = ["I like Refrigerated squeezed apple juices"]


def get_phrase_matcher(match_dict):

    matcher = PhraseMatcher(NLP_ENG.vocab)
    terms = match_dict.keys()

    # Using make_doc to speed things up
    patterns = [NLP_ENG.make_doc(text) for text in terms]
    matcher.add("Categories", None, *patterns)

    return matcher


def get_match_dict(categories_df):
    match_dict = defaultdict(str)
    # create dict from keys: cleaned + lemmatized to values
    for index, row in categories_df.iterrows():
        match_dict[row.match_phrase] = row.category
        if row.match_phrase_lemma:
            match_dict[row.match_phrase_lemma] = row.category

    return match_dict


def get_reduced_df(df):

    if SELECT_ROWS_BY_RANGE:
        df = df[ROWS.first : ROWS.last]
    elif LAST_ROWS_ONLY:
        df = df[LAST_ROWS_ONLY:]

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

    match_strings = []

    for match_id, start, end in matches:
        span = doc[start:end]
        match_strings.append(span.text)

    return match_strings


def find_matches(match_dict, matcher, phrases):
    for phrase in phrases:

        phrase = re.sub(r"\s+", " ", remove_punct(phrase.lower().lstrip().rstrip()))
        match_strings = match_phrases(phrase, matcher)

        print(phrase)
        print("match_strings:")
        pprint(match_strings)

        for match_string in match_strings:
            print("matched category:", match_dict[match_string])


def main(phrases):

    categories_file_df = pd.read_csv(CATEGORIES_FILE, sep="\t", header=0)

    if REDUCE_ROWS:
        categories_file_df = get_reduced_df(categories_file_df)

    # create the data structure required for creating the phrase-match object
    categories_series = categories_file_df["category"].astype("string")
    categories_df = prepare_data(categories_series)

    match_dict = get_match_dict(categories_df)
    matcher = get_phrase_matcher(match_dict)

    # TODO: I could drop the df at this point to reduce memory footprint.

    find_matches(match_dict, matcher, phrases)

    if DEBUG:
        print_df(categories_df)


if __name__ == "__main__":

    start = perf_counter()
    main(PHRASES)
    end = perf_counter()
    print("\n\nprocess time:", end - start)
