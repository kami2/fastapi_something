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

    def send_file(self, channel_id: str, file_path: str, text: str = None):
        try:
            self.client.files_upload_v2(channel=channel_id, file=file_path, initial_comment=text)
        except SlackApiError as e:
            logging.info(f"ERROR: {e}")


if __name__ == "__main__":
    paciak_slack = SlackHelper()
    # paciak_slack.send_message(channel="#testowanko_na_produkcji", text="Debug")
    paciak_slack.send_file(channel_id="C01L22NNZPY", file_path="./cache/norzxr.jpg", text="Do i need to provide channel id rather than channel name? Why this shit is fine for send message but not for file upload? Norbert cisnie")
