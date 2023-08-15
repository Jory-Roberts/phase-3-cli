from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from .base import Base
from .session import Session
from .booking import booking


class Artist(Base):
    __tablename__ = "artist"
    id = Column(Integer, primary_key=True)
    artist_name = Column(String)
    email = Column(String, unique=True)
    phone_number = Column(String)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    zip_code = Column(String)
    genre = Column(String)
    availability = Column(Date)

    venues = relationship("Venue", secondary=booking)
