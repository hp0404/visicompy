# -*- coding: utf-8 -*-
"""This module contains logging-related utilities."""
import logging
from typing import Callable


def create_logger(name: str = "visicom.log") -> logging.Logger:
    """Creates logger with File & Stream Handlers."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler(name, encoding="utf-8")
    fh.setLevel(logging.DEBUG)
    sh = logging.StreamHandler()
    sh.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s [%(levelname)s]: %(message)s")
    fh.setFormatter(formatter)
    sh.setFormatter(formatter)
    logger.addHandler(fh)
    logger.addHandler(sh)
    return logger


def initialize_logger() -> Callable[..., None]:
    """Creates custom log method."""
    _logger = create_logger()
    return _logger.info


log = initialize_logger()
