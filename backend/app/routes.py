from fastapi import APIRouter

from app.database import SessionLocal
from app.models import ROI

router = APIRouter()


@router.get("/roi")
def get_roi_data():
    db = SessionLocal()

    roi_data = db.query(ROI).all()

    return roi_data
