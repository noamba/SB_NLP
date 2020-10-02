import string
from collections import namedtuple

import spacy

CATEGORIES_FILE = "/home/n/code/streetbees/SB_NLP/off_categories.tsv"

DEBUG = "Basic"  #  "Full" OR "Basic" or None
REDUCE_CATEGORY_SET_SIZE = False

DEMO_PHRASES = [
    "I love concentrated apricot juice. I can also drink blueberry-juices or concentrated Blueberry juices",
    "Blueberry juices - that`s my fav. But, I also love concentrated apricot juice",
    "Blueberry juice - that`s my fav. But, I also love concentrated apricot juices",
    "I like Refrigerated squeezed apple juices",
    "I like lemon juice and granulated sugar on my pancake   ",
    "I like lemon juice and granulated sugars on my pancakes.",
]

# REDUCE_CATEGORY_SET_SIZE variables
SELECT_ROWS_BY_RANGE = True
select_rows = namedtuple("rows", ["first", "last"])
ROW_RANGE = select_rows(10, 20)

LAST_ROWS_ONLY = 300

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
