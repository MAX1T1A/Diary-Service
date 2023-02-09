from fastapi import APIRouter, Depends
from db.postgres import get_db
from sqlalchemy.orm import Session
from models.schemas import UserInSchemas, Login
from services.user_services import create, login

router = APIRouter(
    prefix="/user"
)


@router.post("/register")
async def create_user(request: UserInSchemas, db: Session = Depends(get_db)):
    return create(request, db)


@router.post("/login")
async def login_user(request: Login, db: Session = Depends(get_db)):
    return login(request, db)
