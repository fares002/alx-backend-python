#!/usr/bin/env python3
"""Asyncronus python
"""
import asyncio
from typing import List
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for the wait_n function.
    Args:
        n (int): The number of times to wait.
        max_delay (float): The maximum delay in seconds (default is 10).
    Returns:
        float: The total execution time in seconds.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return end - start
