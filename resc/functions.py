"""
Some math functions.
"""


def factors(a_int):
    """Find factors of an integer."""
    factors_list = []
    for i in range(1, a_int):
        if a_int % i == 0:
            factors_list.append(i)
    return factors_list
