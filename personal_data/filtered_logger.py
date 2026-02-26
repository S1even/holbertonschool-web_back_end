#!/usr/bin/env python3
"""
Module for filtering sensitive information from log messages.
"""
import re
import logging
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ Returns the log message obfuscated using a single regex. """
    return re.sub(r"({})=.*?{}".format('|'.join(fields), separator),
                  r"\1={}{}".format(redaction, separator), message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class to filter PII from log records. """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Initialize with the fields to be redacted. """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Filters values in incoming log records using filter_datum. """
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)
