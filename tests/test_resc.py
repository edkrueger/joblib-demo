"""
Tests timer.py.
"""
from resc.timer import timefunc


def test_timefunc_same_results():
    """Tests add."""
    # pylint: disable=invalid-name
    def f(x):
        """Identity function."""
        return x

    f_timed = timefunc(f)

    assert f(3) == f_timed(3)
