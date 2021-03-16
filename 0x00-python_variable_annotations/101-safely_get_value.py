#!/usr/bin/env python3

""" More involved type annotations """

from typing import TypeVar, Union, Any, Mapping

t = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[t, None] = None) -> Union[Any, t]:
    """ type annotations"""
    if key in dct:
        return dct[key]
    else:
        return default
