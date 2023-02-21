from fastapi import HTTPException, status
from pydantic import BaseModel, constr, EmailStr, validator


class UserSchemas(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserInSchemas(BaseModel):
    name: str
    email: EmailStr
    password: constr(min_length=8, max_length=20)
    password2: str

    @validator("password2")
    def password_match(cls, password2, values):
        if 'password' in values and password2 != values["password"]:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Passwords don't match.")
        return password2


class Login(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: int


class DiaryUniversal(BaseModel):
    name: str


class DiaryGet(DiaryUniversal):
    id: int


class PageUniversal(BaseModel):
    name: str
    body: str


class PageGet(PageUniversal):
    id: int
