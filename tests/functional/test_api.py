import json
from urllib.parse import quote_plus

import pytest

from conftest import (
    phrases_with_ONE_category,
    phrases_with_NO_categories,
    phrases_with_TWO_category,
)
from nlp.match_categories import get_matched_categories_in_phrase


@pytest.mark.parametrize(
    "phrases, expected_matches",
    [
        (phrases_with_NO_categories(), 0),
        (phrases_with_ONE_category(), 1),
        (phrases_with_TWO_category(), 2),
    ],
)
def test_base_route_with_a_phrase_with_matches(
    match_dict_fixture, phrase_match_fixture, client, phrases, expected_matches
):
    url_prefix = "/?text="

    for phrase in phrases:
        matched_categories_expected = get_matched_categories_in_phrase(
            match_dict_fixture, phrase_match_fixture, phrase
        )

        url = url_prefix + quote_plus(phrase)
        response = client.get(url)
        matched_categories_in_response = json.loads(response.get_data())

        assert response.status_code == 200
        assert set(matched_categories_in_response) == set(matched_categories_expected)
