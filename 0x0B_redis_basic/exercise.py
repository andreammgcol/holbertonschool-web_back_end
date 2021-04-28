#!/usr/bin/env python3
""" Redis client """

import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ decorator that takes a single method Callable argument
        and returns a Callable
    """
    key = method.__qualname__
    @wraps(method)
    def wrapper(self, *args, **kwds):
        """ wrapped function """
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


class Cache:
    """ Cache class
    """
    def __init__(self):
        """ initialize """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ method that takes a data argument and returns a string """
        key = str(uuid.uuid4())
        self._redis.mset({key: data})
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[
            str, bytes, int, float]:
        """ method that take a key string argument """
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, data: str) -> str:
        """ that will automatically parametrize Cache.get """
        return self._redis.get(data).decode('utf-8')

    def get_int(self, data: str) -> int:
        """ that will automatically parametrize Cache.get """
        return int(self._redis.get(data))
