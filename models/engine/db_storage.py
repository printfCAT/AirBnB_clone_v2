#!/usr/bin/python3
""" This module defines a class that handles the storage for the application"""

from os import getenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import SQLAlchemyError
import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

model_classes = {"Amenity": Amenity, "City": City, "Place": Place,
                 "Review": Review, "State": State, "User": User
                 }


class DBStorage:
    """ Defines a class that handles db storage of the models """

    __engine = None
    __session = None

    def __init__(self):
        """ Constructor for the DBStorage class """
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')

        try:
            self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}/{}'.format(
                    user, password, host, db),
                pool_pre_ping=True, echo=True)

            if getenv('HBNB_ENV') == 'test':
                Base.metadata.drop_all(self.__engine)

        except SQLAlchemyError as e:
            print('An error occured during engine creation:')
            print(str(e))

    def all(self, cls=None):
        """ retrieves all data in table cls or all tables if cls=None """

        cls_dict = {}

        for model in model_classes:
            if cls is None or cls is model_classes[model] or cls is model:
                objs = self.__session.query(model_classes[model]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    cls_dict[key] = obj
        return cls_dict

    def new(self, obj):
        """ Add obj to current db session """
        self.__session.add(obj)

    def save(self):
        """ saves all transactions of current session to db"""
        self.__session.commit()

    def delete(self, obj=None):
        """ delete obj from current session """
        if obj is not None:
            self.__session.delete(obj)
        pass

    def reload(self):
        """ reloads data from db """
        Base.metadata.create_all(self.__engine)
        sessionFactory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sessionFactory)
        self.__session = Session
