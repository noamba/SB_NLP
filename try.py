from setup_phrase_match import setup
from match_categories import get_matched_categories_in_phrase
from settings import DEMO_PHRASES

if __name__ == "__main__":
    match_dict, phrase_matcher = setup()

    for phrase in DEMO_PHRASES:
        matched_categories = get_matched_categories_in_phrase(
            match_dict, phrase_matcher, phrase
        )
