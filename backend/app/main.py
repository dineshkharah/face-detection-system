from fastapi import FastAPI

from app.models import ROI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Backend is running 🚀"}
