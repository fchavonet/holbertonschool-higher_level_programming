#!/usr/bin/python3
"""
Module that defines the `City` class and initializes a `Base` object.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    Represents a city for a MySQL database.

    Attributes:
        id (int): an auto-generated, unique integer
                  representing the state's ID.
        name (str): a string with a maximum of
                    128 characters representing the city's name.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id", ondelete="CASCADE"))
