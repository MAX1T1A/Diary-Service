from pydantic import BaseModel, constr, EmailStr, validator


class User(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserIn(BaseModel):
    name: str
    email: EmailStr
    password: constr(min_length=8, max_length=20)
    password2: str

    @validator("password2")
    def password_match(cls, password2, values):
        if 'password' in values and password2 != values["password"]:
            raise ValueError("Passwords don't match")
        return password2

