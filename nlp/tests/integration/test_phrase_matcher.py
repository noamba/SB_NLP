import pytest

from conftest import (
    phrases_with_ONE_category,
    phrases_with_NO_categories,
    phrases_with_TWO_category,
)
from nlp.match_categories import get_matched_categories_in_phrase


@pytest.mark.parametrize(
    "phrases, number_or_matches",
    [
        (phrases_with_NO_categories(), 0),
        (phrases_with_ONE_category(), 1),
        (phrases_with_TWO_category(), 2),
    ],
)
def test_find_one_category_in_phrase(
    match_dict_fixture, phrase_match_fixture, phrases, number_or_matches
):
    for phrase in phrases:
        matched_categories = get_matched_categories_in_phrase(
            match_dict_fixture, phrase_match_fixture, phrase
        )

        assert len(matched_categories) == number_or_matches
