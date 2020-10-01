from collections import namedtuple
from time import perf_counter

import pandas as pd

from prepare import prepare_data

CATEGORIES_FILE = "/home/n/code/streetbees/SB_NLP/off_categories.tsv"

# Reduce rows
REDUCE_ROWS = True
SELECT_ROWS_BY_RANGE = True

select_rows = namedtuple("rows", ["first", "last"])
ROWS = select_rows(10, 20)

LAST_ROWS_ONLY = -300

PRINT = True


def get_phrase_match(categories_df):
    pass
    # create dict from keys: cleaned + lemmatized to values

    # create phrase match object


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


def main():

    categories_file_df = pd.read_csv(CATEGORIES_FILE, sep="\t", header=0)

    if REDUCE_ROWS:
        categories_file_df = get_reduced_df(categories_file_df)

    # create a string series from categories_file_df
    categories_series = categories_file_df["category"].astype("string")

    # create the data structure required for creating the phrase-match object
    categories_df = prepare_data(categories_series)

    get_phrase_match(categories_df)

    # drop the df?

    # match on input

    if PRINT:
        print_df(categories_df)


if __name__ == "__main__":
    start = perf_counter()
    main()
    end = perf_counter()
    print("\n\nprocess time:", end - start)
