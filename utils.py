from time import perf_counter


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