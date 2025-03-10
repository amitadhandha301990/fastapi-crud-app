from pydantic import BaseModel


class UserSchemas(BaseModel):
    id: int
    name: str
    email: str
    password: str
    phone_no: int
    address: str
    city: str
    state: str
    Country: str
    zip: int
    photo: str
