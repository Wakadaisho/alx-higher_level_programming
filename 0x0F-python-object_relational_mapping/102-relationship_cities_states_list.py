#!/usr/bin/python3
"""
Module 102-relationship_cities_states_list
List all City objects from the database hbtn_0e_101_usa using sqlalchemy
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine, orm


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1],
                                   argv[2],
                                   argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    with orm.sessionmaker(bind=engine)() as session:
        for city in session.query(City).order_by(City.id):
            print("{:d}: {:s} -> {:s}"
                  .format(city.id, city.name, city.state.name))
