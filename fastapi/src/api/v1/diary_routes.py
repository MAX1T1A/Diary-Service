from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.v1.utils.auth_bearer import JWTBearer
from db.postgres import get_db
from diary import schemas, service
from models.models import User

router = APIRouter(tags=['Diary'])


@router.post("/diary", response_model=schemas.DiaryCreate)
async def create_diary(
        item: schemas.DiaryCreate,
        db: Session = Depends(get_db),
        user_id: User = Depends(JWTBearer())):
    return service.create_diary(db=db, item=item, user_id=user_id)


@router.get("/diary", response_model=List[schemas.DiaryGet])
async def get_diary_list(db: Session = Depends(get_db), user_id: User = Depends(JWTBearer())):
    return service.get_diary(db=db, user_id=user_id)


@router.post("/page", response_model=schemas.PageCreate)
def create_page(item: schemas.PageCreate, db: Session = Depends(get_db)):
    return service.create_page(db=db, item=item)
