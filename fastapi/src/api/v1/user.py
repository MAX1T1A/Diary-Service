from fastapi import APIRouter, Depends
from db.postgres import get_db
from sqlalchemy.orm import Session
from models.schemas import UserIn
from repository.user import create

router = APIRouter(tags=['Auth'])


@router.post('/register')
def create_user(request: UserIn, db: Session = Depends(get_db)):
    return create(request, db)
