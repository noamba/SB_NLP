"""This module includes unit-tests for the setup_phrase_match module"""

import collections

import pandas as pd
import pytest
from spacy.matcher import PhraseMatcher

from settings import CATEGORIES_FILE
from setup_phrase_match import get_categories, get_match_dict, get_phrase_matcher


@pytest.mark.parametrize("reduce_category_set_size", [True, False])
def test_get_categories(reduce_category_set_size):
    """test get_categories function"""
    categories = get_categories(CATEGORIES_FILE, reduce_category_set_size)

    assert type(categories) == pd.Series
    assert not categories.empty


def test_get_match_dict(prepared_data_fixture, categories_series_fixture):
    """test get_match_dict function"""
    match_dict = get_match_dict(prepared_data_fixture)

    assert type(match_dict) == collections.defaultdict
    assert len(match_dict) >= len(prepared_data_fixture) > 0

    # check that a representative match_dict value is one of the
    # original categories
    assert list(match_dict.values())[0] in categories_series_fixture.to_list()


class TestGetPhraseMatcher:
    """tests for get_phrase_matcher function"""

    def test_get_phrase_matcher_returns_PhraseMatcher(self, match_dict_fixture):
        """test get_phrase_matcher returns a PhraseMatcher"""
        phrase_matcher = get_phrase_matcher(match_dict_fixture)

        assert type(phrase_matcher) == PhraseMatcher

    def test_something_else_in_get_phrase_matcher(self):
        """Just an noop test to show how a test *class* could be useful"""
        assert True
