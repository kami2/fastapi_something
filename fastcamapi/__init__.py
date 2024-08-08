from fastcamapi.config import Config
from fastcamapi.helpers.camera_helper import CameraHelper
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()
Config.initialize()
CameraHelper().run()
app.add_middleware(SessionMiddleware, secret_key="some-random-string")

from fastcamapi import routes
