#!/usr/bin/env python3
""" Redis client """

import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps
import sys


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


def call_history(method: Callable) -> Callable:
    """ that create input and output list keys, respectively
    """
    @wraps(method)
    def wrapper(self, *args, **kwds):
        """ wrapped function """
        self._redis.rpush(method.__qualname__ + ':inputs', str(args))
        output = method(self, *args, **kwds)
        self._redis.rpush(method.__qualname__ + ':outputs', output)
        return output
    return wrapper


def replay(method: Callable):
    """ function to display the history of calls of a particular
    """
    rds = redis.Redis()
    name = method.__qualname__
    count = rds.get(name).decode('utf-8')
    inputs = rds.lrange(name + ':inputs', 0, -1)
    outputs = rds.lrange(name + ':outputs', 0, -1)
    print('{} was called {} times:'.format(name, count))
    for i, o in zip(inputs, outputs):
        print('{}(*{}) -> {}'.format(name, i.decode('utf-8'),
                                     o.decode('utf-8')))


class Cache:
    """ Cache class
    """
    def __init__(self):
        """ initialize """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
