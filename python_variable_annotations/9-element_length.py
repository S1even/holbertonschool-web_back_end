#!/usr/bin/env python3
"""function that returns the length of each element in a list"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples with each element from lst and its length"""
    return [(i, len(i)) for i in lst]
