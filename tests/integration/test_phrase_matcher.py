from match_categories import get_matched_categories_in_phrase

PHRASES_WITH_ONE_CATEGORY = [
    "I love plant based foods and beverages",
    "Where can I get that french delicacy, Andouilles?",
]


PHRASES_WITH_TWO_CATEGORIES = [
    "I love Plant Based foods and Beverages but I can`t "
    "handle andouilles in any given day...",
    "Where can I get that french delicacy, Andouilles? "
    "Also, are plant based foods and beverages a fad?",
]

PHRASES_WITH_NO_CATEGORY = [
    "I love plant foods and beverages",
    "Where can I get that french delicacy, Andou-illes?",
]


class TestIntegrationFindCategoriesInPhrase:
    def test_find_one_category_in_phrase(
        self, match_dict_fixture, phrase_match_fixture
    ):

        for phrase in PHRASES_WITH_ONE_CATEGORY:
            matched_categories = get_matched_categories_in_phrase(
                match_dict_fixture, phrase_match_fixture, phrase
            )

            assert len(matched_categories) == 1

    def test_find_two_categories_in_phrase(
        self, match_dict_fixture, phrase_match_fixture
    ):

        for phrase in PHRASES_WITH_TWO_CATEGORIES:
            matched_categories = get_matched_categories_in_phrase(
                match_dict_fixture, phrase_match_fixture, phrase
            )

            assert len(matched_categories) == 2

    def test_find_no_categories_in_phrase(
        self, match_dict_fixture, phrase_match_fixture
    ):

        for phrase in PHRASES_WITH_NO_CATEGORY:
            matched_categories = get_matched_categories_in_phrase(
                match_dict_fixture, phrase_match_fixture, phrase
            )

            assert len(matched_categories) == 0
