#!/usr/bin/env python3
"""Async generator that yields random numbers between 0 and 10."""

import asyncio
import random


async def async_generator():
    """Yield 10 random numbers asynchronously, pausing 1 second each time."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
