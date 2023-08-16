from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship, backref
from .base import Base
from .session import Session


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

    bookings = relationship("Booking", backref="artist")

    def __repr__(self):
        return (
            f"\n<Artist "
            + f"\n id={self.id}, "
            + f"\n artist_name={self.artist_name}, "
            + f"\n email={self.email}, "
            + f"\n phone_number={self.phone_number}, "
            + f"\n address={self.address}, "
            + f"\n city={self.city}, "
            + f"\n state={self.state}, "
            + f"\n zip_code={self.zip_code}, "
            + f"\n genre={self.genre}, "
            + f"\n availability={self.availability} "
            + f"\n>"
        )
