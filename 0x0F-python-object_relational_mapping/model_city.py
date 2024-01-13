#!/usr/bin/python3
"""Defines class City
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State

Base = declarative_base()


class City(Base):
    """City class that inherits from Base

    Attribute:
        id: represents a column of an auto-generated, unique integer,
            can’t be null and is a primary key
        name: represents a column of a string with maximum 128 characters
             and can’t be null
        state_id: represents a column of an integer, can’t be null and
             is a foreign key to states.id
    """
    __tablename__ = "cities"
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("state.id") , nullable=False)
