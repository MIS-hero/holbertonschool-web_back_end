#!/usr/bin/env python3
"""This module provides a function to create a
key-value tuple with a squared value."""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple containing a string and the square of a number.

    Args:
        k (str): the key string
        v (Union[int, float]): a number to square

    Returns:
        Tuple[str, float]: a tuple (k, v squared)
    """
    return (k, float(v ** 2))
