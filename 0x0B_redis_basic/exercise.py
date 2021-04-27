#!/usr/bin/env python3
""" Redis client """

from redis.client import Redis
import uuid
from typing import Union


class Cache:
    """ Cache class
    """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.mset({key: data})
        return key
