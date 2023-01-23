from typing import Optional

from pydantic import BaseModel


class UserSchemas(BaseModel):
    email: str
    login: str
    password: str


class LoginSchemas(BaseModel):
    login: str
    password: str
