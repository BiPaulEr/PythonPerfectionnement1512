import schedule
import psutil
import time
import logging
import os

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
path_log = os.path.join(os.path.dirname(__file__), "system.log")
logger.addHandler(logging.FileHandler(path_log))


def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_disk_usage():
    return psutil.disk_usage("C:/").percent

def get_ram_usage():
    return psutil.virtual_memory().percent

def system_log():
    msg = "System Info : " + str(get_cpu_usage()) +" "+ str(get_disk_usage())+ " " + str(get_ram_usage())
    logger.info(msg)

schedule.every(10).seconds.do(system_log)

while True:
    try:
        schedule.run_pending()
        time.sleep(15)
    except KeyboardInterrupt as ki:
        print("System arrete par lutilisateur")
        break

print("end")