import logging

logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)

console_handler = logging.StreamHandler()
logger.addHandler(console_handler)

def info():
    logger.debug("DEBUG")
    logger.info("INFO")
    logger.warning("WARNING")
    logger.error("ERROR")
    logger.critical("CRITICAL")
    logger.log(logging.CRITICAL, "CRITICAL")

info()