from sqlalchemy.orm import Session

from models.models import Diary, Page
from .schemas import DiaryCreate, PageBase


def create_diary(db: Session, item: DiaryCreate):
    db_item = Diary(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def create_page(db: Session, item: PageBase):
    db_item = Page(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_diary(db: Session):
    return db.query(Diary).all()

