#!/usr/bin/env python3
""" MRU caching """

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ class that inherits from BaseCaching """
    def __init__(self):
        super().__init__()
        self.tmp = []

    def put(self, key, item):
        if key or item:
            if self.cache_data.get(key):
                self.tmp.remove(key)
            while len(self.tmp) >= self.MAX_ITEMS:
                discard = self.tmp.pop()
                self.cache_data.pop(discard)
                print('DISCARD: {}'.format(discard))
            self.tmp.append(key)
            self.cache_data[key] = item
        else:
            pass

    def get(self, key):
        if self.cache_data.get(key):
            self.tmp.remove(key)
            self.tmp.append(key)
        return self.cache_data.get(key)
