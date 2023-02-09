from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.v1.utils.auth_bearer import JWTBearer
from db.postgres import get_db
from models.schemas import DiaryBase
from models.models import Diary, User
from services import base, diary

router = APIRouter()


@router.post("/diary", response_model=DiaryBase)
async def create_diary(item: DiaryBase, db: Session = Depends(get_db), user_id: User = Depends(JWTBearer())):
    db_item = Diary(**item.dict(), user_id=user_id)
    return base.create_items(db=db, db_item=db_item)


@router.get("/diary", response_model=List[DiaryBase])
async def get_diary_list(db: Session = Depends(get_db), user_id: User = Depends(JWTBearer())):
    return diary.get_diary(db=db, user_id=user_id)
