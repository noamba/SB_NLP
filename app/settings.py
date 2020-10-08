import string

import spacy

DEBUG = None  #  "Full" OR "Basic" OR None for level of debug output

# save/load match objects to disk
PERSIST_MATCH_OBJECTS = True

PHRASE_MATCHER_PICKLE_FILE = "data/pickled_objects/phrase_matcher.pickle"
MATCH_DICT_PICKLE_FILE = "data/pickled_objects/match_dict.pickle"

# TESTING_CATEGORIES_FILE = "data/off_categories_reduced.tsv"
TESTING_CATEGORIES_FILE = "data/off_categories_1000.tsv"

CATEGORIES_FILE = "data/off_categories.tsv"
# CATEGORIES_FILE = TESTING_CATEGORIES_FILE  # useful for testing/debugging

NLP_ENG = spacy.load("en_core_web_lg")

PUNCT_TO_REMOVE = set(string.punctuation) - {"'"}  # excluding apostrophe

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
