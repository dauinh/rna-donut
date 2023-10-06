from sqlalchemy import Column, Integer, String

from database import Base

class RNA(Base):
    __tablename__ = 'rna'

    id = Column(Integer, primary_key=True, index=True)
    sample_id = Column(Integer, unique=True)
    license_plate = Column(String)
    type = Column(String)
    read_counts = Column(Integer)
