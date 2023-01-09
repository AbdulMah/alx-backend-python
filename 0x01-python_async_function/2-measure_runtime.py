#!/usr/bin/env python3
"""measure time module
"""
import asyncio
import random
from time import perf_counter

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures time of async fun
    """
    counter = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    result = perf_counter() - counter
    return result
