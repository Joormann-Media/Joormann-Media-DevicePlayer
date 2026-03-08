from __future__ import annotations

import logging


def configure_logger(level: str = 'INFO') -> logging.Logger:
    logger = logging.getLogger('deviceplayer')
    if logger.handlers:
        return logger

    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    logger.setLevel(getattr(logging, str(level or 'INFO').upper(), logging.INFO))
    logger.propagate = False
    return logger
