from sqlalchemy import Column, Integer, String, DateTime, Uuid

from .database import Base


class PricePaid(Base):
    __tablename__ = "price_paid_transactions"

    transaction_id = Column(Uuid, primary_key=True)
    price = Column(Integer)
    transfer_date = Column(DateTime, index=True)
    postcode = Column(String(length=10), index=True)
    property_type = Column(String(length=1))
    age_indicator = Column(String(length=1))
    duration = Column(String(length=1))
    paon = Column(String(length=50))
    saon = Column(String(length=50), nullable=True)
    street = Column(String(length=50))
    locality = Column(String(length=50))
    city = Column(String(length=50))
    district = Column(String(length=50))
    county = Column(String(length=50))
    ppd_type = Column(String(length=1))
    record_status = Column(String(length=1))

