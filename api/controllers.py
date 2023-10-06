from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.sql import func

import models


def get_total(db: Session):
    statement = select(func.count(models.RNA.id))
    total = db.execute(statement).all()
    return total


def get_stats(db: Session, sample_id: str):
    statement = (
        select(models.RNA.type, func.sum(models.RNA.read_counts))
        .filter(models.RNA.sample_id == sample_id)
        .group_by(models.RNA.type)
        .having(func.count("*") > 1)
    )
    count_per_type = db.execute(statement).all()
    statement = (
        select(models.RNA.type, func.count(models.RNA.license_plate.distinct()))
        .filter(models.RNA.sample_id == sample_id)
        .group_by(models.RNA.type)
        .having(func.count("*") > 1)
    )
    unique_count_per_type = db.execute(statement).all()
    total_types = len(count_per_type)
    return count_per_type, unique_count_per_type, total_types


def get_sample(db: Session, sample_id: str):
    statement = select(models.RNA).filter(models.RNA.sample_id == sample_id)
    rows = db.execute(statement).all()
    return rows
