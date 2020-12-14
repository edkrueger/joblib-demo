"""Build the timefunc decorator."""

import time
import functools


def timefunc(func):
    """timefunc's doc"""

    @functools.wraps(func)
    def time_wrapper(*args, **kwargs):
        """time_wrapper's doc string"""
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"Function: {func.__name__}, Time: {time.perf_counter() - start}")
        return result

    return time_wrapper
