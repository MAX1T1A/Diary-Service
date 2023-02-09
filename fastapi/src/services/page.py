from sqlalchemy.orm import Session

from models.models import Page


def get_page(db: Session, diary_id: int):
    return db.query(Page).filter(Page.diary_id == diary_id).all()
