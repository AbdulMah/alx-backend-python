#!/usr/bin/env python3
""" function"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """  Sums a list 
    Args:
        input_list (list): A list of floats
    Returns:
        float: sum 
    """
    if input_list is None:
        return 0
    else:
        return sum(input_list)
