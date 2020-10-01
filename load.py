import pandas as pd

from prepare import prepare_data

CATEGORIES_FILE = "/home/n/code/streetbees/SB_NLP/off_categories.tsv"


def get_phrase_match(categories_df):



    print(categories_df[["match_phrase", "language"]].tail())

    # for index, row in categories.iterrows():
    #     print(row.match_phrase, row.language)

    #   add cleaned + lemmatized

    # create dict from keys: cleaned + lemmatized to values

    # create phrase match object

    # drop the df?

    # match on input


def main():
    categories_file_df = pd.read_csv(CATEGORIES_FILE, sep="\t", header=0)

    # create a string series from categories_file_df
    categories_series = categories_file_df["category"].astype("string")

    # create the data structure required for creating the phrase-match object
    categories_df = prepare_data(categories_series)

    get_phrase_match(categories_df)


if __name__ == "__main__":
    main()
