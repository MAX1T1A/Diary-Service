from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.v1.utils.auth_bearer import JWTBearer
from db.postgres import get_db
from diary import schemas, service
from models.models import Diary, Page, User

router = APIRouter()


@router.post("/diary", response_model=schemas.DiaryCreate)
async def create_diary(item: schemas.DiaryCreate, db: Session = Depends(get_db), user_id: User = Depends(JWTBearer())):
    db_item = Diary(**item.dict(), user_id=user_id)
    return service.create_items(db=db, db_item=db_item)


@router.get("/diary", response_model=List[schemas.DiaryGet])
async def get_diary_list(db: Session = Depends(get_db), user_id: User = Depends(JWTBearer())):
    return service.get_diary(db=db, user_id=user_id)


@router.post("/page", response_model=schemas.PageCreate)
async def create_page(item: schemas.PageCreate, db: Session = Depends(get_db)):
    db_item = Page(**item.dict())
    return service.create_items(db=db, db_item=db_item)


# @router.get("/page", response_model=List[schemas.PageGet])
# def get_page(diary_id: Page, db: Session = Depends(get_db)):
#     return service.get_page(db=db, diary_id=diary_id)
