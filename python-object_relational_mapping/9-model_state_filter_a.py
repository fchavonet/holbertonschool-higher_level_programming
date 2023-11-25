#!/usr/bin/python3
"""
Module that lists all State objects that contain the letter a from a database.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).first()

    for state in session.query(State).filter(State.name.ilike("%a%")):
        print("{}: {}".format(state.id, state.name))

    session.close()
