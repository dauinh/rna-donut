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


@app.get("/length")
def len(db: Session = Depends(get_db)):
    length = controllers.get_length(db)
    if length is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return length


@app.get("/samples/{sample_id}")
async def get_sample(sample_id: str, db: Session = Depends(get_db)):
    controllers.get_sample(db, sample_id=sample_id)
    # if sample is None:
    #     raise HTTPException(status_code=404, detail="Sample not found")
    return sample_id
