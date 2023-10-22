#!/usr/bin/python3
""" this all class Place"""
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy import Float
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity
import models
from os import getenv



class PlaceAmenity(Base):
    """
    place amenities table definition
    """
    __tablename__ = "place_amenities"

    place_id = Column(String(80),
                      ForeignKey("places.id"),
                      primary_key=True,
                      nullable=False)
    amenity_id = Column(String(80),
                        ForeignKey("amenities.id"),
                        primary_key=True,
                        nullable=False)
    metadata = Base.metadata


class Place(BaseModel, Base):
    """Representation of Place
    Attributes:
    city_id: city id
    user_id: user id
    name: name input
    description: string of description
    number_rooms: number of room in int
    number_bathrooms: number of bathrooms in int
    max_guest: maximum guest in int
    price_by_night:: pice for a staying in int
    latitude: latitude in flaot
    longitude: longitude in float
    amenity_ids: list of Amenity ids
    """
    __tablename__ = "places"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        city_id = Column(String(60), ForeignKey("cities.id"))
        user_id = Column(String(60), ForeignKey("users.id"))
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False,
                              default=0)
        number_bathrooms = Column(Integer, nullable=False,
                                  default=0)
        max_guest = Column(Integer, nullable=False,
                           default=0)
        price_by_night = Column(Integer, nullable=False,
                                default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship("Review", backref="place",
                               cascade="delete")
        amenities = relationship("Amenity",
                                 secondary="place_amenities",
                                 viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0

        @property
        def reviews(self):
            """Returns respective list of reviews"""
            all_reviews = models.storage.all(Review)
            return list(filter((lambda c: c.place_id == self.id), all_reviews))

        @property
        def amenities(self):
            """Returns respective list of reviews"""
            amenities = models.storage.all(Amenity)
            return list(filter((lambda c: c.place_id == self.id), amenities))

        def __init__(self, *args, **kwargs):
            """initializes Review"""
            super().__init__(*args, **kwargs)
