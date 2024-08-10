import os
import logging

from dotenv import load_dotenv
from authlib.integrations.starlette_client import OAuth


class Config:

    load_dotenv()

    CAMERA_HOST_IP = "192.168.42.1"
    CAMERA_HOST_PORT = 7878
    CAMERA_RTSP_ADDRESS = "rtsp://192.168.42.1/live"
    TEST_VAR = os.environ.get("TEST_VAR")

    CLIENT_ID = os.environ.get("CLIENT_ID")
    CLIENT_SECRET = os.environ.get("CLIENT_SECRET")

    MONGODB_URL = os.environ.get("MONGODB_URL")
    MONGODB_NAME = os.environ.get("MONGODB_NAME")
    MONGODB_COLLECTION = os.environ.get("MONGODB_COLLECTION")

    @staticmethod
    def initialize():
        try:
            logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', encoding='utf-8', level=logging.DEBUG)
            logging.info("CONFIG INITIALIZED")
        except Exception as e:
            raise f"Failed to initialize config [{e}]"

    @staticmethod
    def oauth_google():
        oauth = OAuth()
        oauth.register(
            name='google',
            client_id=Config.CLIENT_ID,
            client_secret=Config.CLIENT_SECRET,
            server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
            client_kwargs={
                'scope': 'openid email profile'
            }
        )
        return oauth


if __name__ == "__main__":
    Config.initialize()
    logging.debug('Debug should be visible')
    logging.info('Info should be visible')
    logging.warning('Warning should be visible')
    logging.error('Error should be visible')
