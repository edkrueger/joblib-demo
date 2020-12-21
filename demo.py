"""
Demo a few different approaches to speed up repeated use of a function.
"""

import multiprocessing
from functools import cache
from random import randint

from joblib import Memory, Parallel, delayed

from mypythonpackage.resc import factors
from mypythonpackage.timer import timefunc

f = factors


@timefunc
def single_thread(inputs):
    """
    Compute single threaded.
    """
    return [f(x) for x in inputs]


@timefunc
def single_thread_with_cache(inputs):
    """
    Compute single threaded with cache.
    """
    f_memoized = cache(f)
    return [f_memoized(x) for x in inputs]


@timefunc
def multiprocess(inputs):
    """
    Compute multiprocess.
    """
    return Parallel(n_jobs=-1)(delayed(f)(x) for x in inputs)


@timefunc
def multiprocess_with_cache(inputs):
    """
    Compute multiprocess with one memory mapped cache.
    """
    location = "./cachedir"
    memory = Memory(location, verbose=0)
    f_memoized = memory.cache(f)
    return Parallel(n_jobs=-1)(delayed(f_memoized)(x) for x in inputs)


@timefunc
def batch_multiprocess(inputs):
    """
    Compute multiprocess with one batch per process.
    """
    len_inputs = len(inputs)
    n_batches = multiprocessing.cpu_count()
    batch_size = len_inputs // n_batches

    batches = []
    for i in range(n_batches):
        start = batch_size * i
        end = (i + 1) * batch_size if i != n_batches - 1 else len_inputs
        batch = inputs[start:end]
        batches.append(batch)

    return Parallel(n_jobs=-1)(
        delayed(single_thread.__wrapped__)(batch) for batch in batches
    )


@timefunc
def batch_multiprocess_caches(inputs):
    """
    Compute multiprocess with one batch and one cache per process.
    """
    len_inputs = len(inputs)
    n_batches = multiprocessing.cpu_count()
    batch_size = len_inputs // n_batches

    batches = []
    for i in range(n_batches):
        start = batch_size * i
        end = (i + 1) * batch_size if i != n_batches - 1 else len_inputs
        batch = inputs[start:end]
        batches.append(batch)

    return Parallel(n_jobs=-1)(
        delayed(single_thread_with_cache.__wrapped__)(batch) for batch in batches
    )


if __name__ == "__main__":

    demo_inputs = [randint(1, 100) for _ in range(10_000)]

    single_thread(demo_inputs)
    single_thread_with_cache(demo_inputs)
    multiprocess(demo_inputs)
    multiprocess_with_cache(demo_inputs)
    batch_multiprocess(demo_inputs)
    batch_multiprocess_caches(demo_inputs)
