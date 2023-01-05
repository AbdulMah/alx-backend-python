#!/usr/bin/env python3
""" function"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    if input_list is None:
        return 0
    else:
        return sum(input_list)
