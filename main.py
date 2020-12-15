import multiprocessing
from functools import cache
from random import randint

from joblib import Memory, Parallel, delayed

from mypythonpackage.resc import common_factors
from mypythonpackage.timer import timefunc


@timefunc
def single_thread(inputs):
    """
    Compute single threaded.
    """
    return [common_factors(x, y) for x, y in inputs]


@timefunc
def single_thread_with_cache(inputs):
    """
    Compute single threaded.
    """
    cached_common_factors = cache(common_factors)
    return [cached_common_factors(x, y) for x, y in inputs]


@timefunc
def multiprocess(inputs):
    """
    Compute multiprocess.
    """
    return Parallel(n_jobs=-1)(delayed(common_factors)(x, y) for x, y in inputs)


@timefunc
def multiprocess_with_cache(inputs):
    """
    Compute multiprocess with one memory mapped cache.
    """
    location = "./cachedir"
    memory = Memory(location, verbose=0)
    cached_common_factors = memory.cache(common_factors)
    return Parallel(n_jobs=-1)(delayed(cached_common_factors)(x, y) for x, y in inputs)


@timefunc
def batch_multiprocess_caches(inputs):
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


@timefunc
def batch_multiprocess(inputs):
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


inputs = [(randint(1, 100), randint(1, 100)) for _ in range(10_000)]
single_thread(inputs)
single_thread_with_cache(inputs)
multiprocess(inputs)
multiprocess_with_cache(inputs)
batch_multiprocess(inputs)
batch_multiprocess_caches(inputs)
