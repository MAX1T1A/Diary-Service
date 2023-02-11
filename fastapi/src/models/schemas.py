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
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Passwords don't match")
        return password2


class Login(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: int


class DiaryBase(BaseModel):
    name: str
    # user_id: int
    # id: int

    class Config:
        orm_mode = True


class DiaryGet(DiaryBase):
    id: int


class DiaryDestroy(BaseModel):
    id: int


class PageBase(BaseModel):
    name: str

    class Config:
        orm_mode = True


class PageGet(PageBase):
    id: int


class PageCreate(PageBase):
    body: str


class PageDestroy(BaseModel):
    id: int
    diary_id: int
