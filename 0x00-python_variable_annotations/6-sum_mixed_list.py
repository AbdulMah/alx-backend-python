#!/usr/bin/env python3
"""
a mixed list of integers and floats and returns the sum of all the numbers
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    return sum(mxd_lst)
