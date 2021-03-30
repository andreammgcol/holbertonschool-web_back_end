#!/usr/bin/env python3
""" Regex-ing """
import re
from typing import List
import logging
import os
import mysql.connector


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
    logger.propagate = False

    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ connect to a secure holberton database to read a users table """
    connection = mysql.connector.connect(
        user=os.environ.get('PERSONAL_DATA_DB_USERNAME', 'root'),
        password=os.environ.get('PERSONAL_DATA_DB_PASSWORD', ''),
        host=os.environ.get('PERSONAL_DATA_DB_HOST', 'localhost'),
        database=os.environ.get('PERSONAL_DATA_DB_NAME'))
    return connection


def main() -> None:
    """ that takes no arguments and returns nothing """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT CONCAT ('name=', name, ';ssn=', ssn, ';ip=', ip,\
        ';user_agent', user_agent, ';') AS message FROM users;")
    msg = cursor.fetchall()
    rec = logging.LogRecord("my_logger", logging.INFO,
                            None, None, message, None, None)
    formatter = RedactingFormatter(PII_FIELDS)
    formatter.format(rec)
    cursor.close()


if __name__ == "__main__":
    main()
