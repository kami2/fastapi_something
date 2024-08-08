import logging
from dotenv import load_dotenv
import os


class Config:

    load_dotenv()

    CAMERA_HOST_IP = "192.168.42.1"
    CAMERA_HOST_PORT = 7878
    CAMERA_RTSP_ADDRESS = "rtsp://192.168.42.1/live"
    TEST_VAR = os.environ.get("TEST_VAR")

    @staticmethod
    def initialize():
        try:
            logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', encoding='utf-8', level=logging.DEBUG)
            logging.info("CONFIG INITIALIZED")
        except Exception as e:
            raise f"Failed to initialize config [{e}]"


if __name__ == "__main__":
    Config.initialize()
    logging.debug('Debug should be visible')
    logging.info('Info should be visible')
    logging.warning('Warning should be visible')
    logging.error('Error should be visible')
