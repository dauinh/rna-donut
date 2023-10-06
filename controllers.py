from sqlalchemy.orm import Session
from sqlalchemy import select

import models


def get_length(db: Session):
    statement = select(models.RNA)
    rows = db.execute(statement).all()
    return len(rows)


import matplotlib.pyplot as plt


def get_sample(db: Session, sample_id: str):
    statement = (
        select(models.RNA.type)
        .filter(models.RNA.sample_id == sample_id)
    )
    types = db.execute(statement).all()
    statement = (
        select(models.RNA.read_counts)
        .filter(models.RNA.sample_id == sample_id)
    )
    counts = db.execute(statement).all()
    x = [r[0] for r in counts]
    labels = [r[0] for r in types]
    plt.pie(x, labels=labels)
    plt.show()