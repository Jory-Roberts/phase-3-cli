#!/usr/bin/env python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Artist, Venue, Booking

if __name__ == "__main__":
    engine = create_engine("sqlite:///db/artist_venue.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    import ipdb

    ipdb.set_trace()
