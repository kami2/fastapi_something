from fastapi import FastAPI
import uvicorn
import logging
from app import config

app = FastAPI()
config.initialize()


@app.get("/")
async def root():
    logging.info("Accessed main route")
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
