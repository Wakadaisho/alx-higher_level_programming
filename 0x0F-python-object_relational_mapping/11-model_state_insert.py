#!/usr/bin/python3
"""
Module 11-model_state_insert
Inserts the State 'Louisiana' into table state,
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
        record = State(name='Louisiana')
        session.add(record)
        session.commit()

        print("{:d}".format(record.id))
