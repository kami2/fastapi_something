from fastapi_something.config import Config
import logging
import requests


class NodeBBHelper:

    def __init__(self):
        self._secret = Config.PACIAK_NODEBB

    def get_data(self, url: str = None):
        pass

    def get_categories(self):
        headers = {"Authorization": f"Bearer {Config.PACIAK_NODEBB}"}
        url = "https://paciak.pl/api/category/7/motowy"
        results = requests.get(url, headers=headers)
        data = None
        if results.status_code == 200:
            data = results.json()
        else:
            logging.info("Failed")
        return data


if __name__ == "__main__":
    Config.initialize()
