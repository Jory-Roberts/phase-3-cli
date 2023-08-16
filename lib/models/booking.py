from sqlalchemy import Column, Boolean, Integer, ForeignKey, Date
from sqlalchemy.orm import backref, relationship
from .base import Base


class Booking(Base):
    __tablename__ = "booking"
    id = Column(Integer, primary_key=True)
    artist_id = Column(Integer, ForeignKey("artist.id"))
    venue_id = Column(Integer, ForeignKey("venue.id"))
    booking_date = Column(Date)
    status = Column(Boolean)

    artist = relationship("Artist", backref="bookings")
    venue = relationship("Venue", backref="bookings")
