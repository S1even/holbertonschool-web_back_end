#!/usr/bin/env python3
"""Basic dictionary"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
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
        self.cache_data[key] = item
        return self.cache_data

    def get(self, key):
        """ Get an item by key
        """
        if key not in self.cache_data or key is None:
            return
        return self.cache_data[key]
