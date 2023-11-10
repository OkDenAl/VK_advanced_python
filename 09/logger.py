import logging


class OptionalFilter(logging.Filter):
    def filter(self, record):
        return "set" not in record.msg


def add_filter(logger):
    for handler in logger.handlers:
        handler.addFilter(OptionalFilter())
    return logger


def init():
    file_handler = logging.FileHandler("cache.log")
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s\t%(levelname)s\t%(message)s")
    file_handler.setFormatter(formatter)
    logger = logging.getLogger("logger")
    logger.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)
    return logger


def add_stdout(logger):
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s\t%(levelname)s\t%(funcName)s:%(lineno)d\t\t%(message)s")
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger
