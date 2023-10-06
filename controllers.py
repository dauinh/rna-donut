from sqlalchemy.orm import Session

import models


def get_sample(db: Session, sample_id: int):
    return db.query(models.RNA).filter(models.RNA.sample_id == sample_id).first()
