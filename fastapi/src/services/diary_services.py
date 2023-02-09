from sqlalchemy.orm import Session
from fastapi import status
from models.models import Diary
from models.schemas import DiaryBase, DiaryGet, DiaryDestroy


def get(db: Session, author: int) -> DiaryGet:
    return db.query(Diary).filter(Diary.user_id == author).all()


def create(request: DiaryBase, author: int, db: Session) -> Diary:
    diary = Diary(
        name=request.name,
        user_id=author
    )
    db.add(diary)
    db.commit()
    db.refresh(diary)
    return diary


def destroy(request: DiaryDestroy, author: int, db: Session) -> int:
    diary = db.query(Diary).filter(Diary.id == request.id, Diary.user_id == author).first()
    db.delete(diary)
    db.commit()
    return status.HTTP_200_OK
