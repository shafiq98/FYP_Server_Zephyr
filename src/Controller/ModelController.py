import logging
import sys

# External Imports
from werkzeug.datastructures import FileStorage
from flask import session

# Service Imports
from src.Service import ZephyrService as ZS
from src.Service import ModelService as MS

# Utilities Import
from settings import *
from src.utilities.Constants import *

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(funcName)20s() - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
    handlers=[logging.StreamHandler()]
)
log = logging.getLogger(__name__)

current_platform = sys.platform
if (current_platform == WINDOWS):
    OUTGOING_C_PATH = OUTGOING_C_PATH_WINDOWS
else:
    OUTGOING_C_PATH = OUTGOING_C_PATH_LINUX


def retrieve_model_controller(file: FileStorage):
    if file:
        MS.store_model_locally(UPLOAD_FOLDER, file)
        MS.update_zephyr_model(UPLOAD_FOLDER, OUTGOING_C_PATH)
    return
