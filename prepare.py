import string

import numpy as np

TRANSLATE_TABLE = {
    ord(punctuation_char): " " for punctuation_char in string.punctuation
}


def extract_language(x):
    if x is not np.nan and ":" in x:
        return x.split(":")[0]
    else:
        return ""


def remove_language(x):
    if x is not np.nan and ":" in x:
        return x.split(":")[1]
    else:
        return x


def remove_punct(x):
    return x.translate(TRANSLATE_TABLE)


def add_lemma(categories_df):
    return categories_df


def prepare_data(categories_series):
    # drop missing values
    categories_series = categories_series.dropna()

    # remove duplicates
    categories_series = categories_series.drop_duplicates()

    ####TEMP add with spaces
    # temp_series = pd.Series(
    #     ["Plant-based      foods and beverages", "blah"], name="category"
    # )
    # categories = categories.append(temp_series, ignore_index=True, verify_integrity=True,)

    # create df
    categories_df = categories_series.to_frame()

    # add match_phrase column
    categories_df["match_phrase"] = categories_df["category"]

    # lower match_phrase
    categories_df["match_phrase"] = categories_df["match_phrase"].str.lower()

    # create and populate language column
    categories_df["language"] = categories_df.match_phrase.apply(extract_language)

    # remove language from match phrase
    categories_df.match_phrase = categories_df.match_phrase.apply(remove_language)

    # remove punctuation from match phrase
    categories_df.match_phrase = categories_df.match_phrase.apply(remove_punct)

    # remove spaces on left side
    categories_df.match_phrase = categories_df.match_phrase.str.lstrip()

    # remove spaces on left side
    categories_df.match_phrase = categories_df.match_phrase.str.rstrip()

    # replace extra spaces
    categories_df.match_phrase = categories_df.match_phrase.replace(
        r"\s+", " ", regex=True
    )

    # add a column of lemmatized strings
    categories_df = add_lemma(categories_df)

    return categories_df
