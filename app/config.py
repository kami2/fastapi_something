import logging


class Config:

    CAMERA_HOST_IP = "192.168.42.1"
    CAMERA_HOST_PORT = 7878
    CAMERA_RTSP_ADDRESS = "rtsp://192.168.42.1/live"

    @staticmethod
    def initialize():
        try:
            logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', encoding='utf-8', level=logging.DEBUG)
        except Exception as e:
            raise f"Failed to initialize config [{e}]"


if __name__ == "__main__":
    Config.initialize()
    logging.debug('Debug should be visible')
    logging.info('Info should be visible')
    logging.warning('Warning should be visible')
    logging.error('Error should be visible')

