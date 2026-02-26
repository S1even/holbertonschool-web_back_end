#!/usr/bin/env python3
"""
Module for encrypting and validating passwords securely using bcrypt.
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Returns a salted, hashed password using bcrypt.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Checks if a provided password matches a hashed password.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
