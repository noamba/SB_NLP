import pandas as pd

from prepare_data import prepare_data


def test_prepare_data_returns_dataframe_smoke_test(categories_series_fixture):
    """"""
    data = prepare_data(categories_series_fixture)

    assert type(data) == pd.DataFrame