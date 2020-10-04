import json

from flask import request

from app.nlp.match_categories import get_matched_categories_in_phrase

DEMO_PHRASE = "I love Vanilla-sugar  but I can`t handle vergeoises in any given day..."


def configure_routes(app, match_dict, phrase_matcher):
    @app.route("/")
    def find_categories_in_phrase():
        phrase = request.args.get("text", default=DEMO_PHRASE, type=str)

        return json.dumps(
            get_matched_categories_in_phrase(match_dict, phrase_matcher, phrase)
        )
