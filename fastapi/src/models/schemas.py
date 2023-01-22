from typing import Optional

from pydantic import BaseModel


class PageBaseSchemas(BaseModel):
    diary_id: int
    name: str
    body: str


# class PageSchemas(PageBaseSchemas):
#     class Config:
#         orm_mode = True


class DiarySchemas(BaseModel):
    user_id: int
    name: str


# class ShowDiarySchemas(BaseModel):
#     name: str
#     page: Optional[PageSchemas]


class UserSchemas(BaseModel):
    email: str
    name: str
    password: str


# class ShowUserSchemas(BaseModel):
#     name: str
#     email: str
#     diary: Optional[DiarySchemas]
#
#     class Config:
#         orm_mode = True


# class ShowPageSchemas(BaseModel):
#     name: str
#     body: str
#     creator: ShowUserSchemas


# class LoginSchemas(BaseModel):
#     name: str
#     password: str
