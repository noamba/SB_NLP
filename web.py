import json

from flask import Flask
from flask import request

from match_categories import get_matched_categories_in_phrase
from settings import DEMO_PHRASES
from setup_phrase_match import setup

app = Flask(__name__)

match_dict, phrase_matcher = setup()


@app.route("/")
def find_categories():
    phrase = request.args.get("text", default=DEMO_PHRASES[0], type=str)

    return json.dumps(
        get_matched_categories_in_phrase(match_dict, phrase_matcher, phrase)
    )
