import logging
import subprocess
import sys
# Web Server Imports

from src.Service import ZephyrService as zs
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(funcName)20s() - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
    handlers=[logging.StreamHandler()]
)
log = logging.getLogger(__name__)


# def start_zephyr_instance():
#     # this function will start a zephyr instance, but not kill it
#     log.debug("Running on {} OS".format(sys.platform))
#
#     subprocess.call("windows_script.bat")
#     return

if (__name__ == "__main__"):
    zs.start_zephyr_instance()