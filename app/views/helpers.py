from pprint import pprint

from nlp.prepare_data import prepare_data_set
from nlp.setup_phrase_match import (
    get_categories,
    get_match_dict,
    get_phrase_matcher,
)
from nlp.utils import save_object_to_disk, load_objects_from_disk, timeit
from settings import (
    CATEGORIES_FILE,
    PERSIST_MATCH_OBJECTS,
    MATCH_DICT_PICKLE_FILE,
    PHRASE_MATCHER_PICKLE_FILE,
    DEBUG,
)

@timeit
def create_match_objects(
    categories_file,
    persist_match_objects,
    match_dict_pickle_file,
    phrase_matcher_pickle_file,
):
    """Create match objects. These will be used to match given text against the
    OFF categories.

    Args:
        categories_file: file-system file with tsv categories-data
        persist_match_objects: {bool} load/save match objects to disk
        match_dict_pickle_file: {str} path to match-dictionary pickle file
        phrase_matcher_pickle_file: {str} path to phrase-matcher pickle file

    Returns: {tuple} match_dict, phrase_matcher
    """
    print("Creating match objects from scratch...")
    # set up required objects for matching categories to a phrase
    categories = get_categories(categories_file)
    prepared_data_set = prepare_data_set(categories)

    match_dict = get_match_dict(prepared_data_set)
    if DEBUG == "Full":
        pprint(match_dict)

    phrase_matcher = get_phrase_matcher(match_dict)

    if persist_match_objects:
        save_object_to_disk(object_to_save=match_dict, path=match_dict_pickle_file)
        save_object_to_disk(
            object_to_save=phrase_matcher, path=phrase_matcher_pickle_file
        )

    return match_dict, phrase_matcher

@timeit
def setup_match_objects(
    categories_file=CATEGORIES_FILE,
    persist_match_objects=PERSIST_MATCH_OBJECTS,
    match_dict_pickle_file=MATCH_DICT_PICKLE_FILE,
    phrase_matcher_pickle_file=PHRASE_MATCHER_PICKLE_FILE,
):
    """Get match objects from disk or create them from scratch

    Args:
        categories_file: file-system file with tsv categories-data
        persist_match_objects: {bool} load/save match objects to disk
        match_dict_pickle_file: {str} path to match dictionary pickle file
        phrase_matcher_pickle_file: {str} path to phrase-matcher pickle file

    Returns: {tuple} match_dict, phrase_matcher
    """
    match_dict = phrase_matcher = None

    if persist_match_objects:
        print("Trying to Load match objects from disk...")
        try:
            match_dict = load_objects_from_disk(match_dict_pickle_file)
            phrase_matcher = load_objects_from_disk(phrase_matcher_pickle_file)
        except FileNotFoundError:
            print("Can't find match object/s on disk...")

    if not (match_dict and phrase_matcher):
        match_dict, phrase_matcher = create_match_objects(
            categories_file,
            persist_match_objects,
            match_dict_pickle_file,
            phrase_matcher_pickle_file,
        )

    return match_dict, phrase_matcher
