#!/usr/bin/env python3
"""Async generator that yields random numbers."""

import asyncio
import random


async def async_generator():
    """Yield 10 random numbers asynchronously, waiting 1 second each time."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
