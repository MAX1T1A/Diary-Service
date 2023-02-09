from sqlalchemy.orm import Session

from models.models import Diary


def get_diary(db: Session, user_id: int):
    return db.query(Diary).filter(Diary.user_id == user_id).all()
