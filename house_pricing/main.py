from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy.orm import Session
from uuid import UUID

from .models import PricePaid
from .database import engine, SessionLocal, create_db_and_tables

app = FastAPI(
    title="Price paid transactions",

)


@app.on_event("startup")
def on_startup():
    create_db_and_tables(engine)


def get_db() -> Session:
    with SessionLocal() as db:
        yield db


@app.get("/")
async def read_ppd_transactions(db: Session = Depends(get_db)):
    return db.query(PricePaid).all()


@app.get("/transaction/{transaction_id}")
async def read_single_ppd_transaction(
        transaction_id: UUID, db: Session = Depends(get_db)
):
    transaction = (
        db.query(PricePaid)
        .filter(PricePaid.transaction_id == transaction_id)
        .first()
    )

    if transaction is not None:
        return transaction

    message = 'Invalid transaction ID'
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=message)
