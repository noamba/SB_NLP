import pandas as pd
import pytest
from flask import Flask

from nlp.prepare_data import prepare_data
from nlp.setup_phrase_match import get_match_dict, get_phrase_matcher
from routes.routes import configure_routes


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


def phrases_with_ONE_category():
    return [
        "I love plant based foods and beverages",
        "Where can I get that french delicacy, Andouilles?",
    ]


def phrases_with_TWO_category():
    return [
        "I love Plant Based foods and Beverages but I can`t "
        "handle andouilles in any given day...",
        "Where can I get that french delicacy, Andouilles? "
        "Also, are plant based foods and beverages a fad?",
    ]


def phrases_with_NO_categories():
    return [
        "I love plant foods and beverages",
        "Where can I get that french delicacy, Andou-illes?",
    ]


@pytest.fixture
def client():
    """Returns a flask test-client"""
    app = Flask(__name__)
    configure_routes(app, reduce_category_set_size=True)

    return app.test_client()
