import logging
from fastapi_something.config import Config
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


class SlackHelper:

    def __init__(self):
        self.client = WebClient(token=Config.PACIAK_SLACK_TOKEN)

    def send_message(self, channel: str, text: str):
        try:
            logging.info(f"Sending [{text}] to channel [{channel}]")
            self.client.chat_postMessage(channel=channel, text=text)
        except SlackApiError as e:
            logging.info(f"ERROR: {e}")


if __name__ == "__main__":
    paciak_slack = SlackHelper()
    paciak_slack.send_message(channel="#testowanko_na_produkcji", text="Send from API")
