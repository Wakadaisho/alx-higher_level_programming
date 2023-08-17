#!/usr/bin/python3
"""
Module 12-model_state_update
Updates the name of the State with an id of 2
into the database hbtn_0e_6_usa using sqlalchemy
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine, orm


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1],
                                   argv[2],
                                   argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    with orm.sessionmaker(bind=engine)() as session:
        session.get(State, 2).name = "New Mexico"
        session.commit()
