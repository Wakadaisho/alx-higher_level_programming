#!/usr/bin/python3

"""
Module relationship_state.py
Contains class representing a State ORM model
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """State class, inherites Base
    Links to the MySQL table states
    """
    __tablename__ = "states"

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City",
                          backref="state",
                          cascade="all, delete-orphan",
                          lazy="dynamic")
