import json

from flask import Flask
from flask import request

from load import setup, DEMO_PHRASES, match_categories_in_phrase

app = Flask(__name__)

match_dict, phrase_matcher = setup()


@app.route("/")
def find_categories():
    phrase = request.args.get("text", default=DEMO_PHRASES[0], type=str)
    matched_categories = match_categories_in_phrase(match_dict, phrase_matcher, phrase)

    return json.dumps(matched_categories)
