#!/usr/bin/env python3
"""Asyncronus python
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously waits for a random amount of time between
    0 and the specified maximum delay, repeated n times.
    Args:
        n (int): The number of times to wait.
        max_delay (float): The maximum delay in seconds (default is 10).
    Returns:
        float: The total waiting time in seconds.
    """
    times = []

    for i in range(1, n):
        waited_time = await wait_random(max_delay)
        times.append(waited_time)
    return sorted(times)
