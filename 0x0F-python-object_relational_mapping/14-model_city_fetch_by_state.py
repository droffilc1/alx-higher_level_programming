#!/usr/bin/python3
"""Prints all City objects from the database hbtn_0e_14_usa
"""
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for inst in session.query(State.name, City.id, City.name).filter(
            State.id == City.state_id).order_by(City.id):
        print("{:s}: ({:d}) {:s}".format(inst[0], inst[1], inst[2]))

    session.close()
