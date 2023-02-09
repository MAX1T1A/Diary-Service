from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.postgres import get_db
from models.schemas import PageBase
from models.models import Page
from services.base import create_items

router = APIRouter()


@router.post("/page", response_model=PageBase)
async def create_page(item: PageBase, db: Session = Depends(get_db)):
    db_item = Page(**item.dict())
    return create_items(db=db, db_item=db_item)

# @router.get("/page", response_model=List[schemas.PageGet])
# def get_page(diary_id: Page, db: Session = Depends(get_db)):
#     return service.get_page(db=db, diary_id=diary_id)
