from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base
from .booking import booking


class Venue(Base):
    __tablename__ = "venue"
    id = Column(Integer, primary_key=True)
    venue_name = Column(String)
    venue_email = Column(String, unique=True)
    venue_address = Column(String)
    venue_city = Column(String)
    venue_state = Column(String)
    venue_zip_code = Column(String)
    capacity = Column(String)

    artists = relationship("Artist", secondary=booking)
