import csv
import requests
import typer

from .models import PricePaid
from .database import engine, SessionLocal, create_db_and_tables, Base

DATA_URL = 'http://prod.publicdata.landregistry.gov.uk.s3-website-eu-west-1.amazonaws.com/pp-complete.csv'

cli = typer.Typer(name="house_pricing")


def _instantiate_model(row: list) -> PricePaid:
    names = [
        'transaction_id', 'price', 'transfer_date', 'postcode', 'property_type', 'age_indicator', 'duration',
        'paon', 'saon', 'street', 'locality', 'city', 'district', 'county', 'ppd_type', 'record_status']
    attributes = dict(zip(names, row))
    price_paid = PricePaid(**attributes)
    return price_paid


def _load_data(no_lines: int = 100):
    request = requests.get(DATA_URL, stream=True)
    with SessionLocal() as db:
        for i, row in enumerate(csv.reader(request.iter_lines(decode_unicode=True))):
            if i == no_lines:
                break
            price_paid = _instantiate_model(row)

            db.add(price_paid)
        db.commit()


@cli.command()
def init_db():
    """Initiate database and fills with data from csv.

    If already created, the table `price_paid_transactions` is dropped.

    """
    Base.metadata.drop_all(bind=engine)
    create_db_and_tables(engine)
    _load_data()


@cli.command(hidden=True)
def secret():
    raise NotImplementedError()


if __name__ == '__main__':
    cli()
