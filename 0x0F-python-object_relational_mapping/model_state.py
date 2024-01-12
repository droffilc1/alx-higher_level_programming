#!/usr/bin/python3
"""Defines class State
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# an instance
Base = declarative_base()


class State(Base):
    """State class that inherits from Base

    Attribute:
        id: represents a column of an auto-generated, unique integer,
            can’t be null and is a primary key
        name: represents a column of a string with maximum 128 characters
             and can’t be null
    """
    __tablename__ = "states"
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
