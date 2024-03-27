#!/usr/bin/python3
""" This module defines the class PLace """
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import os
import models
from models.review import Review


association_table = Table("place_amenity", Base.metadata,
                          Column("place_id", String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True, nullable=False),
                          Column("amenity_id", String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """Represents a Place for a MySQL database.

    Public class attributes (with sqlalchemy):

        __tablename__ (str): Name of MySQL table to store places.

        city_id (Columns: Str): Foreign key to 'cities.id'.
        user_id (Columns: Str): Foreign key to 'user.id'.
        name (Columns: Str): Name of the place.
        description (Columns: Str): Description of the place.

        number_rooms (Columns: Integer): Number of room. Default 0.
        number_bathrooms (Columns: Integer): Number of bathrooms. Default 0.
        max_guest (Columns: Integer): Max guest. Default 0.
        price_by_night (Columns: Integer): Price by night. Default 0.

        latitude (Columns: Float): The place's latitude.
        longitude (Columns: Float): The place's longitude.

        amenity_ids (Columns: list): An id list of all linked amenities.

        reviews (Relationship Place --> Review): Links place with reviews.
    """
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []

    reviews = relationship("Review", backref="place", cascade="delete")
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False)

    if os.getenv("HBNB_TYPE_STORAGE", None) != "db":

        @property
        def reviews(self):
            """Return a list of all linked Reviews."""
            review_list = []
            for review in list(models.storage.all(Review).values()):
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """Get/set linked Amenities."""
            amenity_list = []
            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, value):
            if type(value) is Amenity:
                self.amenity_ids.append(value.id)
