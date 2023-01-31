from pydantic import BaseModel


class DiaryBase(BaseModel):
    diary_name: str
    diary_description: str
    user_id: int

    class Config:
        orm_mode = True


class DiaryCreate(DiaryBase):
    pass


class DiaryUpdate(DiaryBase):
    id: int


class DiaryGet(DiaryBase):
    id: int


class PageBase(BaseModel):
    page_name: str
    note_content: str
    diary_id: int

    class Config:
        orm_mode = True


class PageCreate(PageBase):
    pass


class PageUpdate(PageBase):
    id: int


class PageGet(PageBase):
    id: int


class PageDelete(PageBase):
    id: int
