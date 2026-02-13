#!/usr/bin/python3
"""MRU Caching"""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """Inherits from BaseCaching and is a caching system"""
    def __init__(self):
        super().__init__()
        self.od = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.od.move_to_end(key)
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            recent_use = next(iter(self.od))
            self.cache_data.pop(recent_use)
            self.od.pop(recent_use)
            print(f"DISCARD: {recent_use}")
        self.cache_data[key] = item
        self.od[key] = None
        self.od.move_to_end(key, False)
        return self.cache_data

    def get(self, key):
        """ Get an item by key
        """
        if key not in self.cache_data or key is None:
            return
        self.od.move_to_end(key, False)
        return self.cache_data[key]
