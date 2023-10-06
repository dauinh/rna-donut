from sqlalchemy import Column, Integer, String
import uuid

from database import Base

class RNA(Base):
    __tablename__ = 'rna'

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    sample_id = Column(String)
    license_plate = Column(String)
    type = Column(String)
    read_counts = Column(Integer)
