import json

from flask import request

from nlp.match_categories import get_matched_categories_in_phrase
from nlp.prepare_data import prepare_data
from nlp.setup_phrase_match import (
    get_categories,
    output_categories_df,
    get_match_dict,
    get_phrase_matcher,
)
from settings import CATEGORIES_FILE, DEBUG, REDUCE_CATEGORY_SET_SIZE

DEMO_PHRASE = (
    "Blueberry juice - that`s my favourite. "
    "But, I can take concentrated apricot juice on any given day"
)


def configure_routes(app, reduce_category_set_size=REDUCE_CATEGORY_SET_SIZE):

    # set up required objects for matching categories to a phrase
    categories = get_categories(CATEGORIES_FILE, reduce_category_set_size)
    prepared_data = prepare_data(categories)

    if DEBUG == "Full":
        output_categories_df(prepared_data)

    match_dict = get_match_dict(prepared_data)
    phrase_matcher = get_phrase_matcher(match_dict)

    @app.route("/")
    def find_categories_in_phrase():
        phrase = request.args.get("text", default=DEMO_PHRASE, type=str)

        return json.dumps(
            get_matched_categories_in_phrase(match_dict, phrase_matcher, phrase)
        )
