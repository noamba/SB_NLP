import string

import spacy

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
NLP_ENG = spacy.load("en_core_web_sm")

TRANSLATE_TABLE = {
    ord(punctuation_char): " " for punctuation_char in string.punctuation
}