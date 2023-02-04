from sqlalchemy.orm import Session

from models.models import Diary, Page


def create_items(db: Session, db_item):
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_diary(db: Session, user_id: int):
    return db.query(Diary).filter(Diary.user_id == user_id).all()


def get_page(db: Session, diary_id: int):
    return db.query(Page).filter(Page.diary_id == diary_id).all()
