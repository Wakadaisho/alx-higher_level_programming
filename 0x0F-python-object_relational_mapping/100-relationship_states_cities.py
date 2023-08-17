#!/usr/bin/python3
"""
Module 100-relationship_states_cities
Creates a new State and City, with the City
referencing the State
in the database hbtn_0e_100_usa using sqlalchemy
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
        state = State(name="California")
        city = City(name="San Francisco", state=state)
        session.add(state)
        session.add(city)
        session.commit()
