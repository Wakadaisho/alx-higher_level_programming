#!/usr/bin/python3
"""
Module 14-model_city_fetch_by_state
Prints all City objects in ascending id
from the database hbtn_0e_6_usa using sqlalchemy
"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine, orm


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1],
                                   argv[2],
                                   argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    with orm.sessionmaker(bind=engine)() as session:
        for c, s in session .query(City, State) \
                            .join(State):
            print("{:s}: ({:d}) {:s}".format(s.name, c.id, c.name))
