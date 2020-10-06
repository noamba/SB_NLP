import pickle
from pprint import pprint
from time import perf_counter, sleep

from settings import DEBUG, NLP_ENG


def timeit(func):
    """Time func execution if in DEBUG mode. Used as decorator"""
    if not DEBUG:
        return func

    def timed(*args, **kw):
        start = perf_counter()
        result = func(*args, **kw)
        end = perf_counter()

        elapsed_time = end - start
        print(
            f"{'>>> ' if elapsed_time > 2 else ''}"
            f"{func.__name__} process time: {elapsed_time}\n"
        )

        return result

    return timed


@timeit
def save_object_to_disk(object_to_save, path):
    """Save (pickle) an object to disk"""
    print(f"Saving object to {path}...")

    with open(path, "wb") as f:
        pickle.dump(object_to_save, f)

    sleep(1)  # TODO: This may be needed to avoid a save/load issue with docker?


@timeit
def load_objects_from_disk(path):
    """Load (unpickle) an object from disk"""
    print(f"Loading object from {path}...")
    with open(path, "rb") as f:
        loaded_object = pickle.load(f)

    sleep(1)  # TODO: This may be needed to avoid a save/load issue with docker?

    return loaded_object


def lemmatize(phrase):
    """Lemmatize words in the phrase.
    Note: The Space large English model includes some foreign words.
    """
    doc = NLP_ENG(phrase)

    lemmatized_list = []
    for token in doc:
        lemmatized_list.append(token.lemma_)

    return " ".join(lemmatized_list)


def output_matches(phrase, cleaned_phrase, match_strings, matched_categories):
    """Send data to output"""
    print("Phrase:", phrase)
    print("Cleaned phrase:", cleaned_phrase)
    print(f"Matched strings:")
    pprint(match_strings)
    print("Matched categories:")
    pprint(matched_categories)
    print("\n")
