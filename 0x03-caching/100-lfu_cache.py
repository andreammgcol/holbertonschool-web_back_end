#!/usr/bin/env python3
""" LFU caching """

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ class that inherits from BaseCaching """
    def __init__(self):
        """ initialize LFU caching"""
        super().__init__()
        self.tmp = []
        self.lfu = {}

    def put(self, key, item):
        """ method assign to the dictionary
        the item value for the key """
        if key and item:
            if (len(self.tmp) >= self.MAX_ITEMS and
                    not self.cache_data.get(key)):
                discard = self.tmp.pop(0)
                self.lfu.pop(discard)
                self.cache_data.pop(discard)
                print('DISCARD: {}'.format(discard))

            if self.cache_data.get(key):
                self.tmp.remove(key)
                self.lfu[key] += 1
            else:
                self.lfu[key] = 0

            i = 0
            while (i < len(self.tmp) and not self.lfu[self.tmp[i]]):
                i += 1
            self.tmp.insert(i, key)
            self.cache_data[key] = item

    def get(self, key):
        """ method return the value linked to key """
        if self.cache_data.get(key):
            self.lfu[key] += 1
            if self.tmp.index(key) + 1 != len(self.tmp):
                while (self.tmp.index(key) + 1 < len(self.tmp) and
                       self.lfu[key] >=
                       self.lfu[self.tmp[self.tmp.index(key) + 1]]):
                    self.tmp.insert(self.tmp.index(key) + 1,
                                    self.tmp.pop(self.tmp.index(key)))
        return self.cache_data.get(key)
