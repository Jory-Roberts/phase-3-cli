from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref
from .base import Base


class Venue(Base):
    __tablename__ = "venue"
    id = Column(Integer, primary_key=True)
    venue_name = Column(String)
    venue_email = Column(String, unique=True)
    venue_city = Column(String)
    venue_state = Column(String)
    venue_zip_code = Column(String)
    capacity = Column(Integer)

    bookings = relationship("Booking", backref="venue")

    def __repr__(self):
        return (
            f"\n<Venue "
            + f"\n id={self.id}, "
            + f"\n venue_name={self.venue_name}, "
            + f"\n venue_email={self.venue_email}, "
            + f"\n venue_city={self.venue_city}, "
            + f"\n venue_state={self.venue_state}, "
            + f"\n venue_zip_code={self.venue_zip_code}, "
            + f"\n capacity={self.capacity} "
            + f"\n>"
        )

    def update_venue_capacity():
        ## query venue by capacity
        ## allow update of venue capacity
        pass

    def create_new_venue():
        ##filter by venue name
        ## if venue name is available create new venue
        pass

    def delete_venue():
        ## filter by venue name
        ## if venue available, remove venue
        pass
