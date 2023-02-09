from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.v1.utils.auth_bearer import JWTBearer
from db.postgres import get_db
from models.schemas import DiaryBase, DiaryGet
from models.models import User
from services import diary_services

router = APIRouter(
    prefix="/diary"
)


@router.get("", response_model=List[DiaryGet])
async def get_diary_list(db: Session = Depends(get_db), author: User = Depends(JWTBearer())):
    return diary_services.get(db, author)


@router.post("", response_model=DiaryBase)
async def create_diary(request: DiaryBase, author: User = Depends(JWTBearer()), db: Session = Depends(get_db)):
    return diary_services.create(request, author, db)


@router.delete("/{diary_id}", response_model=int)
async def destroy_diary(diary_id: int, author: User = Depends(JWTBearer()), db: Session = Depends(get_db)):
    return diary_services.destroy(diary_id, author, db)


@router.put("/{diary_id}", response_model=int)
async def update_diary(diary_id: int, request: DiaryBase, author: User = Depends(JWTBearer()), db: Session = Depends(get_db)):
    return diary_services.update(diary_id, request, author, db)
