from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker ,scoped_session
from fastapi_mail import ConnectionConfig
from smtplib import SMTP

SQLALCHEMY_DB_URL=("mysql+mysqlconnector://root@localhost:3306/users")

engine= create_engine(SQLALCHEMY_DB_URL)

conn=engine.connect()

SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))


Base= declarative_base()


def get_db():
    db = SessionLocal
    try:
        yield db
    finally:
        db.close()


class Config:
    orm_mode = True

conf = ConnectionConfig(

    MAIL_USERNAME = "c2ba5ee6a4cea9",
    MAIL_PASSWORD = "105e726496cfc2",
    MAIL_FROM = "amita.dhandha301990@gmail.com",
    MAIL_PORT = 465,
    MAIL_SERVER ="smtp.mailtrap.io",
    MAIL_FROM_NAME="Desired Name",
    MAIL_STARTTLS = False,
    MAIL_SSL_TLS = True,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)

