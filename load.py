import string

import pandas as pd
import numpy as np

CATEGORIES_FILE = "/home/n/code/streetbees/SB_NLP/off_categories.tsv"
TRANSLATE_TABLE = {ord(punct): " " for punct in string.punctuation}


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


df = pd.read_csv(CATEGORIES_FILE, sep="\t", header=0)

# create string series from categories
categories = df["category"].astype("string")

# drop missing values
categories = categories.dropna()

# remove duplicates
categories = categories.drop_duplicates()

####TEMP add with spaces
# temp_series = pd.Series(
#     ["Plant-based      foods and beverages", "blah"], name="category"
# )
# categories = categories.append(temp_series, ignore_index=True, verify_integrity=True,)

# create df
categories = categories.to_frame()

# add match_phrase column
categories["match_phrase"] = categories["category"]

# lower match_phrase
categories["match_phrase"] = categories["match_phrase"].str.lower()

# create and populate language column
categories["language"] = categories.match_phrase.apply(extract_language)

# remove language from match phrase
categories.match_phrase = categories.match_phrase.apply(remove_language)

# remove punctuation from match phrase
categories.match_phrase = categories.match_phrase.apply(remove_punct)

# remove spaces on left side
categories.match_phrase = categories.match_phrase.str.lstrip()

# remove trailing spaces
categories.match_phrase = categories.match_phrase.str.rstrip()

# replace extra spaces
categories.match_phrase = categories.match_phrase.replace(r"\s+", " ", regex=True)



#   create ALT: lemmatize


print(categories[["match_phrase", "language"]].tail())

# for index, row in categories.iterrows():
#     print(row.match_phrase, row.language)




#   add cleaned + lemmatized

# create phrase match object

# drop the df?
# create dict from keys: cleaned + lemmatized to values

#
# print(categories.describe())
# print(categories.head())
#
# print("type", type(categories))

# match on input

# print(df)
