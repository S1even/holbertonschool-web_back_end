#!/usr/bin/env python3
"""function that multiplies a float by a multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Takes a float multiplier as an argument and returns a function"""
    def multiply(n: float) -> float:
        """return product of n and multiplier"""
        return n * multiplier
    return multiply
