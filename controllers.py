from sqlalchemy.orm import Session
from sqlalchemy import select

import models

def get_all(db: Session):
    statement = select(models.RNA)
    rows = db.execute(statement).all()
    return len(rows)

def get_sample(db: Session, sample_id: int):
    return db.query(models.RNA).filter(models.RNA.sample_id == sample_id).first()
