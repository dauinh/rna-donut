from pydantic import BaseModel


class RNA(BaseModel):
    id: str
    sample_id: str
    license_plate: str
    type: str
    read_counts: int
