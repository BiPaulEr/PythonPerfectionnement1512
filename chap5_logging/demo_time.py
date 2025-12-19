import logging, os, time
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
path = os.path.join(os.path.dirname(__file__), "time.log")
rotating_handler = TimedRotatingFileHandler(path, when="m", interval=1, backupCount=3)
formatter = logging.Formatter("%(asctime)s %(message)s")
rotating_handler.setFormatter(formatter)
logger.addHandler(rotating_handler)

def info():
    logger.debug("DEBUG")
    logger.info("INFO")
    logger.warning("WARNING")
    logger.error("ERROR")
    logger.critical("CRITICAL")
    logger.log(logging.CRITICAL, "CRITICAL")

for i in range(0, 100000000):
    time.sleep(5)
    info()