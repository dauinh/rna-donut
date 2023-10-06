from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import controllers, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/total")
def len(db: Session = Depends(get_db)):
    total = controllers.get_total(db)[0][0]
    if total is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return total


@app.get("/stats/{sample_id}")
def calc_stats(sample_id: str, db: Session = Depends(get_db)):
    count_per_type, unique_count_per_type = controllers.get_stats(db, sample_id=sample_id)
    if not (count_per_type or unique_count_per_type):
        raise HTTPException(
            status_code=404, detail="Sample not found"
        )
    res = {
        "labels": [row[0] for row in count_per_type],
        "count_per_type": [row[1] for row in count_per_type],
        "unique_count_per_type": [row[1] for row in unique_count_per_type]
    }

    return res


@app.get("/samples/{sample_id}")
async def get_sample(sample_id: str, db: Session = Depends(get_db)):
    sample = controllers.get_sample(db, sample_id=sample_id)
    if sample is None:
        raise HTTPException(status_code=404, detail="Sample not found")
    res = [row[0] for row in sample]

    return res
