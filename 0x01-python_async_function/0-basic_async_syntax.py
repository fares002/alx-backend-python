#!/usr/bin/env python3
"""
async python
"""

import asyncio
import random


async def wait_random(max_delay=10):
    """
    Asynchronously waits for a random amount of time between
    0 and the specified maximum delay.

    Args:
        max_delay (float): The maximum delay in seconds (default is 10).

    Returns:
        float: The actual waiting time in seconds.
    """
    waiting_time = random.uniform(0, max_delay)
    await asyncio.sleep(waiting_time)
    return waiting_time
