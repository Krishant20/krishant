import logging


class Baseclass:
    def test_logging(self):
        logger = logging.getLogger(__name__)

        filehandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.CRITICAL)
        return logger