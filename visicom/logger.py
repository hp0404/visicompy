# -*- coding: utf-8 -*-
import logging


def create_logger(name: str = "visicom.log"):
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


def initialize_logger():
    _logger = create_logger()
    return _logger.info


log = initialize_logger()
