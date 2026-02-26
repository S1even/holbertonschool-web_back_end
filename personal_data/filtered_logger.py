#!/usr/bin/env python3
"""
Module for filtering sensitive information from log messages.
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Returns the log message obfuscated based on the fields provided.

    Args:
        fields: List of strings representing fields to obfuscate.

    Returns:
        The obfuscated log message.
    """
    for field in fields:
        message = re.sub(f'{field}=.*?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message
