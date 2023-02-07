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
    # kill any QEMU Instance running before starting a new zephyr one
    complete_kill(process)

    if (current_platform == WINDOWS):
        # this function will start a zephyr instance, but not kill it
        log.debug("Running on {} OS".format(current_platform))
        # subprocess.call(BASH_PATH)
        process = subprocess.Popen(BASH_PATH, start_new_session=True)
        # subprocess.call(r"C:\Users\pcadmin\Documents\GitHub\FYP_Server_Zephyr\resources\windows_script.bat")
    else:
        log.debug("Sorry, {} is not supported yet. Exiting now...".format(current_platform))
        return None

    log.debug("Current Process ID = {}".format(process.pid))
    time.sleep(30)
    complete_kill(process)
    return process


def list_process(processID: subprocess.DETACHED_PROCESS = None):
    dict_pids = {
        p.info["pid"]: p.info["name"]
        for p in psutil.process_iter(attrs=["pid", "name"])
    }
    if (processID in dict_pids.keys()):
        log.debug("Found Process ID".format(processID))
    else:
        log.debug("Not Found")
    log.debug(json.dumps(dict_pids, indent=4))
    process = psutil.Process(processID)
    process.kill()


def complete_kill(process: subprocess.Popen[str] = None):
    for proc in psutil.process_iter():
        # check whether the process name matches
        if proc.name() == PROCNAME:
            log.debug("Found QEMU Instance")
            proc.kill()
            log.debug("Killed QEMU Instance")
        # kill any existing processes if any

    if (process != None):
        log.debug("Killing Process {}".format(process.pid))
        process.kill()
        log.debug("Process Killed successfully")
        time.sleep(10)
    return
