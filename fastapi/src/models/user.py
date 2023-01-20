from typing import Optional

from pydantic import BaseModel, EmailStr, validator, constr


class User(BaseModel):
    id: int
    email: EmailStr
    name: str
    password: str


class UserIn(BaseModel):
    name: str
    email: EmailStr
    password: constr(min_length=8)
    password_repeat: str

    @validator("password_repeat")
    def password_verification(cls, value, values):
        if 'password' in values and value != values["password"]:
            raise ValueError("Passwords don't match")
        return value
