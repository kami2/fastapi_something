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

    GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET")

    MONGODB_URL = os.environ.get("MONGODB_URL")
    MONGODB_NAME = os.environ.get("MONGODB_NAME")
    MONGODB_COLLECTION = os.environ.get("MONGODB_COLLECTION")

    PACIAK_FORUM_URL = os.environ.get("PACIAK_FORUM_URL")
    PACIAK_FORUM_SECRET = os.environ.get("PACIAK_FORUM_SECRET")
    PACIAK_SLACK_APP = os.environ.get("PACIAK_SLACK_APP")
    PACIAK_SLACK_TOKEN = os.environ.get("PACIAK_SLACK_TOKEN")
    PACIAK_SLACK_CLIENT_ID = os.environ.get("PACIAK_SLACK_CLIENT_ID")
    PACIAK_SLACK_CLIENT_SECRET = os.environ.get("PACIAK_SLACK_CLIENT_SECRET")
    PACIAK_SLACK_SIGNING_SECRET = os.environ.get("PACIAK_SLACK_SIGNING_SECRET")

    SECRET_KEY = os.environ.get("SECRET_KEY")

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
            client_id=Config.GOOGLE_CLIENT_ID,
            client_secret=Config.GOOGLE_CLIENT_SECRET,
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
