from typing import Optional

from pydantic import BaseModel, EmailStr, constr, validator


class UserSchemas(BaseModel):
    id: Optional[str] = None
    name: str
    email: EmailStr
    hashed_password: str


class RegisterUserSchemas(BaseModel):
    name: str
    email: EmailStr
    password: constr(min_length=8)
    password2: str

    @validator("password2")
    def password_match(cls, password2, values):
        if "password" in values and password2 != values["password"]:
            raise ValueError("Passwords don't match")
        return password2


class LoginUserSchemas(BaseModel):
    name: str
    password: str
