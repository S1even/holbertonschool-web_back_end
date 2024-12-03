#!/usr/bin/env python3
"""function that measures the runtime of executing concurrent coroutines"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Spawns wait_random n times with the specified max_delay
    and returns a list of delays in ascending order.
    """
    baslangic = time.time()
    asyncio.run(wait_n(n, max_delay))
    bitis = time.time()
    toplam = (bitis - baslangic) / n
    return toplam
