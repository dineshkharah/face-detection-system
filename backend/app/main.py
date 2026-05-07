from fastapi import FastAPI, WebSocket

from app.websocket import websocket_endpoint
from app.database import Base, engine
from app.routes import router

app = FastAPI()

Base.metadata.create_all(bind=engine)
app.include_router(router)


@app.get("/")
def root():
    return {"message": "Backend is running 🚀"}


@app.websocket("/ws/video")
async def websocket_route(websocket: WebSocket):
    await websocket_endpoint(websocket)
