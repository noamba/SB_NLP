import re

from nlp.prepare_data import remove_punct
from nlp.utils import timeit, lemmatize, output_matches
from settings import NLP_ENG, DEBUG


def get_matches(phrase, matcher):
    """Return the match-strings found in given phrase using the given Spacy
    PhraseMatcher object

    Args:
        phrase: {str} string to check if any matches in it
        matcher: {Spacy PhraseMatcher} a PhraseMatcher with match-strings
            added to it

    Returns: {set} the match-strings found
    """
    doc = NLP_ENG(phrase)
    matches = matcher(doc)

    match_strings = set()

    for match_id, start, end in matches:
        span = doc[start:end]
        match_strings.add(span.text)

    return match_strings


def clean_string(phrase):
    """Lower and clean given string from punctuation and extra spaces"""
    return re.sub(r"\s+", " ", remove_punct(phrase.lower().lstrip().rstrip()))


@timeit
def get_matched_categories_in_phrase(match_dict, matcher, phrase):
    """Return the matched categories found in the given phrase.

    For each phrase try to match on:
        - The cleaned phrase *and*
        - The cleaned lemmatized phrase
    This will improve matches on non-English words/phrases.

    Args:
        match_dict: {dict} dict of match-phrase keys and category values
        matcher: {Spacy PhraseMatcher} a PhraseMatcher object with category
            match phrases added to it
        phrase: {string} a string to check if any categories in it

    Returns: {list} the matched categories
    """
    cleaned_phrase = clean_string(phrase)
    lemmatized_phrase = lemmatize(cleaned_phrase)
    match_strings = get_matches(lemmatized_phrase, matcher)
    match_strings.update(get_matches(cleaned_phrase, matcher))

    matched_categories = []

    for match_string in match_strings:
        matched_categories.extend(match_dict[match_string])

    if DEBUG:
        output_matches(phrase, cleaned_phrase, match_strings, matched_categories)

    return matched_categories
