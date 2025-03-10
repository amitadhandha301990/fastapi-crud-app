from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker ,scoped_session

SQLALCHEMY_DB_URL=("mysql+mysqlconnector://root@localhost:3306/users")

engine= create_engine(SQLALCHEMY_DB_URL)

conn=engine.connect()

SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))


Base= declarative_base()