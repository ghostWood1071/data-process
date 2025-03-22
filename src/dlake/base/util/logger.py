import logging

from dlake.base.config import Constants


class Logger:
    @staticmethod
    def get_logger(name: str = "ROOT"):
        logging.basicConfig(
            format=Constants.LOG_FORMAT, datefmt=Constants.LOG_DATE_FORMAT
        )
        logger = logging.getLogger(name)
        logger.setLevel(Constants.LOG_LEVEL)
        return logger
