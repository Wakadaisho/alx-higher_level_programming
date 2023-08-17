#!/usr/bin/python3
"""
Module 8-model_state_fetch_first
Get the first State from the database hbtn_0e_6_usa using sqlalchemy
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
        row = session.query(State).first()
        if (row):
            print("{:d}: {:s}".format(row.id, row.name))
        else:
            print("Nothing")
