import json
import logging
import subprocess
import sys
import time

import psutil

from settings import BASH_PATH
from src.utilities.Constants import *

# Base Configuration
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(funcName)20s() - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
    handlers=[logging.StreamHandler()]
)
log = logging.getLogger(__name__)
current_platform = sys.platform


def start_zephyr_instance(process: subprocess.Popen[str] = None) -> subprocess.Popen[str]:

    log.debug("Starting new Zephyr Instance")
    # kill any QEMU Instance running before starting a new zephyr one
    complete_kill(process)

    if (current_platform == WINDOWS):
        # this function will start a zephyr instance, but not kill it
        log.debug("Running on {} OS".format(current_platform))
        # subprocess.call(BASH_PATH)
        # process = subprocess.Popen(BASH_PATH, start_new_session=True)
        process = subprocess.Popen(r"C:\Users\pcadmin\Documents\GitHub\FYP_Server_Zephyr\resources\windows_script.bat", start_new_session=True)
        # subprocess.call(r"C:\Users\pcadmin\Documents\GitHub\FYP_Server_Zephyr\resources\windows_script.bat")
    else:
        log.debug("Sorry, {} is not supported yet. Exiting now...".format(current_platform))
        return None

    log.debug("Current Process ID = {}".format(process.pid))
    # time.sleep(30)
    # complete_kill(process)
    return process


def complete_kill(process_id=None):
    for proc in psutil.process_iter():
        # check whether the process name matches
        if proc.name() == PROCNAME:
            log.debug("Found QEMU Instance")
            proc.kill()
            log.debug("Killed QEMU Instance")
        # kill any existing processes if any

    if (process_id != None):
        try:
            process = psutil.Process(process_id)
            log.debug("Killing Process {}".format(process_id))
            process.kill()
            log.debug("Process Killed successfully")
        except psutil.NoSuchProcess:
            log.error("Process {} was already closed".format(process_id))

    return
