"""
Definition of Fibonacci Sequence:
f(0) = 0
f(1) = 1
f(n) = f(n-1) + f(n-2)

Fibonacci Sequence:
i: 0, 1, 2, 3, 4, 5, 6
f(i): 0, 1, 1, 2, 3, 5, 8, 13, ...
"""

from resc.tracer import tracefunc
from resc.timer import timefunc
from functools import cache


def fibo_iter(num):
    """Iterative Fibo."""

    if num == 0:
        return 0

    second_to_last = 0
    last = 1

    for _ in range(1, num):
        second_to_last, last = last, second_to_last + last

    return last


def fibo_rec(num):
    """Recursive Fibo."""
    return num if num <= 1 else fibo_rec(num - 1) + fibo_rec(num - 2)


@tracefunc
def traced_fibo_rec(num):
    """Recursive Fibo."""
    return num if num <= 1 else traced_fibo_rec(num - 1) + traced_fibo_rec(num - 2)


@cache
def cached_fibo_rec(num):
    """Recursive Fibo."""
    return num if num <= 1 else cached_fibo_rec(num - 1) + cached_fibo_rec(num - 2)


if __name__ == "__main__":

    # timing

    timed_fibo_iter = timefunc(fibo_iter)
    timed_fibo_rec = timefunc(fibo_rec)
    timed_cached_fibo_rec = timefunc(cached_fibo_rec)

    timed_fibo_iter(20)  # O(n)
    timed_fibo_rec(20)  # O(n*log(n))
    timed_cached_fibo_rec(20)  # O(n)

    # why recursive takes longer
    # traced_fibo_rec(10)

    # Python can only handle a certain number of recursive calls
    timed_fibo_iter(1000)
    timed_cached_fibo_rec(1000)


# @tracefunc


# @tracefunc
# def fibo_kwargs(num):
#     """Recursive Fibo."""
#     return num if num <= 1 else fibo_kwargs(num=num - 1) + fibo_kwargs(num=num - 2)

# fibo(5)
# fibo_kwargs(num=5)
