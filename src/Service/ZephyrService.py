import subprocess
import os
import json
import sys
import logging
import psutil

from src.utilities.Constants import WINDOWS, PROCNAME

# Base Configuration
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(funcName)20s() - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
    handlers=[logging.StreamHandler()]
)
log = logging.getLogger(__name__)


def start_zephyr_instance():
    # this function will start a zephyr instance, but not kill it
    log.debug("Running on {} OS".format(sys.platform))

    platform = sys.platform
    if (platform == WINDOWS):
        path = "windows_script.bat"
        subprocess.Popen(path)
        # print("New PID: {}".format(proc.pid))
        list_process()
    else:
        log.debug("Sorry, {} is not supported yet".format(platform))
    return


def kill_zephyr_instance():
    # kill Qemu Instance directly, since Zephyr application cannot be exited
    # kernel simply idles
    for proc in psutil.process_iter():
        # check whether the process name matches
        if proc.name() == PROCNAME:
            print("Found QEMU Instance")
            proc.kill()
            print("Killed QEMU Instance")


def list_process(processID: subprocess.DETACHED_PROCESS = None):
    dict_pids = {
        p.info["pid"]: p.info["name"]
        for p in psutil.process_iter(attrs=["pid", "name"])
    }
    if (processID in dict_pids.keys()):
        log.debug("Found Process ID".format(processID))
    else:
        log.debug("Not Found")
    print(json.dumps(dict_pids, indent=4))
    process = psutil.Process(processID)
    process.kill()

def kill_QEMU():
    for proc in psutil.process_iter():
        # check whether the process name matches
        if proc.name() == PROCNAME:
            print("Found QEMU Instance")
            proc.kill()
            print("Killed QEMU Instance")