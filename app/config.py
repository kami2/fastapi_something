import logging


def initialize():
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', encoding='utf-8', level=logging.DEBUG)


if __name__ == "__main__":
    initialize()
    logging.debug('Debug should be visible')
    logging.info('Info should be visible')
    logging.warning('Warning should be visible')
    logging.error('Error should be visible')

