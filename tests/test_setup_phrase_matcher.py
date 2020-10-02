import pytest

import pandas as pd

from setup_phrase_match import get_categories
from settings import CATEGORIES_FILE



@pytest.mark.parametrize("reduce_category_set_size", [True, False])
def test_get_categories(reduce_category_set_size):
    categories = get_categories(CATEGORIES_FILE, reduce_category_set_size)

    assert type(categories) == pd.Series
    assert not categories.empty



