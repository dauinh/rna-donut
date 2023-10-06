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


@app.get("/")
def read_all(db: Session = Depends(get_db)):
    database = controllers.get_all(db)
    if database is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return database


@app.get("/sample/{sample_id}", response_model=list[schemas.RNA])
async def root(sample_id: int, db: Session = Depends(get_db)):
    sample = controllers.get_sample(db, sample_id=sample_id)
    if sample is None:
        raise HTTPException(status_code=404, detail="Sample not found")
    return sample
