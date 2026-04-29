from sqlalchemy import Column, Integer, String
from database.db import Base


class Challenge(Base):
    __tablename__ = "challenges"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    points = Column(Integer, nullable=False)
    progress = Column(Integer, nullable=False, default=0)
    target = Column(Integer, nullable=False)
    frequency = Column(String, nullable=False)
    due_date = Column(String, nullable=False)
    assigned_to = Column(String, nullable=False)
    status = Column(String, nullable=False, default="In Progress")