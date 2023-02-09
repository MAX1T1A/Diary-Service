from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.v1.utils.auth_bearer import JWTBearer
from db.postgres import get_db
from models.schemas import DiaryBase, DiaryGet, DiaryDestroy
from models.models import User
from services import diary_services

router = APIRouter()


@router.get("/diary", response_model=List[DiaryGet])
async def get_diary_list(db: Session = Depends(get_db), author: User = Depends(JWTBearer())):
    return diary_services.get(db, author)


@router.post("/diary", response_model=DiaryBase)
async def create_diary(request: DiaryBase, author: User = Depends(JWTBearer()), db: Session = Depends(get_db)):
    return diary_services.create(request, author, db)


@router.delete("/{diaryId}", response_model=int)
async def destroy_diary(request: DiaryDestroy, author: User = Depends(JWTBearer()), db: Session = Depends(get_db)):
    return diary_services.destroy(request, author, db)
