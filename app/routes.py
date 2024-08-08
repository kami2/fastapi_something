from app import app
from starlette.responses import StreamingResponse
from helpers.camera_helper import CameraHelper
import logging


@app.get("/")
async def root():
    logging.info("Accessed main route")
    return {"message": "Hello World"}


@app.get("/video_feed")
async def video_feed():
    return StreamingResponse(CameraHelper().generate_frames(), media_type='multipart/x-mixed-replace; boundary=frame')

