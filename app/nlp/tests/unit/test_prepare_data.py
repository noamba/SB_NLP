import pandas as pd

from nlp.prepare_data import prepare_data_set

# TODO: Add tests & docstrings

def test_prepare_data_returns_dataframe_smoke_test(categories_series_fixture):
    data = prepare_data_set(categories_series_fixture)

    assert type(data) == pd.Series