from sqlalchemy.orm import Session
from fastapi import status, HTTPException
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
    if not diary:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This diary doesn't exist")
    db.delete(diary)
    db.commit()
    return status.HTTP_200_OK
