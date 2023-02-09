from sqlalchemy.orm import Session
from fastapi import status, HTTPException
from models.models import Diary
from models.schemas import DiaryBase, DiaryGet


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


def destroy(user_id: int, author: int, db: Session) -> int:
    diary = db.query(Diary).filter(Diary.id == user_id, Diary.user_id == author).first()
    if not diary:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This diary doesn't exist")
    db.delete(diary)
    db.commit()
    return status.HTTP_204_NO_CONTENT


def update(diary_id: int, request: DiaryBase, author: int, db: Session) -> int:
    diary = db.query(Diary).filter(Diary.id == diary_id, Diary.user_id == author).first()
    if not diary:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This diary doesn't exist")
    diary.name = request.name
    db.commit()
    return status.HTTP_200_OK
