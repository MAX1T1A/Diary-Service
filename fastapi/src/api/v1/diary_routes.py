from typing import List
from fastapi import APIRouter, Depends
from api.v1.utils.auth_bearer import JWTBearer
from models.schemas import DiaryBase, DiaryGet
from models.models import User
from services.diary_services import DiaryServices

router = APIRouter()


@router.get("/diary", response_model=List[DiaryGet])
async def get(author: User = Depends(JWTBearer())):
    return DiaryServices().get_diary(author)


@router.post("/diary", response_model=DiaryBase)
async def create(request: DiaryBase, author: User = Depends(JWTBearer())):
    return await DiaryServices().create_diary(request, author)


@router.delete("/{diary_id}", response_model=int)
async def delete(diary_id: int, author: User = Depends(JWTBearer())):
    return DiaryServices().delete_diary(id=diary_id, user_id=author)


@router.put("/{diary_id}", response_model=int)
async def update(diary_id: int, request: DiaryBase, author: User = Depends(JWTBearer())):
    return DiaryServices().update_diary(request, id=diary_id, user_id=author)
