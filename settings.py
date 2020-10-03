import string
from collections import namedtuple

import spacy

select_rows = namedtuple("rows", ["first", "last"])

# TODO: use Path package?
CATEGORIES_FILE = "data/off_categories.tsv"

DEBUG = "Basic"  #  "Full" OR "Basic" or None
REDUCE_CATEGORY_SET_SIZE = True

# REDUCE_CATEGORY_SET_SIZE variables
ROW_RANGE = select_rows(first=10, last=20)

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
