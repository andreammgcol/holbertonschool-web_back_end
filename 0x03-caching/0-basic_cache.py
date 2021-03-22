#!/usr/bin/env python3
""" Basic dictionary """

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ class that inherits from BaseCaching """
    def put(self, key, item):
        """ method assign to the dictionary
        the item value for the key"""
        if key or item:
            self.cache_data[key] = item
        else:
            pass

    def get(self, key):
        """ method return the value linked to key"""
        if key:
            return self.cache_data.get(key)
        else:
            pass
