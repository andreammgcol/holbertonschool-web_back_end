#!/usr/bin/env python3
"""
Encrypting and validate passwords
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """that expects one string argument name password
    and returns a salted """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ that expects 2 arguments and returns a boolean """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
