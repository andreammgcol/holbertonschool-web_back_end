#!/usr/bin/env python3
""" Regex-ing """
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ that return the log message obfuscated """
    for f in fields:
        message = re.sub(f'(?<={f}=)[^{separator}]*', redaction, message)
    return message
