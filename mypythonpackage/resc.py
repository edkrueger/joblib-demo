"""
Some math functions.
"""


def add(a_num, b_num):
    """Adds two numbers."""
    return a_num + b_num


def sub(a_num, b_num):
    """Subtract two numbers."""
    return a_num - b_num


def common_factors(a_int, b_int):
    """Find all common factors between two paris of integers."""
    common_factors_list = []
    for i in range(1, min(a_int, b_int)):
        if a_int % i == 0 and b_int % i == 0:
            common_factors_list.append(i)
    return common_factors_list
