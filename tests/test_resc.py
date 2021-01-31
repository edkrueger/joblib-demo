"""
Tests timer.py.
"""
from resc.timer import timefunc
from resc.cachetools import MemoizedFunction, _cache


def test_timefunc_same_results():
    """Test that the decorated function returns the same results."""

    # pylint: disable=invalid-name

    def f(x):
        """Identity function."""
        return x

    f_timed = timefunc(f)

    assert f(3) == f_timed(3)


def test_memoized_function_same_results():
    """Test that the callable returns the same results."""

    # pylint: disable=invalid-name

    def f(x):
        """Identity function."""
        return x

    f_memoized = MemoizedFunction(f)
    assert f(2) == f_memoized(2)


def test__cache():
    """Test _cache."""

    # pylint: disable=invalid-name

    def f(x):
        """Identity function."""
        return x

    f_memoized = _cache(f)
    assert f(2) == f_memoized(2)
    assert f(x=2) == f_memoized(x=2)
