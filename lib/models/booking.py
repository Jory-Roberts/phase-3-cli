from sqlalchemy import Column, String, Integer, ForeignKey, Table
from .base import Base

booking = Table(
    "booking",
    Base.metadata,
    Column("artist_id", ForeignKey("artist.id")),
    Column("venue_id", ForeignKey("venue.id")),
)
