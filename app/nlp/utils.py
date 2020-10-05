import pickle
from time import perf_counter, sleep


def timeit(func):
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
    print(f"Saving object to {path}...")

    with open(path, "wb") as f:
        pickle.dump(object_to_save, f)

    sleep(1)  # TODO: This may be needed to avoid a save/load issue with docker?


@timeit
def load_objects_from_disk(path):
    print(f"Loading object from {path}...")
    with open(path, "rb") as f:
        loaded_object = pickle.load(f)

    sleep(1)  # TODO: This may be needed to avoid a save/load issue with docker?

    return loaded_object
