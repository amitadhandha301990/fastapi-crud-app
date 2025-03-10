from database import Base
from sqlalchemy import String,Integer,Column
from pydantic import BaseModel, EmailStr
from typing import List


class Usermodel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name=Column(String(50))
    email = Column(String(255), unique=True)
    password=Column(String(50))
    phone_no=Column(Integer,nullable=False)
    address=Column(String(255))
    city=Column(String(50))
    state=Column(String(50))
    Country=Column(String(40))
    zip=Column(Integer,nullable=False)
    photo=Column(String(255))



class EmailSchema(BaseModel):
    email: List[EmailStr]
