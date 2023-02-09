from typing import Dict

from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.models import User
from models.schemas import UserInSchemas, Login
from core.hashing import Hash
from api.v1.utils.create_token import create_token


def create(request: UserInSchemas, db: Session) -> User:
    new_user = User(
        name=request.name,
        email=request.email,
        password=Hash().bcrypt(request.password)
    )
    for c in db.query(User):
        if c.email == request.email:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="This user is already registered")
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def login(request: Login, db: Session) -> Dict[str, str]:
    user = db.query(User).filter(User.email == request.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This user is not registered")

    if not Hash().verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Password or login was entered incorrectly")

    access_token = create_token(data={"user_id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}
