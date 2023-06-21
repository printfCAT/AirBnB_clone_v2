#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if getenv('HBNB_TYPE_STORAGE') == 'db':

        name = Column(String(128), nullable=False)
        cities = relationship('City', back_populates='state',
                              cascade='all, delete')
    else:

        @property
        def cities(self):
            """ get a list of cities associated with current state instance """
            list_cities = []

            for city in models.storage.all("city").values():
                if city.state_id == self.id:
                    list_cities.append(city)

            return list_cities
