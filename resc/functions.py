"""
Some math functions.
"""


def add(a_num, b_num):
    """Adds two numbers."""
    return a_num + b_num


def sub(a_num, b_num):
    """Subtract two numbers."""
    return a_num - b_num


def factors(a_int):
    """Find factors of an integer."""
    factors_list = []
    for i in range(1, a_int):
        if a_int % i == 0:
            factors_list.append(i)
    return factors_list
