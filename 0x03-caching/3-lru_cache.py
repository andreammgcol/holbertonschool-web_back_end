#!/usr/bin/env python3
""" LRU caching """

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ class that inherits from BaseCaching """
    def __init__(self):
        """ initialize LRU caching"""
        super().__init__()
        self.tmp = []

    def put(self, key, item):
        """ method assign to the dictionary
        the item value for the key """
        if key and item:
            if self.cache_data.get(key):
                self.tmp.remove(key)
            self.tmp.append(key)
            self.cache_data[key] = item
            if len(self.tmp) > self.MAX_ITEMS:
                discard = self.tmp.pop(0)
                self.cache_data.pop(discard)
                print('DISCARD: {}'.format(discard))

    def get(self, key):
        """ method return the value linked to key """
        if self.cache_data.get(key):
            self.tmp.remove(key)
            self.tmp.append(key)
        return self.cache_data.get(key)
