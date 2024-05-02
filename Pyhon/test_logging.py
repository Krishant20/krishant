import logging

def test_logging():
    logger = logging.getLogger(__name__)

    filehandler=logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    logger.setLevel(logging.CRITICAL)
    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.warning("Something is in warning code")
    logger.error("A major error has happend")
    logger.critical("critical issue")