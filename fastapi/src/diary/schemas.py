from pydantic import BaseModel


class DiaryBase(BaseModel):
    name: str
    # user_id: int
    # id: int

    class Config:
        orm_mode = True


class DiaryCreate(DiaryBase): ...


class DiaryUpdate(DiaryBase): ...


class DiaryGet(DiaryBase): ...


class PageBase(BaseModel):
    name: str
    note_content: str
    # diary_id: int
    # id: int

    class Config:
        orm_mode = True


class PageCreate(PageBase): ...


class PageUpdate(PageBase): ...


class PageGet(PageBase): ...


class PageDelete(PageBase): ...
