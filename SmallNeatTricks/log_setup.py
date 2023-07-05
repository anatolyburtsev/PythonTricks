import logging

def setup_basic_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler())
    return logger


def setup_formatted_logger(name: str, logging_level=logging.INFO) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging_level)

    handler = logging.StreamHandler()

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger