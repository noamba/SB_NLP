import re
from pprint import pprint

from app.nlp.prepare_data import remove_punct
from app.settings import NLP_ENG, DEBUG
from app.nlp.utils import timeit


def match_phrases(phrase, matcher):
    doc = NLP_ENG(phrase)
    matches = matcher(doc)

    match_strings = set()

    for match_id, start, end in matches:
        span = doc[start:end]
        match_strings.add(span.text)

    return match_strings


def output_matches(phrase, cleaned_phrase, match_strings, matched_categories):
    print("Phrase:", phrase)
    print("Cleaned phrase:", cleaned_phrase)
    print(f"Matched strings:")
    pprint(match_strings)
    print("Matched categories:")
    pprint(matched_categories)
    print("\n\n")


def clean_string(phrase):
    return re.sub(r"\s+", " ", remove_punct(phrase.lower().lstrip().rstrip()))


@timeit
def get_matched_categories_in_phrase(match_dict, matcher, phrase):
    cleaned_phrase = clean_string(phrase)
    match_strings = match_phrases(cleaned_phrase, matcher)
    matched_categories = []

    for match_string in match_strings:
        matched_categories.append(match_dict[match_string])

    if DEBUG:
        output_matches(phrase, cleaned_phrase, match_strings, matched_categories)

    return matched_categories
