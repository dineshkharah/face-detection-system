from sqlalchemy import Column, Integer, DateTime
from datetime import datetime

from app.database import Base


class ROI(Base):
    __tablename__ = "roi_data"

    id = Column(Integer, primary_key=True, index=True)

    x = Column(Integer)
    y = Column(Integer)

    width = Column(Integer)
    height = Column(Integer)

    timestamp = Column(DateTime, default=datetime.utcnow)
