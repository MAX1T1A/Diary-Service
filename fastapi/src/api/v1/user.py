from typing import List
from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from api.v1.depends import get_user_repository, get_current_user
from models.user import User, UserIn
from repositories.user import UserRepository

router = APIRouter()


@router.get("/users", response_model=List[User])
async def get_users(
        users: UserRepository = Depends(get_user_repository),
        limit: int = 100,
        skip: int = 0
):
    return await users.get_all(limit=limit, skip=skip)


@router.post("/user/create", response_model=User)
async def create_user(
        user: UserIn,
        users: UserRepository = Depends(get_user_repository)
):
    return await users.create(user=user)


@router.put("/user/update", response_model=User)
async def update_user(
        pk: int,
        user: UserIn,
        users: UserRepository = Depends(get_user_repository),
        current_user: User = Depends(get_current_user)
):
    old_user = await users.get_by_id(pk)
    if old_user is None or old_user.email != current_user.email:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found user")
    return await users.update(pk, user=user)

