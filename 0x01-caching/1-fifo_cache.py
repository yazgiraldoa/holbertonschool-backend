#!/usr/bin/python3
"""
FIFO caching
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFO caching class
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Method to save data in cache"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                key_to_delete = ''
                for key in self.cache_data.keys():
                    key_to_delete = key
                    break
                self.cache_data.pop(key_to_delete)
                print('DISCARD: {}'.format(key_to_delete))

    def get(self, key):
        """Method to get a key from cache"""
        return self.cache_data.get(key)
