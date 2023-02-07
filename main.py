import logging
import subprocess
import sys

# Web Server Imports

# utilities import
import time

from src.Service import ZephyrService as zs

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(funcName)20s() - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
    handlers=[logging.StreamHandler()]
)
log = logging.getLogger(__name__)

if (__name__ == "__main__"):
    SLEEP_TIME = 5
    # zs.start_zephyr_instance()
    for i in range(0, 3):
        process: subprocess.Popen[str] = zs.start_zephyr_instance()
        log.debug("Sleeping for {} seconds, currently on {} iteration".format(SLEEP_TIME, i))
        time.sleep(SLEEP_TIME)
