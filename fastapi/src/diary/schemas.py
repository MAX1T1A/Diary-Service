from pydantic import BaseModel


class DiaryBase(BaseModel):
    name: str
    description: str


class DiaryCreate(DiaryBase):
    pass


class DiaryUpdate(DiaryBase):
    id: int


class DiaryGet(DiaryBase):
    id: int


class PageBase(BaseModel):
    name: str
    body: str


class PageCreate(PageBase):
    pass


class PageUpdate(PageBase):
    id: int


class PageGet(PageBase):
    id: int


class PageDelete(PageBase):
    id: int
