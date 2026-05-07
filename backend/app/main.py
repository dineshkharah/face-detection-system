from fastapi import FastAPI, WebSocket

from app.models import ROI
from app.websocket import websocket_endpoint

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Backend is running 🚀"}


@app.websocket("/ws/video")
async def websocket_route(websocket: WebSocket):
    await websocket_endpoint(websocket)
