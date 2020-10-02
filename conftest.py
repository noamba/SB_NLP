import pandas as pd
import pytest

from prepare_data import prepare_data
from setup_phrase_match import get_match_dict, get_phrase_matcher


@pytest.fixture
def categories_series_fixture():
    return pd.Series(
        name="category", data=["Plant-based foods and beverages", "fr:Andouilles"]
    )


@pytest.fixture
def prepared_data_fixture(categories_series_fixture):
    return prepare_data(categories_series_fixture)


@pytest.fixture
def match_dict_fixture(prepared_data_fixture):
    return get_match_dict(prepared_data_fixture)


@pytest.fixture
def phrase_match_fixture(match_dict_fixture):
    return get_phrase_matcher(match_dict_fixture)