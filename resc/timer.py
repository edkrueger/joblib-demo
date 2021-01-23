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
        end = time.perf_counter() - start
        print(f"Function: {func.__name__}, Time: {end}")
        return result

    return time_wrapper
