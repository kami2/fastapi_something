from fastapi_something.config import Config
import logging
import requests


class NodeBBHelper:

    def __init__(self):
        self._secret = Config.PACIAK_FORUM_SECRET
        self.base_url = Config.PACIAK_FORUM_URL

        if not self._secret:
            logging.warning("Secret not provided")

    def get_headers(self):
        return {"Authorization": f"Bearer {self._secret}"}

    def get_data(self, url: str, entity: str = None):
        params = {"page": 1}

        data = []
        while True:
            response = requests.get(self.base_url+url, headers=self.get_headers(), params=params)
            if response.status_code != 200:
                logging.warning(f"Failed response {response.status_code}")
                break
            json_response = response.json()
            if entity not in json_response:
                # Let's say if entity not in response then return as single object, maybe I will need this later
                return json_response
            data.extend(json_response[entity])

            if json_response["pagination"]["currentPage"] != json_response["pagination"]["pageCount"]:
                logging.info(f'Collected {json_response["pagination"]["currentPage"]}/{json_response["pagination"]["pageCount"]} pages')
                params["page"] += 1
            else:
                logging.info(f'All pages collected {json_response["pagination"]["pageCount"]}')
                break
        return data

    def get_categories(self):
        return self.get_data("categories", "categories")

    def get_category_topics(self, category_id):
        return self.get_data(f"category/{category_id}", "topics")


if __name__ == "__main__":
    forum = NodeBBHelper()
    logging.info(len(forum.get_category_topics(category_id=7)))
