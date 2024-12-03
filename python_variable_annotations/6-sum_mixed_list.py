#!/usr/bin/env python3
"""function that returns the sum of a list of mixed floats and integers"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Takes a list of integers and floats and returns their sum as a float"""
    return sum(mxd_lst)
