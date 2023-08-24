from sqlalchemy import Column, String, Float, Integer, ForeignKey, Date
from sqlalchemy.orm import backref, relationship
from .base import Base


class Booking(Base):
    __tablename__ = "booking"
    id = Column(Integer, primary_key=True)
    artist_id = Column(Integer, ForeignKey("artist.id"))
    venue_id = Column(Integer, ForeignKey("venue.id"))
    booking_date = Column(Date)
    ticket_price = Column(Float)
    status = Column(String)

    artist = relationship("Artist", back_populates="bookings")
    venue = relationship("Venue", back_populates="bookings")

    def __repr__(self):
        return (
            f"\n<Booking "
            + f"\n id = {self.id}, "
            + f"\n artist_id = {self.artist_id}, "
            + f"\n artist_name = {self.artist.artist_name}, "
            + f"\n venue_id = {self.venue_id}, "
            + f"\n venue_name = {self.venue.venue_name}, "
            + f"\n booking_date = {self.booking_date}, "
            + f"\n ticket_price = {self.ticket_price}, "
            + f"\n status = {self.status}"
            + f"\n>"
        )
