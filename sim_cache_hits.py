"""
Simulation to determine number of cache hits.

Problem Statement:
n Numbers are generated by a random uniform distribution from 1 to n.
Each of the m numbers is fed, one at a time, into a memoized function.
How many time does the function access a cached value?
"""

import random

from resc.cachetools import MemoizedFunction

MIN_INPUT = 1
MAX_INPUT = 100
NUM_RUNS = 100
NUM_TRIALS = 100_000


def trial():
    """
    Runs a trail feeding m numbers into a memoized function.
    Returns the number of cache hits.
    """

    # pylint: disable=invalid-name

    def f(a):
        """Identity function."""
        return a

    f_memoized = MemoizedFunction(f)

    for _ in range(NUM_RUNS):
        f_input = random.randint(MIN_INPUT, MAX_INPUT)
        f_memoized(f_input)

    return f_memoized.cache_hits


results = [trial() for _ in range(NUM_TRIALS)]
print(sum(results) / len(results))
