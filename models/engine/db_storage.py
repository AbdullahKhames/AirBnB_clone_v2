#!/usr/bin/python3
"""db storage module to define session and engine"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.engine.available_class import FileUtil
from os import getenv


class DBStorage:
    """
    class DBStorage that will contain connection properties and
    manages all db interactions
    """
    __engine = None
    __session = None

    def __init__(self):
        from models.base_model import Base
        """
        init function to initialize the DBStorage object
        """
        connection_str = (
            f"mysql+mysqldb://{getenv('HBNB_MYSQL_USER')}:"
            f"{getenv('HBNB_MYSQL_PWD')}@"
            f"{getenv('HBNB_MYSQL_HOST')}:3306/"
            f"{getenv('HBNB_MYSQL_DB')}"
        )
        self.__engine = create_engine(connection_str, pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine, checkfirst=False)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage by class"""
        from models.base_model import BaseModel
        self.reload()
        fetched_objects = {}
        if cls is None or cls == "":
            classes = list(FileUtil.my_Classes.values())
            for curr in classes:
                if curr in [BaseModel]:
                    continue
                records = self.__session.query(curr).all()
                for record in records:
                    key = f"{curr.__name__}.{record.id}"
                    fetched_objects[key] = record
            return fetched_objects
        else:
            records = self.__session.query(cls).all()
            for record in records:
                key = f"{cls.__name__}.{record.id}"
                fetched_objects[key] = record
            return fetched_objects

    def new(self, obj):
        """Adds new object to storage session"""
        self.__session.add(obj)

    def save(self):
        """Saves storage session and commits to database"""
        self.__session.commit()

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import Base

        Base.metadata.create_all(bind=self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def delete(self, obj=None):
        """delete object from __objects f it’s inside"""
        if obj is None:
            return
        else:
            for k, v in FileUtil.my_Classes.items():
                if k == obj.__class__.__name__:
                    toDelete = (self.__session.query(v)
                                .filter(v.id == obj.id).first())
                    self.__session.delete(toDelete)

    def close(self):
        self.__session.remove()
