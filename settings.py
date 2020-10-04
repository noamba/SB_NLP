import string
from collections import namedtuple

import spacy

select_rows = namedtuple("rows", ["first", "last"])


DEBUG = "Basic"  #  "Full" OR "Basic" or None for level of debug output

# save/load match objects to disk
PERSIST_MATCH_OBJECTS = True

# files TODO: use Path package?
PHRASE_MATCHER_PICKLE_FILE = "data/pickled_objects/phrase_matcher.pickle"
MATCH_DICT_PICKLE_FILE = "data/pickled_objects/match_dict.pickle"

TESTING_CATEGORIES_FILE = "data/off_categories_reduced.tsv"

CATEGORIES_FILE = "data/off_categories.tsv"
# CATEGORIES_FILE = TESTING_CATEGORIES_FILE  # useful for testing/debugging


# NLP_ENG = spacy.load("en_core_web_sm")
NLP_ENG = spacy.load("en_core_web_lg")

PUNCT_TO_REMOVE = set(string.punctuation) - {"`"}  # excluding asterix

TRANSLATE_TABLE = {ord(punctuation_char): " " for punctuation_char in PUNCT_TO_REMOVE}

LANGUAGES = {
    "ge",
    "cy",
    "vi",
    "he",
    "fi",
    "ch",
    "uk",
    "sq",
    "pt",
    "bg",
    "th",
    "xx",
    "is",
    "ja",
    "el",
    "si",
    "tr",
    "bn",
    "fr",
    "hu",
    "mk",
    "ca",
    "aa",
    "ar",
    "nb",
    "gl",
    "de",
    "ro",
    "lt",
    "sv",
    "pl",
    "fa",
    "sl",
    "cz",
    "nl",
    "it",
    "hr",
    "sk",
    "ru",
    "ka",
    "sr",
    "cs",
    "es",
    "zh",
    "ko",
    "da",
}

NON_ENGLISH_LANGUAGES = LANGUAGES - {"uk"}
