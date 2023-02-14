from typing import Dict

from fastapi import APIRouter, Depends, HTTPException, status

from api.v1.utils.create_token import create_token
from core.hashing import Hash
from models.schemas import UserInSchemas, Login, UserSchemas
from services.user_services import UserServices, get_user_service, get_hasher

router = APIRouter()


@router.post("/register")
def create(request: UserInSchemas, user_service: UserServices = Depends(get_user_service), hasher: Hash = Depends(get_hasher)) -> int:
    for c in user_service.session.query(user_service.model):
        if c.email == request.email:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="This user is already registered.")
    user_service.create(name=request.name, email=request.email, password=hasher.bcrypt(request.password))
    return status.HTTP_201_CREATED


@router.post("/login")
def login(request: Login, user_service: UserServices = Depends(get_user_service), hasher: Hash = Depends(get_hasher)) -> Dict[str, str]:
    user = user_service.session.query(user_service.model).filter_by(email=request.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This user is not registered.")

    if not hasher.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Password or login was entered incorrectly")

    access_token = create_token(data={"user_id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}
