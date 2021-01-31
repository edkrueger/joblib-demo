"""Tools to implement caching."""

# pylint: disable=too-few-public-methods

import functools


class MemoizedFunction:
    """Takes a function and returns a callable that is a memoized version of that function."""

    def __init__(self, func):
        self.func = func
        self.cache = dict()
        self.cache_hits = 0
        self.n_calls = 0

    def __call__(self, *args):
        self.n_calls += 1
        if not self.cache.get(args):
            self.cache[args] = self.func(*args)
        else:
            self.cache_hits += 1
        return self.cache[args]


def _cache(func):
    """Decorates a function to implement a memo.
    A simpler, less optimized version of functools.cache for demonstration."""

    memo = {}

    @functools.wraps(func)
    def simple_cache_closure(*args, **kwargs):

        # create a key for the memo from args and kwargs
        key = args
        if kwargs:
            # marks the start of the keyword argument in key
            key += (object(),)
            for item in kwargs.items():
                key += item

        if not memo.get(key):
            memo[key] = func(*args, **kwargs)

        return memo[key]

    return simple_cache_closure
