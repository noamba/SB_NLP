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
from nlp.utils import load_objects_from_disk, save_object_to_disk
from settings import (
    CATEGORIES_FILE,
    DEBUG,
    REDUCE_CATEGORY_SET_SIZE,
    SAVE_MATCH_OBJECTS_TO_DISK,
    LOAD_MATCH_OBJECTS_FROM_DISK,
    MATCH_DICT_PICKLE_FILE,
    PHRASE_MATCHER_PICKLE_FILE,
)

DEMO_PHRASE = "I love Vanilla-sugar  but I can`t handle vergeoises in any given day..."


def get_match_objects(reduce_category_set_size):
    if LOAD_MATCH_OBJECTS_FROM_DISK:
        print("Loading match objects from disk...")
        match_dict = load_objects_from_disk(MATCH_DICT_PICKLE_FILE)
        phrase_matcher = load_objects_from_disk(PHRASE_MATCHER_PICKLE_FILE)
    else:
        print("Creating match objects from scratch...")
        # set up required objects for matching categories to a phrase
        categories = get_categories(CATEGORIES_FILE, reduce_category_set_size)
        prepared_data = prepare_data(categories)

        if DEBUG == "Full":
            output_categories_df(prepared_data)

        match_dict = get_match_dict(prepared_data)
        phrase_matcher = get_phrase_matcher(match_dict)

        if SAVE_MATCH_OBJECTS_TO_DISK:
            save_object_to_disk(object_to_save=match_dict,
                                path=MATCH_DICT_PICKLE_FILE)
            save_object_to_disk(object_to_save=phrase_matcher,
                                path=PHRASE_MATCHER_PICKLE_FILE)

    return match_dict, phrase_matcher


def configure_routes(app, reduce_category_set_size=REDUCE_CATEGORY_SET_SIZE):
    match_dict, phrase_matcher = get_match_objects(reduce_category_set_size)

    @app.route("/")
    def find_categories_in_phrase():
        phrase = request.args.get("text", default=DEMO_PHRASE, type=str)

        return json.dumps(
            get_matched_categories_in_phrase(match_dict, phrase_matcher, phrase)
        )
