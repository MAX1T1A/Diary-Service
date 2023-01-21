from fastapi import Depends, HTTPException
from starlette import status

from core.security import JWTBearer, decode_access_token
from db.postgres import database
from models.user import User
from repositories.user import UserRepository


def get_user_repository() -> UserRepository:
    return UserRepository(database)


async def get_current_user(
    users: UserRepository = Depends(get_user_repository),
    token: str = Depends(JWTBearer()),
) -> HTTPException | User:
    cred_exception = HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Credentials are not valid")
    payload = decode_access_token(token)
    if payload is None:
        raise cred_exception
    email: str = payload.get("sub")
    if email is None:
        raise cred_exception
    user = await users.get_by_email(email=email)
    if user is None:
        return cred_exception
    return user
