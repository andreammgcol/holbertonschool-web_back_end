#!/usr/bin/env python3
""" Simple helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Function return a tuple of size two containing
    a start index and an end index """
    index = (page * page_size - page_size, page * page_size)
    return index
