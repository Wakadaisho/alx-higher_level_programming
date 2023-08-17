#!/usr/bin/python3
"""
Module 101-relationship_states_cities_list
List all State objects with corresponding City objects
from the database hbtn_0e_101_usa using sqlalchemy
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
        for state in session.query(State).order_by(State.id):
            print("{:d}: {:s}".format(state.id, state.name))
            for city in state.cities:
                print("\t{:d}: {:s}".format(city.id, city.name))
