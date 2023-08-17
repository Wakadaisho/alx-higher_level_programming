#!/usr/bin/python3

"""
Module relationship_city.py
Contains class representing a City ORM model
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """City class, inherites Base
    Links to the MySQL table cities
    """
    __tablename__ = "cities"

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
