from time import perf_counter


def timeit(func):
    def timed(*args, **kw):
        start = perf_counter()
        result = func(*args, **kw)
        end = perf_counter()

        print(f"\n\n{func.__name__} process time:", end - start)

        return result

    return timed
