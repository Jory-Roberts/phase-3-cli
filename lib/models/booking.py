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

    def __repr__(self):
        return (
            f"\n<Booking "
            + f"\n id = {self.id}, "
            + f"\n artist_id = {self.artist_id}, "
            + f"\n venue_id = {self.venue_id}, "
            + f"\n booking_date = {self.booking_date}, "
            + f"\n status = {self.status}"
        )

    def create_booking():
        ##query by status and booking date
        ## if booking status false, allow for booking
        ## otherwise, return message booking not created
        pass

    def cancel_booking():
        ##query by booking_date
        ## remove booking, return message that confirmed
        pass

    def confirmed_booking():
        ##if true:
        ## return message that venue is booked
        ## otherwise, return message that venue is available
        pass
