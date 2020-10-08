from nlp.prepare_data import lemmatize, clean_string
from nlp.utils import timeit, output_matches
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


@timeit
def get_matched_categories_in_phrase(match_dict, matcher, phrase):
    """Return the matched categories found in the given phrase.

    Try to match on:
        - The cleaned lemmatized phrase *and*
        - The cleaned (non-lemmatized) phrase 
    This latter will improve matches on non-English words/phrases.

    Args:
        match_dict: {dict} dict of category match-phrase keys and original
            category values
        matcher: {Spacy PhraseMatcher} a PhraseMatcher object with category
            match-phrases added to it
        phrase: {string} a string to check if there are any categories in it

    Returns: {set} the matched categories
    """
    matched_original_categories = set()
    cleaned_phrase = clean_string(phrase)

    for processed_phrase in [lemmatize(cleaned_phrase), cleaned_phrase]:
        for match_phrase in get_matches(processed_phrase, matcher):
            matched_original_categories.update(match_dict[match_phrase])

    if DEBUG:
        output_matches(phrase, matched_original_categories)

    return matched_original_categories
