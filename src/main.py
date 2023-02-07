import logging

# Web Server Imports
import os

from flask import Flask, jsonify, request

from Service import ZephyrService as zs

# Base Configuration
app = Flask(__name__)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(funcName)20s() - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
    handlers=[logging.StreamHandler()]
)
log = logging.getLogger(__name__)

if (__name__ == "__main__"):
    # log.debug("Hello World")
    # print(os.getcwd())
    zs.start_zephyr_instance()