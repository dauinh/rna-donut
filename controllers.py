from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.sql import func

import models


def get_total(db: Session):
    statement = select(models.RNA)
    rows = db.execute(statement).all()
    return len(rows)


def get_stats(db: Session):
    statement = (
        select(models.RNA.type, func.sum(models.RNA.read_counts))
        .group_by(models.RNA.type)
        .having(func.count("*") > 1)
    )
    rows = db.execute(statement).all()
    return rows


def get_sample(db: Session, sample_id: str):
    statement = select(models.RNA).filter(models.RNA.sample_id == sample_id)
    rows = db.execute(statement).all()
    return rows
