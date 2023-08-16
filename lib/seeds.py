from models import Artist, Venue
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("sqlite:///db/artist_venue.db")
Session = sessionmaker(bind=engine)
session = Session()

import random
from faker import Faker

fake = Faker()

print("🎸 Seeding DB..")

venue_names = [
    "Red Rocks Park and Amphitheatre",
    "First Avenue",
    "The Thirsty Duck",
    "Ryman Auditorium",
    "The Bluebird Cafe",
    "Brew Works",
    "The Basement",
    "The Emerald Theater",
    "Pabst Theater",
    "Turner Hall Ballroom",
]


def delete_records():
    session.query(Artist).delete()
    session.query(Venue).delete()
    session.commit()


def create_venues():
    venues = []
    for i in range(10):
        venue = Venue(
            venue_name = venue_names,
            venue_email = fake.email(),
            venue_address = fake.street_address(),
            venue_city = fake.city(),
            venue_state = fake.state(),
            venue_zip_code = fake.postcode(),
            capacity = fake.random_int(min=50, max=1000)
        )

        session.add(venue)
        session.commit()
        venues.append(venue)
    return venues




print("Success! 🤘")
