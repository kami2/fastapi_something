from fastapi import FastAPI, Response
import uvicorn
import logging
from app.config import Config
from helpers.camera_helper import CameraHelper
from starlette.responses import StreamingResponse

app = FastAPI()
Config.initialize()
CameraHelper().run()


@app.get("/")
async def root():
    logging.info("Accessed main route")
    return {"message": "Hello World"}


@app.get("/video_feed")
async def video_feed():
    return StreamingResponse(CameraHelper().generate_frames(), media_type='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
