import secrets
import logging
from config import Config


def generate_secret_key():
    generated_key = secrets.token_urlsafe(30)
    logging.info(f"GENERATED KEY : {generated_key}")
    return generated_key


if __name__ == "__main__":
    Config.initialize()
    generate_secret_key()
