from pydantic import BaseModel


class Diary(BaseModel):
    id: int
    name: str


class DiaryIn(BaseModel):
    name: str
