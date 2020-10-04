from nlp.prepare_data import prepare_data
from nlp.setup_phrase_match import (
    get_categories,
    output_categories_df,
    get_match_dict,
    get_phrase_matcher,
)
from nlp.utils import save_object_to_disk, load_objects_from_disk
from settings import (
    CATEGORIES_FILE,
    DEBUG,
    PERSIST_MATCH_OBJECTS,
    MATCH_DICT_PICKLE_FILE,
    PHRASE_MATCHER_PICKLE_FILE,
)


def create_match_objects(reduce_category_set_size):
    print("Creating match objects from scratch...")
    # set up required objects for matching categories to a phrase
    categories = get_categories(CATEGORIES_FILE, reduce_category_set_size)
    prepared_data = prepare_data(categories)

    if DEBUG == "Full":
        output_categories_df(prepared_data)

    match_dict = get_match_dict(prepared_data)
    phrase_matcher = get_phrase_matcher(match_dict)

    if PERSIST_MATCH_OBJECTS:
        save_object_to_disk(object_to_save=match_dict,
                            path=MATCH_DICT_PICKLE_FILE)
        save_object_to_disk(
            object_to_save=phrase_matcher, path=PHRASE_MATCHER_PICKLE_FILE
        )

    return match_dict, phrase_matcher


def get_match_objects(reduce_category_set_size):
    if PERSIST_MATCH_OBJECTS:
        print("Trying to Load match objects from disk...")
        try:
            match_dict = load_objects_from_disk(MATCH_DICT_PICKLE_FILE)
            phrase_matcher = load_objects_from_disk(PHRASE_MATCHER_PICKLE_FILE)
        except FileNotFoundError:
            print("Can't find match object/s on disk...")
            match_dict, phrase_matcher = create_match_objects(
                reduce_category_set_size)
    else:
        match_dict, phrase_matcher = create_match_objects(
            reduce_category_set_size)

    return match_dict, phrase_matcher
