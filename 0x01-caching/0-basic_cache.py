#!/usr/bin/python3
"""
Basic caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Basic caching system
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Method to save data in cache"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Method to get a key from cache"""
        return self.cache_data.get(key)
