import pandas as pd
import pytest
from flask import Flask

from nlp.prepare_data import prepare_data_set
from nlp.setup_phrase_match import get_match_dict, get_phrase_matcher
from views.routes import configure_routes
from views.helpers import setup_match_objects
from settings import TESTING_10_CATEGORIES_FILE


@pytest.fixture
def categories_series_fixture():
    return pd.Series(name="category", data=["Vanilla sugars", "fr:Sucres perlés"])


@pytest.fixture
def prepared_data_fixture(categories_series_fixture):
    return prepare_data_set(categories_series_fixture)


@pytest.fixture
def match_dict_fixture(prepared_data_fixture):
    return get_match_dict(prepared_data_fixture)


@pytest.fixture
def phrase_match_fixture(match_dict_fixture):
    return get_phrase_matcher(match_dict_fixture)

# NOTE: the following phrases have X matched categories in the categories in
# categories_series_fixture
def phrases_with_ONE_category():
    return [
        "I love vanilla sugars and Plant Based foods and beverages",
        "Where can I get that french delicacy, SUCRES perlés?",
    ]


def phrases_with_TWO_category():
    return [
        "I love Vanilla-sugar  but I can`t do sucres perlés on any given day...",
        "Where can I get that french delicacy, SucreS perlés? "
        "Also, are Vanilla   sugars and plant based foods and beverages a fad?",
    ]


def phrases_with_NO_categories():
    return [
        "I love plant foods and beverages",
        "Where can I get that french delicacy, Suc-res perlés?",
    ]


@pytest.fixture
def client():
    """Returns a flask test-client with a reduced categories list"""
    app = Flask(__name__)
    match_dict, phrase_matcher = setup_match_objects(
        categories_file=TESTING_10_CATEGORIES_FILE,
        persist_match_objects=False,
        match_dict_pickle_file=None,
        phrase_matcher_pickle_file=None
    )
    configure_routes(app, match_dict, phrase_matcher)

    return app.test_client()
