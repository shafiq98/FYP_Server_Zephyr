import logging
import os
import subprocess
import sys

import psutil

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
        # log.debug("Sorry, {} is not supported yet. Exiting now...".format(current_platform))
        path = r"/home/shafiq/Documents/CodingProjects/Python/FYP_Server_Zephyr/resources/linux_script.sh"
        if os.path.isdir(path):
            raise Exception("{} is a directory. Please ensure that the script path is correct".format(path))

        process = subprocess.Popen(path, start_new_session=True)

    log.debug("Current Process ID = {}".format(process.pid))
    return process


def complete_kill(process_id=None):
    log.debug("Entering Complete Kill")
    log.debug("Searching for QEMU Instances")
    for proc in psutil.process_iter():
        # Kill any QEMU Processes
        if QEMU in proc.name():
            log.debug("Found QEMU Instance")
            proc.kill()
            log.debug("Killed QEMU Instance")

    if (process_id != None):
        log.debug("Trying to kill Process ID {}".format(process_id))
        try:
            process = psutil.Process(process_id)
            log.debug("Killing Process {}".format(process_id))
            process.kill()
            log.debug("Process Killed successfully")
        except psutil.NoSuchProcess:
            log.error("Process {} was already closed".format(process_id))
    log.debug("Completed service killing")
    return
