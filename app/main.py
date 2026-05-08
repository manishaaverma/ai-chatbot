from fastapi import FastAPI, Request, WebSocket
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.websocket import websocket_endpoint

app = FastAPI()

# Static folder
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates folder
templates = Jinja2Templates(directory="app/templates")

@app.get("/")
async def get_chat_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

@app.websocket("/ws")
async def websocket_route(websocket: WebSocket):

    await websocket_endpoint(websocket)