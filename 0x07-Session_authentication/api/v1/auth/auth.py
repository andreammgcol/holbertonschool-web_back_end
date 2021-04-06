#!/usr/bin/env python3
""" Auth class """

from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """ Class to manage the API authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method that returns False - path and excluded_paths
        """
        if not path or not excluded_paths:
            return True
        if path[-1] != '/':
            path += '/'
        for p in excluded_paths:
            if path[:p.find('*')] in p[:p.find('*')]:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Method that returns None - request
        """
        if not request:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ Method that returns None
        """
        return None

    def session_cookie(self, request=None):
        """ Method that returns a cookie value from a request
        """
        if request:
            return request.cookies.get(getenv('SESSION_NAME'))
