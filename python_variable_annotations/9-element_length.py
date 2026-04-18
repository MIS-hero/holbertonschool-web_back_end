#!/usr/bin/env python3
"""This module provides a function that returns elements with their lengths."""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples containing elements and their lengths.

    Args:
        lst (Iterable[Sequence]): iterable of sequence objects

    Returns:
        List[Tuple[Sequence, int]]: list of (element, length) pairs
    """
    return [(i, len(i)) for i in lst]
