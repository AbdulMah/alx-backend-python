#!/usr/bin/env python3
"""converts a Python variable to a KV pair."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return k, v ** 2
