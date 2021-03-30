#!/usr/bin/env python3
""" Regex-ing """
import re
from typing import List
import logging


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ constructor """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ method to filter values in incoming log records """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ that return the log message obfuscated """
    for f in fields:
        message = re.sub(f'(?<={f}=)[^{separator}]*', redaction, message)
    return message


def get_logger() -> logging.Logger:
    """ that takes no arguments and returns a logging.Logger object """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagateMsg = False

    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)
