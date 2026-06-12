#!/usr/bin/env python3
"""
This module provides a web caching and tracking system using Redis.
It caches HTML content from URLs and tracks the access frequency.
"""
from functools import wraps
import redis
import requests
from typing import Callable

redis_client = redis.Redis()


def cache_and_track(method: Callable) -> Callable:
    """
    A decorator that tracks how many times a URL is accessed and
    caches the fetched HTML content with an expiration time of 10 seconds.
    """
    @wraps(method)
    def wrapper(url: str) -> str:
        """
        Wrapper function that increments the access counter, checks
        the Redis cache, and stores the fresh content if necessary.
        """
        count_key = f"count:{url}"
        redis_client.incr(count_key)

        cache_key = f"cached:{url}"
        cached_content = redis_client.get(cache_key)
        if cached_content:
            return cached_content.decode("utf-8")

        html_content = method(url)

        redis_client.setex(cache_key, 10, html_content)

        return html_content
    return wrapper


@cache_and_track
def get_page(url: str) -> str:
    """
    Obtains the HTML content of a particular URL using the requests module
    and returns it as a string.
    """
    response = requests.get(url)
    return response.text
