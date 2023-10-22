#!/usr/bin/python
""" holds class Amenity"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Numeric, String, ForeignKey
from sqlalchemy.orm import relationship
import models
from os import getenv


class Amenity(BaseModel, Base):
    """Representation of Amenity
    Attributes:
    name: input name
    """
    __tablename__ = "amenities"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        place_amenities = relationship(
                            "Place",
                            secondary="place_amenities",
                            back_populates="amenities"
                            )
# The `else` block in the code is defining
# a separate `Amenity` class when the value of the
# environment variable `HBNB_TYPE_STORAGE`
# is not equal to "db".
    else:
        """Representation of Amenity
        Attributes:
        name: input name
        """
        name = ""
