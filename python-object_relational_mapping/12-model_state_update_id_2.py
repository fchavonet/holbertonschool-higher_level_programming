#!/usr/bin/python3
"""
Module that  that changes the name of a State object from a database.
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

    state_update = session.query(State).filter(State.id == 2).first()

    if state_update:
        state_update.name = "New Mexico"
        session.commit()

    session.close()
