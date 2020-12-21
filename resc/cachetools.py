"""Tools to implement caching."""

# pylint: disable=too-few-public-methods


class MemoizedFunction:
    """Takes a function and returns a callable that is a memoized version of that function."""

    def __init__(self, func):
        self.func = func
        self.cache = dict()
        self.cache_hits = 0

    def __call__(self, *args):
        if not self.cache.get(args):
            self.cache[args] = self.func(*args)
        else:
            self.cache_hits += 1
        return self.cache[args]
