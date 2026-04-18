#!/usr/bin/env python3
"""This module provides a function to sum a list of floats."""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return the sum of a list of floating-point numbers.

    Args:
        input_list (List[float]): list of floats to sum

    Returns:
        float: sum of all elements in input_list
    """
    return sum(input_list)