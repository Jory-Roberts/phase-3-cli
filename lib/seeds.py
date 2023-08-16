from models import Artist, Venue
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("sqlite:///db/artist_venue.db")
Session = sessionmaker(bind=engine)
session = Session()

import random
from faker import Faker

fake = Faker()


def delete_records(self):
    session.query(Artist).delete()
    session.query(Venue).delete()
    session.commit()
