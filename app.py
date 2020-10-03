import json

from flask import Flask
from flask import request

from nlp.match_categories import get_matched_categories_in_phrase
from nlp.prepare_data import prepare_data
from settings import CATEGORIES_FILE, REDUCE_CATEGORY_SET_SIZE, DEBUG
from nlp.setup_phrase_match import (
    get_categories,
    output_categories_df,
    get_match_dict,
    get_phrase_matcher,
)

DEMO_PHRASE = (
    "Blueberry juices - that`s my favourite. "
    "But, I also love concentrated apricot juice"
)

app = Flask(__name__)

# set up required objects for matching categories to a phrase
categories = get_categories(CATEGORIES_FILE, REDUCE_CATEGORY_SET_SIZE)
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


if __name__ == "__main__":
    app.run(debug=True)
