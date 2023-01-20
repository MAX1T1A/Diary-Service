from fastapi import APIRouter, HTTPException, status, Depends
from models.token import Token, Login
from repositories.user import UserRepository
from core.security import verify_password, create_access_token
from api.v1.depends import get_user_repository

router = APIRouter()


@router.post("/auth", response_model=Token)
async def login(log: Login, users: UserRepository = Depends(get_user_repository)):
    user = await users.get_by_email(log.email)
    if user is None or not verify_password(log.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    return Token(
        access_token=create_access_token({"sub": user.email}),
        token_type="Bearer"
    )
