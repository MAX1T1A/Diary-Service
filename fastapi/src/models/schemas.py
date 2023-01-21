from typing import List, Optional

from pydantic import BaseModel


class PageBase(BaseModel):
    name: str
    body: str


class Page(PageBase):
    class Config:
        orm_mode = True


class Diary(BaseModel):
    name: str


class ShowDiary(BaseModel):
    name: str
    page: Optional[Page]


class User(BaseModel):
    email: str
    name: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str
    diary: Optional[Diary]

    class Config:
        orm_mode = True


class ShowPage(BaseModel):
    name: str
    body: str
    creator: ShowUser


class Login(BaseModel):
    name: str
    password: str
