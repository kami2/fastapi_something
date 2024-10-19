from fastapi_something.config import Config
# from helpers.camera_helper import CameraHelper
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()
Config.initialize()
# CameraHelper().run()
# noinspection PyTypeChecker
app.add_middleware(SessionMiddleware, secret_key=Config.SECRET_KEY)
oauth = Config.oauth_google()

import fastapi_something.routes
