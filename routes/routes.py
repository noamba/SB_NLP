import json

from flask import request

from nlp.match_categories import get_matched_categories_in_phrase
from routes.utils import get_match_objects
from settings import REDUCE_CATEGORY_SET_SIZE

DEMO_PHRASE = "I love Vanilla-sugar  but I can`t handle vergeoises in any given day..."


def configure_routes(app, reduce_category_set_size=REDUCE_CATEGORY_SET_SIZE):
    match_dict, phrase_matcher = get_match_objects(reduce_category_set_size)

    @app.route("/")
    def find_categories_in_phrase():
        phrase = request.args.get("text", default=DEMO_PHRASE, type=str)

        return json.dumps(
            get_matched_categories_in_phrase(match_dict, phrase_matcher, phrase)
        )
