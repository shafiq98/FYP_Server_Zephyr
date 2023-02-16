import logging

from werkzeug.datastructures import FileStorage

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(funcName)20s() - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
    handlers=[logging.StreamHandler()]
)
log = logging.getLogger(__name__)


def store_model_locally(destination: str, file: FileStorage):
    file.save(destination)
    file.close()


def update_zephyr_model(source: str, destination: str):
    with open(source, 'r') as f_read, open(destination, 'w') as f_write:
        incoming_data = []
        for line in f_read.read():
            incoming_data.append(line)

        f_read.close()
        f_write.writelines(incoming_data)
        f_write.close()
