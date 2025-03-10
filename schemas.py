from pydantic import BaseModel,List
from pydantic import EmailStr


class UserSchemas(BaseModel):
        id =int
        name=str
        email = str
        password=str
        phone_no=int
        address=str
        city=str
        state=str
        Country=str
        zip=int
        photo=str


class EmailSchema(BaseModel):
    email: List[EmailStr]
