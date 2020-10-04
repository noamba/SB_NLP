from collections import defaultdict

import pandas as pd
from spacy.matcher import PhraseMatcher

from app.nlp.utils import timeit
from app.settings import NLP_ENG


@timeit
def get_phrase_matcher(match_dict):
    matcher = PhraseMatcher(NLP_ENG.vocab, validate=True)
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


def output_categories_df(categories_df):
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

    return categories_file_df["category"].astype("string")
