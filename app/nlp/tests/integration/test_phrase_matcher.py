import pytest

from conftest import (
    phrases_with_ONE_category,
    phrases_with_NO_categories,
    phrases_with_TWO_category,
)
from nlp.match_categories import get_matched_categories_in_phrase


@pytest.mark.parametrize(
    "phrases_and_matches",
    [
        phrases_with_NO_categories(),
        phrases_with_ONE_category(),
        phrases_with_TWO_category(),
    ],
)
def test_find_one_category_in_phrase(
    match_dict_fixture, phrase_match_fixture, phrases_and_matches
):
    """Integration test for the process of finding matching categories in a
     phrase"""
    for phrase, matches in phrases_and_matches:
        matched_categories = get_matched_categories_in_phrase(
            match_dict_fixture, phrase_match_fixture, phrase
        )

        assert matched_categories == matches
