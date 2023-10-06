from pydantic import BaseModel

class RNA(BaseModel):
    sample_id: str
    license_plate: str
    type: str
    read_counts: int