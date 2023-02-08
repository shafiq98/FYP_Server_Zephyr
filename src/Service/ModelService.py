import requests
import logging
# from src.utilities.Constants import TENSOR_SERVER_ROUTE
#
# from settings import INCOMING_C_PATH, OUTGOING_C_PATH

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(funcName)20s() - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
    handlers=[logging.StreamHandler()]
)
log = logging.getLogger(__name__)

# def retrieve_model():
#     response = requests.get(TENSOR_SERVER_ROUTE+"/model")
#     with open(INCOMING_C_PATH, 'wb+') as f:
#         f.write(response.content)
#         f.close()
#     return
#
# def replace_model():
#     with open(INCOMING_C_PATH, 'r') as f_read, open(OUTGOING_C_PATH, 'w') as f_write:
#         incoming_data = []
#         for line in f_read.read():
#             incoming_data.append(line)
#
#         f_read.close()
#         f_write.writelines(incoming_data)
#         f_write.close()


def store_model_locally(destination: str, file):
    file.save(destination)

def update_zephyr_model(source: str, destination: str):
    with open(source, 'r') as f_read, open(destination, 'w') as f_write:
        incoming_data = []
        for line in f_read.read():
            incoming_data.append(line)

        f_read.close()
        f_write.writelines(incoming_data)
        f_write.close()
