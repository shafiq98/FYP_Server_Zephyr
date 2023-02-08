import logging

# Web Server Imports
from flask import Flask, request, session, flash, Response
from werkzeug.utils import secure_filename

# utilities import
from settings import UPLOAD_FOLDER, OUTGOING_C_PATH
from src.Service import ModelService as ms
# Service imports
from src.Service import ZephyrService as zs
from src.utilities.Constants import *

app = Flask(__name__)
app.secret_key = "zephyrkeysupersecret"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(funcName)20s() - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
    handlers=[logging.StreamHandler()]
)
log = logging.getLogger(__name__)

zs.complete_kill()
zs.start_zephyr_instance()

def restart_zephyr_instance():
    zs.complete_kill(session.get('process'))
    session['process'] = zs.start_zephyr_instance().pid

@app.route("/retrieve_model", methods=[POST])
def retrieve_model_route():

    zs.complete_kill(session.get('process'))

    log.debug("Request Files: {}".format(request.files))
    log.debug("Model: {}".format(request.files.get("model")))

    if 'model' not in request.files:
        flash('No file part')
        return Response("{'message: 'Please name your file as model and try again'}", status=400,
                        mimetype='application/json')
    file = request.files['model']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        flash('No selected file')
        return Response("{'message: 'No file transmitted'}", status=404, mimetype='application/json')
    if file:
        filename = secure_filename(file.filename)
        ms.store_model_locally(UPLOAD_FOLDER, file)
        ms.update_zephyr_model(UPLOAD_FOLDER, OUTGOING_C_PATH)

        restart_zephyr_instance()

    return Response("{'message: 'File saved successfully'}", status=200, mimetype='application/json')


if (__name__ == "__main__"):
    app.run(host='0.0.0.0', port=8081, debug=True)
