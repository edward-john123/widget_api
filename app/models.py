from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from app.extensions import db


class Widget(db.Model):
    __tablename__ = "widgets"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), nullable=False)
    num_parts = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )

    def __repr__(self):
        return f"<Widget {self.name}>"
