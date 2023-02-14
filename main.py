import logging
import time

import psutil
# Web Server Imports
from flask import Flask, request, session, flash, Response
from werkzeug.utils import secure_filename

# utilities import
from settings import UPLOAD_FOLDER
# Service imports
from src.Service import ZephyrService as ZS
from src.utilities.Constants import *
# Controller imports
from src.Controller import ModelController as MC

app = Flask(__name__)
app.secret_key = "zephyrkeysupersecret"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(funcName)20s() - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
    handlers=[logging.StreamHandler()]
)
log = logging.getLogger(__name__)

# NOTE: start_zephyr_instance() will kill existing QEMU instances
existingProcess = ZS.start_zephyr_instance()

def restart_zephyr_instance():
    ZS.complete_kill(session.get('process'))
    session['process'] = ZS.start_zephyr_instance().pid

@app.route("/retrieve_model", methods=[POST])
def retrieve_model_route():
    session['process'] = ZS.start_zephyr_instance().pid
    if 'model' not in request.files:
        flash('No file part')
        return Response("{'message: 'Please name your file as model and try again'}", status=400,
                        mimetype='application/json')

    log.debug("Request Files: {}".format(request.files))
    log.debug("Model: {}".format(request.files.get("model")))

    file = request.files['model']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        flash('No selected file')
        return Response("{'message: 'No file transmitted'}", status=404, mimetype='application/json')
    else:
        MC.retrieve_model_controller(file)
        ZS.start_zephyr_instance(session.get('process'))
    return Response("{'message: 'File saved successfully'}", status=200, mimetype='application/json')


if (__name__ == "__main__"):
    app.run(host='0.0.0.0', port=8081, debug=True)
