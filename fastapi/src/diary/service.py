from sqlalchemy.orm import Session

from models.models import Diary, Page
from .schemas import DiaryCreate, PageBase


def db_func(db: Session, db_item):
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def create_diary(db: Session, item: DiaryCreate, **kwargs):
    db_item = Diary(**item.dict(), **kwargs)
    return db_func(db, db_item)


def create_page(db: Session, item: PageBase):
    db_item = Page(**item.dict())
    return db_func(db, db_item)


def get_diary(db: Session, user_id: int):
    return db.query(Diary).filter(Diary.user_id == user_id).all()
