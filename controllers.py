from sqlalchemy.orm import Session
from sqlalchemy import select

import models

def get_length(db: Session):
    statement = select(models.RNA)
    rows = db.execute(statement).all()
    return len(rows)


def get_sample(db: Session, sample_id: str):
    statement = select(models.RNA).filter(models.RNA.sample_id == sample_id)
    rows = db.execute(statement).all()
    return [r[0] for r in rows]
