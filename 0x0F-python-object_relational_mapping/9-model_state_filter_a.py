#!/usr/bin/python3
"""All cities by state"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import MySQLdb
import sys

if __name__ == '__main__':

    host = "localhost"
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, password, database))

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State.id, State.name).order_by(State.id)\
        .filter(State.name.like('%a%'))

    for match in state:
        print("{}: {}".format(match.id, match.name))
