#!/usr/bin/python3
"""
Module 9-model_state_filter_a
Get all States whose name contains an 'a'
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
        for row in session  .query(State) \
                            .filter(State.name.contains('a')) \
                            .order_by(State.id):
            print("{:d}: {:s}".format(row.id, row.name))
