from collections import namedtuple
from time import perf_counter

import pandas as pd

from prepare import prepare_data

CATEGORIES_FILE = "/home/n/code/streetbees/SB_NLP/off_categories.tsv"


def get_phrase_match(categories_df):
    pass
    # create dict from keys: cleaned + lemmatized to values

    # create phrase match object


def main():
    categories_file_df = pd.read_csv(CATEGORIES_FILE, sep="\t", header=0)

    select_rows = namedtuple("rows", ["first", "last"])

    ROWS = select_rows(10, 20)
    ROWS = None
    # LAST_ROWS_ONLY = -300
    LAST_ROWS_ONLY = None

    if ROWS:
        categories_file_df = categories_file_df[ROWS.first : ROWS.last]
    elif LAST_ROWS_ONLY:
        categories_file_df = categories_file_df[LAST_ROWS_ONLY:]

    # create a string series from categories_file_df
    categories_series = categories_file_df["category"].astype("string")

    # create the data structure required for creating the phrase-match object
    categories_df = prepare_data(categories_series)

    get_phrase_match(categories_df)

    # drop the df?

    # match on input

    if False:
        for index, row in categories_df.iterrows():
            print(
                row.category,
                row.match_phrase,
                row.language or "No language",
                row.match_phrase_lemma,
                sep=",",
            )


if __name__ == "__main__":
    start = perf_counter()
    main()
    end = perf_counter()
    print("\n\nprocess time:", end - start)
