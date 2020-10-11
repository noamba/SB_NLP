import json
from http import HTTPStatus
from urllib.parse import quote_plus

import pytest

from conftest import (
    phrases_with_ONE_category,
    phrases_with_NO_categories,
    phrases_with_TWO_category,
)


@pytest.mark.parametrize(
    "phrases_and_matches",
    [
        phrases_with_NO_categories(),
        phrases_with_ONE_category(),
        phrases_with_TWO_category(),
    ],
)
def test_base_route_with_phrases(
    client, phrases_and_matches,
):
    """Functional test using the API to test the process of finding matching
     categories in a phrase"""
    url_prefix = "/?text="

    for phrase, matches in phrases_and_matches:

        url = url_prefix + quote_plus(phrase)
        response = client.get(url)
        matched_categories_in_response = json.loads(response.get_data())

        assert response.status_code == HTTPStatus.OK
        assert set(matched_categories_in_response) == matches
