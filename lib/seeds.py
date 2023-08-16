#!/usr/bin/env python
from models import Artist, Venue, Booking
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from datetime import datetime, timedelta

engine = create_engine("sqlite:///db/artist_venue.db")
Session = sessionmaker(bind=engine)
session = Session()

import random
from faker import Faker

fake = Faker()

print("🎸 Seeding DB..")

start_date = datetime.today()
end_date = start_date + timedelta(days=365)

venue_names = [
    "Red Rocks",
    "First Avenue",
    "The Thirsty Duck",
    "Ryman Auditorium",
    "The Bluebird Cafe",
    "Brew Works",
    "The Basement",
    "The Emerald Theater",
    "Pabst Theater",
    "Turner Hall Ballroom",
    "Hollywood Bowl",
    "Radio City Music Hall",
    "Oasis Events Center",
    "Aurora Pavillion",
    "Starlight Pavillion",
    "Serenity Garden",
    "Velvet Lounge",
    "Rudy's",
    "Opry House",
    "Harmony Hall",
]

genres = [
    "Alternative",
    "Blues",
    "Country",
    "Classical",
    "Dance",
    "Electronic",
    "Folk",
    "Funk",
    "Indie",
    "Latin",
    "Metal",
    "Pop",
    "Rock",
    "Rap",
    "Soul",
    "Jazz",
    "R&B",
    "Reggae",
    "Hip Hop",
    "Punk",
]

artist_names = [
    "Electric Echoes",
    "Midnight Madness",
    "Haze",
    "Quantum Dream",
    "Infinite Groove",
    "Solar Flare",
    "Stellar Serenity",
    "Dreamwave Ensembale",
    "Celestial Fusion",
    "Lunar Groove",
    "Radiant Pulse",
    "Sonic Mirage",
    "Eclipsed",
    "Cosmic Echo",
    "Crystal Harmonies",
    "Brad Earl Experience",
    "Whiskey Crutch",
    "Crimson Drop",
    "City Orchestra",
    "Aurora Harmony",
]


def delete_records():
    session.query(Artist).delete()
    session.query(Venue).delete()
    session.query(Booking).delete()
    session.commit()


def create_venues():
    venues = []
    for venue_name in venue_names:
        venue = Venue(
            venue_name=venue_name,
            venue_email=f"{venue_name.replace(' ' , ' ').lower()}@gmail.com",
            venue_address=fake.street_address(),
            venue_city=fake.city(),
            venue_state=fake.state(),
            venue_zip_code=fake.postcode(),
            capacity=fake.random_int(min=50, max=1000),
        )

        session.add(venue)
        session.commit()
        venues.append(venue)
    return venues


def create_artists():
    artists = []
    for artist_name in artist_names:
        artist = Artist(
            artist_name=artist_name,
            email=f"{artist_name.replace(' ' , ' ').lower()}@gmail.com",
            phone_number=fake.phone_number(),
            address=fake.street_address(),
            city=fake.city(),
            state=fake.state(),
            zip_code=fake.postcode(),
            genre=random.choice(genres),
            availability=fake.date_between_dates(
                date_start=start_date, date_end=end_date
            ),
        )

        session.add(artist)
        session.commit()
        artists.append(artist)
    return artists


def create_bookings(artists, venues):
    bookings = []
    for _ in range(50):
        artist = random.choice(artists)
        venue = random.choice(venues)
        booking_date = fake.date_between_dates(date_start=start_date, date_end=end_date)
        status = fake.boolean(chance_of_getting_true=50)
        booking = Booking(
            artist_id=artist.id,
            venue_id=venue.id,
            booking_date=booking_date,
            status=status,
        )

        session.add(booking)
        session.commit()
        bookings.append(booking)
    return bookings


def relate_one_to_many(artists, venues, bookings):
    for booking in bookings:
        booking.artist = random.choice(artists)
        booking.venue = random.choice(venues)

    session.add_all(bookings)
    session.commit()
    return artists, venues, bookings


if __name__ == "__main__":
    delete_records()
    artists = create_artists()
    venues = create_venues()
    bookings = create_bookings()
    artists, venues, bookings = relate_one_to_many(artists, venues, bookings)


print("Success! 🤘")
