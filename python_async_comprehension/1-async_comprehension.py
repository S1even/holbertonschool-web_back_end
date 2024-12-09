#!/usr/bin/env python3
"""Module for async_comprehension coroutine."""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 random numbers using async comprehending over async_generator.

    Returns:
        A list of 10 random floats collected from async_generator.
    """
    return [number async for number in async_generator()]
