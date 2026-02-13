#!/usr/bin/env python3
""" LIFO Caching"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Inherits from BaseCaching and is a caching system"""

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.pop(key)

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = next(reversed(self.cache_data))
            self.cache_data.pop(last_key)
            print(f"DISCARD: {last_key}")

        self.cache_data[key] = item
        return self.cache_data

    def get(self, key):
        """ Get an item by key
        """
        if key not in self.cache_data or key is None:
            return
        return self.cache_data[key]
