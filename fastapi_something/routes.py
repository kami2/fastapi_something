import logging
from fastapi_something import app
from fastapi_something import oauth
from fastapi_something.helpers.camera_helper import CameraHelper
from starlette.responses import StreamingResponse
from starlette.requests import Request
from starlette.responses import HTMLResponse, RedirectResponse
from authlib.integrations.starlette_client import OAuthError


@app.get("/")
async def root():
    logging.info("Accessed main route")
    return {"message": "Hello World"}


@app.get("/video_feed")
async def video_feed():
    return StreamingResponse(CameraHelper().generate_frames(), media_type='multipart/x-mixed-replace; boundary=frame')


@app.get('/login')
async def login(request: Request):
    redirect_uri = request.url_for('auth')
    return await oauth.google.authorize_redirect(request, redirect_uri)


@app.get('/auth')
async def auth(request: Request):
    try:
        token = await oauth.google.authorize_access_token(request)
    except OAuthError as error:
        return HTMLResponse(f'<h1>{error.error}</h1>')
    user = token.get('userinfo')
    if user:
        request.session['user'] = dict(user)
        logging.info(dict(token))
    return RedirectResponse(url='/')

