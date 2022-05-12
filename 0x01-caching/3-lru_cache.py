#!/usr/bin/python3
"""
LIFO caching
"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    LIFO caching class
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Method to save data in cache"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                item = list(self.cache_data.keys())[BaseCaching.MAX_ITEMS - 1]
                self.cache_data.pop(item)
                print('DISCARD: {}'.format(item))

    def get(self, key):
        """Method to get a key from cache"""
        return self.cache_data.get(key)
