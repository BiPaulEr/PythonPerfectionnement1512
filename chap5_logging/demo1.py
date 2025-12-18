import logging

class MyFilter(logging.Filter):
    def filter(self, record):
        if "A" in record.msg:
            return False
        return True


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.addFilter(MyFilter())
logger.addHandler(console_handler)

def info():
    logger.debug("DEBUG")
    logger.info("INFO")
    logger.warning("WARNING")
    logger.error("ERROR")
    logger.critical("CRITICAL")
    logger.log(logging.CRITICAL, "CRITICAL")

info()