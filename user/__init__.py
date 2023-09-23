from pydantic import BaseModel


class UserRegisterModel(BaseModel):
    name: str
    surname: str
    phone_number: int
    email: str
    password: str
    profile_photo: str = 'None'
    city: str



