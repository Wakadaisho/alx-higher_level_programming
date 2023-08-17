#!/usr/bin/python3
"""
Module 10-model_state_my_get
Prints the State object id of a named State
from the database hbtn_0e_6_usa using sqlalchemy
"""

from sys import argv
from model_state import State
from sqlalchemy import create_engine, orm


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1],
                                   argv[2],
                                   argv[3]),
                           pool_pre_ping=True)

    with orm.sessionmaker(bind=engine)() as session:
        row = session   .query(State) \
                        .filter(State.name == argv[4]) \
                        .first()
        if (row):
            print("{:d}".format(row.id))
        else:
            print("Not found")
