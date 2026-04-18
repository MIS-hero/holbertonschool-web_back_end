#!/usr/bin/env python3
"""This module provides a function that returns a multiplier function."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): the multiplier factor

    Returns:
        Callable[[float], float]: a function that takes a float and
        returns its product with multiplier
    """
    def multiply(x: float) -> float:
        return x * multiplier

    return multiply
