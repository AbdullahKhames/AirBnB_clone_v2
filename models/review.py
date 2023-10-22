#!/usr/bin/python
""" holds class Review"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
import models
from os import getenv


class Review(BaseModel, Base):
    """Representation of Review
    Attributes:
    __tablename__: table name
    place_id: place id
    user_id: user id
    text: review description
    """
    __tablename__ = "reviews"
    if getenv("HBNB_TYPE_STORAGE") == "db":

        place_id = Column(String(60),
                          ForeignKey("places.id"))
        user_id = Column(String(60),
                         ForeignKey("users.id"))
        text = Column(String(1024),
                      nullable=False)
    else:

        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)
