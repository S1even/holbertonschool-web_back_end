#!/usr/bin/env python3
"""
Module for filtering and obfuscating sensitive data in log messages,
and connecting to a secure database.
"""

import logging
import mysql.connector
import os
import re
from typing import List


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Obfuscates specified fields in a log message using a single regex.
    """
    return re.sub(rf'({"|".join(fields)})=[^{separator}]*',
                  rf'\1={redaction}', message)


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class to filter sensitive information from logs.
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initializes the formatter with a list of fields to redact.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Formats the log record, masking the sensitive fields.
        """
        formatted_message = super(RedactingFormatter, self).format(record)
        return filter_datum(self.fields, self.REDACTION,
                            formatted_message, self.SEPARATOR)


def get_logger() -> logging.Logger:
    """
    Creates and configures a logger for user data.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(stream_handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Connects to a secure database using environment variables.
    """
    db_user = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    db_pwd = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    db_host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME")

    return mysql.connector.connect(
        user=db_user,
        password=db_pwd,
        host=db_host,
        database=db_name
    )


def main() -> None:
    """
    Retrieves all rows in the users table and displays each row
    under a filtered format.
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    
    # Récupération du nom des colonnes
    headers = [field[0] for field in cursor.description]
    logger = get_logger()

    for row in cursor:
        # Création de la chaîne de caractères "champ=valeur; champ2=valeur2; "
        message = "".join(f"{k}={v}; " for k, v in zip(headers, row))
        # Le strip() supprime l'espace final en trop
        logger.info(message.strip())

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
