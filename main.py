from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import controllers, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/total")
def len(db: Session = Depends(get_db)):
    total = controllers.get_total(db)
    if total is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return total


@app.get("/stats")
def calc_stats(db: Session = Depends(get_db)):
    stats = controllers.get_stats(db)
    if stats is None:
        raise HTTPException(
            status_code=404, detail="Error occurred while calculating stats"
        )
    stats_dict = [{"type": row[0], "total_read_counts": row[1]} for row in stats]

    return stats_dict


@app.get("/samples/{sample_id}")
async def get_sample(sample_id: str, db: Session = Depends(get_db)):
    sample = controllers.get_sample(db, sample_id=sample_id)
    if sample is None:
        raise HTTPException(status_code=404, detail="Sample not found")
    res = [r[0] for r in sample]
    return res
